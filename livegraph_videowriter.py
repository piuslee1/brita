import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import matplotlib.animation as anim
import ffmpeg

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))



def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = anim.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)

Writer = anim.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ims = []
for add in np.arange(15):
    ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))

im_ani = anim.ArtistAnimation(fig, ims, interval=50, repeat_delay=3000,
                                   blit=True)

im_ani.save('test_liveim.mp4', writer=writer)