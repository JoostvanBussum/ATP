import unittest
import ctypes
from DS18B20 import readMockedTemperaturevalue
from HeatModule import HeatModule

class TestWaterMonitoringSystem(unittest.TestCase):

    def test_pHSensorUnitTest(self):
        pHSensor = ctypes.CDLL("C:/Users/Joost/Documents/GitHub/ATP/PHSensor.so") 
        pHSensor.readMockedPHValue.restype = ctypes.c_float

        currentPH = round(pHSensor.readMockedPHValue(ctypes.c_float(6.9) , ctypes.c_float(7.1)), 2)
        goalPH = 7.0

        message = "should be around 7.0 with a margin of error of 0.1"

        self.assertAlmostEqual(currentPH, goalPH, None, message, 0.1)

    def test_DS18B20UnitTest(self):
        currentTemperature = round(readMockedTemperaturevalue(14.5, 15.5), 1)
        goalTemperature = 15.0

        message = "Should be around 15.0 with a margin of error of 0.5"

        self.assertAlmostEqual(currentTemperature, goalTemperature, None, message, 1)

    def test_DS18B20HeatModuleIntegrationTest(self):
        goalTemperature = 20
        adjustedHeat = 0
        currentTemperature = round(readMockedTemperaturevalue(goalTemperature - 3 + adjustedHeat, goalTemperature), 2)

        heatModule = HeatModule()

        while(currentTemperature < goalTemperature - 0.5 or currentTemperature > goalTemperature + 0.5):
            adjustedHeat += heatModule.adjustTemperature(currentTemperature, goalTemperature)
            currentTemperature = round(readMockedTemperaturevalue(goalTemperature - 3 + adjustedHeat, goalTemperature), 2)

        message = "Should be around 20.0 with a margin of error of 0.5"

        self.assertAlmostEqual(currentTemperature, goalTemperature, None, message, 1)
    
    def test_PHSensorValveModuleIntegrationTest(self):
        pHSensor = ctypes.CDLL("C:/Users/Joost/Documents/GitHub/ATP/PHSensor.so") 
        valveModule = ctypes.CDLL("C:/Users/Joost/Documents/GitHub/ATP/ValveModule.so")

        pHSensor.readMockedPHValue.restype = ctypes.c_float
        valveModule.adjustPHValue.restype = ctypes.c_float

        goalPH = 7.5
        adjustedPH = 0
        currentPH = round(pHSensor.readMockedPHValue(ctypes.c_float(goalPH - 2 + adjustedPH) , ctypes.c_float(goalPH)), 1)

        while(currentPH < goalPH - 0.1 or currentPH > goalPH + 0.1):
            adjustedPH += valveModule.adjustPHValue(ctypes.c_float(currentPH), ctypes.c_float(goalPH))
            currentPH = round(pHSensor.readMockedPHValue(ctypes.c_float(goalPH - 2 + adjustedPH) , ctypes.c_float(goalPH)), 1)

        message = "Should be around 7.5 with a margin of error of 0.1"

        self.assertAlmostEqual(currentPH, goalPH, None, message, 0.1)

    def test_systemTest(self):
        pHSensor = ctypes.CDLL("C:/Users/Joost/Documents/GitHub/ATP/PHSensor.so") 
        valveModule = ctypes.CDLL("C:/Users/Joost/Documents/GitHub/ATP/ValveModule.so")

        pHSensor.readMockedPHValue.restype = ctypes.c_float
        valveModule.adjustPHValue.restype = ctypes.c_float

        heatModule = HeatModule()

        goalTemperature = 15
        adjustedHeat = 0

        goalPH = 8.0
        adjustedPH = 0

        currentTemperature = round(readMockedTemperaturevalue(goalTemperature - 3 + adjustedHeat, goalTemperature), 2)
        currentPH = round(pHSensor.readMockedPHValue(ctypes.c_float(goalPH - 1 + adjustedPH) , ctypes.c_float(goalPH)), 1)

        while currentTemperature < goalTemperature - 0.5 or currentTemperature > goalTemperature + 0.5:
            adjustedHeat += heatModule.adjustTemperature(currentTemperature, goalTemperature)
            currentTemperature = round(readMockedTemperaturevalue(goalTemperature - 3 + adjustedHeat, goalTemperature), 2)

        while currentPH < goalPH - 0.1 or currentPH > goalPH + 0.1:
            adjustedPH += valveModule.adjustPHValue(ctypes.c_float(currentPH), ctypes.c_float(goalPH))
            currentPH = round(pHSensor.readMockedPHValue(ctypes.c_float(goalPH - 1 + adjustedPH) , ctypes.c_float(goalPH)), 2)
        
        
        PHMessage = "Should be around 8.0 with a margin of error of 0.1"
        TemperatureMessage = "Should be around 15.0 with a margin of error of 0.5"

        self.assertAlmostEqual(currentPH, goalPH, None, PHMessage, 0.1)
        self.assertAlmostEqual(currentTemperature, goalTemperature, None, TemperatureMessage, 1)

if __name__ == '__main__':
    unittest.main()