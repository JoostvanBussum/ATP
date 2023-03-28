def loggedAdjustHeat(f):
    def inner(currentTemp, goalTemp):
        print("adjusting temperature with current temperature of: ", currentTemp, " and a goal temperature of: ", goalTemp)
        return f(currentTemp, goalTemp)
    return inner

def loggedAdjustPH(f):
    def inner(currentPH, goalPH):
        print("adjusting pH with current pH of: ", currentPH, " and a goal pH of: ", goalPH)
        return f(currentPH, goalPH)
    return inner

def loggedReadTemp(f):
    def inner(min, max):
        print("reading mocked temperature between ", min, " and ", max)
        return f(min, max)
    return inner