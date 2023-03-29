import ctypes
import time
from DS18B20 import readMockedTemperaturevalue
from HeatModule import HeatModule
from loggers import *

# setup for c++ pH library
pHSensor = ctypes.CDLL("PHSensor.so") 
valveModule = ctypes.CDLL("ValveModule.so")

pHSensor.readMockedPHValue.restype = ctypes.c_float
valveModule.adjustPHValue.restype = ctypes.c_float

# variables to be used in the program
goalTemperature = 20
goalPH = 7.5

adjustedHeat = 0
adjustedPH = 0

# heatmodule setup
heatModule = HeatModule()

# set up loggers
adjustTemperature = loggedAdjustHeat(heatModule.adjustTemperature)
readMockedTemperaturevalue = loggedReadTemp(readMockedTemperaturevalue)

while True:
    currentTemperature = round(readMockedTemperaturevalue(goalTemperature - 3 + adjustedHeat, goalTemperature), 2)
    currentPH = round(pHSensor.readMockedPHValue(ctypes.c_float(goalPH - 1 + adjustedPH) , ctypes.c_float(goalPH)), 1)

    if(currentTemperature < goalTemperature - 0.5 or currentTemperature > goalTemperature + 0.5):
        adjustedHeat += adjustTemperature(currentTemperature, goalTemperature)

    if(currentPH < goalPH - 0.1 or currentPH > goalPH + 0.1):
        adjustedPH += valveModule.adjustPHValue(ctypes.c_float(currentPH), ctypes.c_float(goalPH))

    print("temp goal: ", goalTemperature, " current: ", currentTemperature, " added heat: ", adjustedHeat) 
    print("pH goal: ", goalPH, " current: ", currentPH, " added pH: ", adjustedPH)
    print("----------------------------------------------")

    time.sleep(0.5)