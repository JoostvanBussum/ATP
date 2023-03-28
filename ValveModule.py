class ValveModule:

    def adjustPH(self, currentPH: float, goalPH: float):
        if currentPH > goalPH:
            return -0.05
        return 0.05