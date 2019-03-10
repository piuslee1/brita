import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
from matplotlib import pylab
import xlrd

<<<<<<< HEAD
loc = (r'C:\Users\Luke Piszkin\Downloads\TestData (1).xlsx') #copy and paste file path
=======
loc = (r'C:\Users\Luke Piszkin\Downloads\TestData (2).xlsx') #copy and paste file path
>>>>>>> Added arduino script

wb = xlrd.open_workbook(loc) #Open a new workbook
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
  
y = []
for i in range(sheet.nrows): #for each row append array with the value
    y.append(sheet.cell_value(i, 0)) 

<<<<<<< HEAD
x = np.arange(0,20,1) #make an array to represent time, with whatever bounds and intervals line up with the data
=======
x = np.arange(0,10,1) #make an array to represent time, with whatever bounds and intervals line up with the data
>>>>>>> Added arduino script

def sd_func(d):
    return np.sqrt(np.sum(np.square(d - np.mean(d)))/(len(d)-1)) #define a function to calculate standard deviation

print("Standard Deviation", sd_func(y))

plt.figure()
plt.errorbar(x, y, yerr = sd_func(y), fmt='bo')
plt.xlabel('Time (min)')
plt.ylabel('Sensor Reading (volts)')
plt.title('Turbidity Vs. Time')

def exponential_func(x, a, b, c): #define an exponential function
    return a*np.exp(b*x)+c

<<<<<<< HEAD
popt, pcov = curve_fit(exponential_func, x, y, p0=(1, 1e-6, 1)) # I am not sure wtf this does

xx = np.linspace(0, 20) 
=======
popt, pcov = curve_fit(exponential_func, x, y, p0=(1, 1e-6, 1))

xx = np.linspace(0, 10) 
>>>>>>> Added arduino script
yy = exponential_func(xx, *popt) 

plt.plot(x,y,'o', xx, yy)
plt.xlabel('Time (min)')
plt.ylabel('Sensor Reading (volts)')
plt.title('Turbidity Vs. Time')
plt.show()







