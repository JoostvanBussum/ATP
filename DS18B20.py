import random

class SensorInterface:
    def __init__(self):
        pass

    def readValue(self):
        pass

class DS18B20(SensorInterface):
    def __init__(self):
        self.min = 10
        self.max = 20

    def readvalue(self):
        return random.uniform(self.min, self.max)

