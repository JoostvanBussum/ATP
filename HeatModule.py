import DS18B20

class HeatModule:
    def __init__(self, DS18B20Sensor: DS18B20):
        self.DS18B20Sensor = DS18B20Sensor