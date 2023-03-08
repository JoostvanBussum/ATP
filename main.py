import ctypes
import time
from DS18B20 import readMockedTemperaturevalue

# setup for c++ library
pHSensor = ctypes.CDLL("C:/Users/Joost/Documents/GitHub/ATP/PHSensor.so") 
pHSensor.readMockedPHValue.restype = ctypes.c_float

pHWaarde = pHSensor.readMockedPHValue( ctypes.c_float(7) , ctypes.c_float(10) );

print("pH waarde: %.1f" % round(pHWaarde, 1))
print("temperatuur: ", readMockedTemperaturevalue(15, 20))
while True:

    

    time.sleep(3)