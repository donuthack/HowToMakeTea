from howtomaketea.api.tea.hotwater import HotWater
from howtomaketea.api.tea.Tea import *
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
                return self.__typeoftea
        except:
            self.__typeoftea = TypeTea.black_tea.name
            return self.__typeoftea

    def getAddition(self):
        try:
            if (len(self.__addWeRecive)) > 0:
                for element in self.__addWeRecive:
                    if element in Adds[element].name:
                        self.__adds.append(element)
            else:
                self.__adds = [Adds.nothing]
        except:
            self.__adds = [Adds.nothing]
        return self.__adds

    def boilWater(self):
        water = HotWater(self.__water, self.__temp)
        water.setHotWater()
        return water

    def prepareTea(self):
        s = Tea(self.boilWater(), 'white_tea', [])
        print(s.capacity())


# Tea_Machine(524, 100, "white_tea", ["honey"]).prepareTea()
