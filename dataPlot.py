import serial #Import the Serial Library
import numpy as np
import matplotlib.pyplot as plt
from drawnow import * #livestream data library

for i in range(1,7):
    vars()['sensor' + str(i)] = [] #create empty arrays for each plot

arduinoSensorData = serial.Serial('COM3' , 115200) #make a serial object/set your port and baud rate
plt.ion() #Tell matplotlib to have interactive mode on to plot live data
def makeFigure() : #make a plotting function
    fig, axs = plt.subplot(2,3) #create subplots
    axs.ylim(0,100) #set y min and max
    axs.ylabel('Turbidity') #set ylabels
    fig.suptitle('Turbidity Sensors') #set figure title
    for i in range(0,6):
        axs[i].plot(vars()['sensor' + str(i+1)], 'r--', label='Volts') #plot each turbidity sensor

while True: # Continuous loop while we are getting data
    while (arduinoSensorData.inWaiting()==0): #Wait until there is data
        pass #do nothing

    arduinoString = arduinoSensorData.readline() #Reads serial string data
    dataArray = arduinoString.split(",") #Put data into an arrays for each sensor 
    for i in range(1,7):
        vars()["turb" + str(i)] = float(dataArray[i-1])  #store as float values
      
    for i in range(1,7):
        vars()['sensor' + str(i)].append(vars()['turb' + str(i)]) #Update arrays with data stream
 
    drawnow(makeFigure) #Call drawnow to plot live data
    plt.pause(0.000001) #wait a small time before updating




