from .hotwater import HotWater
from .Tea import Tea, Adds, TypeTea
from enum import IntEnum


class Tea_Machine:
    __water = int(0)
    __temp = int(0)
    __boiling_temp = int(100)
    __typeoftea = int(0)
    __adds = []

    def __init__(self, water, temp, teaType, addWeRecive):
        self.__water = water
        self.__temp = temp
        self.__typeoftea = teaType
        self.__addWeRecive = addWeRecive

    def getTypeTea(self):
        try:
            if self.__typeoftea in TypeTea[self.__typeoftea].name:
                return TypeTea[self.__typeoftea].value
        except:
            self.__typeoftea = [TypeTea.black_tea.value]
            return self.__typeoftea

    def getAddition(self):
        self.__adds = []
        try:
            if (len(self.__addWeRecive)) > 0:
                for element in self.__addWeRecive:
                    if element in Adds[element].name:
                        self.__adds.append(Adds[element].value)
            else:
                self.__adds = [Adds.nothing.value]
        except:
            self.__adds = [Adds.nothing.value]
        return self.__adds

    def boilWater(self):
        water = HotWater(self.__water, self.__temp)
        hotwater = water.getHotWater()
        return hotwater

    def returnIngr(self):
        ingradients = Tea(self.boilWater(), self.getTypeTea(), self.getAddition())
        amount = ingradients.calculateAmount()
        return amount

    # def prepareTea(self):
    #
    #     print(s.calculateAmount())


# x = Tea_Machine(890, 400, "green_tea", ["honey"]).returnIngr()
# print("Sum", x)
