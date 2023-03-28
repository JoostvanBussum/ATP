class HeatModule:

    def adjustTemperature(self, currentTemp: float, goalTemp: float):
        if currentTemp > goalTemp:
            return -0.05
        return 0.05