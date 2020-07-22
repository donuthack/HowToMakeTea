from howtomaketea.api.tea.hotwater import HotWater
from howtomaketea.api.tea.Tea import Tea


class Tea_Machine:
    water = int(0)
    temp = int(0)
    boiling_temp = int(100)

    def __init__(self, water, temp):
        self.water = water
        self.temp = temp

    def askHowMuch(self):
        print("Yours water in ml is " + self.water)
        print("Yours water temperature is " + self.temp)

    def boilWater(self):
        water = HotWater(self.water, self.temp)
        water.setHotWater()
        return water.getHotWater()

    def addTea(self):
        return Tea().finalDecisionTea()

    def addAdditions(self):
        return Tea().finalDecisionAddition()

    def getCapacity(self):
        return Tea().getCapacity()

obj = Tea_Machine(524, 110)
#
print(repr(obj.getCapacity()))
#
# y= obj.addAdditions()
# print(repr(y.coconut_milk))

# ['red', 'blue', 'black']
