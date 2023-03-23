import ctypes
import time
from DS18B20 import readMockedTemperaturevalue
from HeatModule import adjustTemperature
from ValveModule import adjustPH

# setup for c++ pH library
pHSensor = ctypes.CDLL("C:/Users/Joost/Documents/GitHub/ATP/PHSensor.so") 
pHSensor.readMockedPHValue.restype = ctypes.c_float

# variables to be used in the program
goalTemperature = 20
goalPH = 7.5
adjustedHeat = 0
adjustedPH = 0

while True:
    currentTemperature = round(readMockedTemperaturevalue(goalTemperature - 3 + adjustedHeat, goalTemperature), 2)
    currentPH = round(pHSensor.readMockedPHValue(ctypes.c_float(goalPH - 1 + adjustedPH) , ctypes.c_float(goalPH)), 1)

    if(currentTemperature < goalTemperature - 0.5 or currentTemperature > goalTemperature + 0.5):
        adjustedHeat += adjustTemperature(currentTemperature, goalTemperature)

    print("temp goal: ", goalTemperature, " current: ", currentTemperature, " added heat: ", adjustedHeat) 

    if(currentPH < goalPH - 0.1 or currentPH > goalPH + 0.1):
        adjustedPH += adjustPH(currentPH, goalPH)

    print("pH goal: ", goalPH, " current: ", currentPH, " added pH: ", adjustedPH)

    time.sleep(0.5)
#     pass