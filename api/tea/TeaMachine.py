from .hotwater import HotWater
from .Tea import Tea, Adds, TypeTea
from api.models import Add
from enum import IntEnum
import psycopg2


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
                return TypeTea[self.__typeoftea].name
        except:
            self.__typeoftea = TypeTea['black_tea'].name
            return self.__typeoftea

    def getAddition(self): #TODO Треба браті з табліци Add і шукати відповідності по ID якщо є то добавляті name до масіву __adds
        self.__adds = []
        print(Add.objects.all())
        try:
            if (len(self.__addWeRecive)) > 0:
                for element in self.__addWeRecive:
                    # if element in tea.
                        self.__adds.append(Add.pk)
            else:
                self.__adds = [Adds.nothing.name]
        except:
            self.__adds = [Adds.nothing.name]
        return self.__adds

    def boilWater(self):
        water = HotWater(self.__water, self.__temp)
        hotwater = water.getHotWater()
        return hotwater

    @property
    def returnIngr(self):
        ingradients = Tea(self.boilWater(), self.getTypeTea(), self.getAddition())
        additions = self.getAddition()
        amount = ingradients.calculateAmount()
        string = ' '
        if len(additions) > 1:
            for element in additions:
                if element == additions[-1]:
                    if len(additions) >= 3:
                        string += "and " + element
                    else:
                        string += ", " + element
                else:
                    if element == additions[-2]:
                        string += element + ' '
                    else:
                        string += element + ', '
        else:
            string = self.__adds[0] + " "
        if amount != 0:
            res =  "You want: {0} type, addition you choose: {1}. So, yours amount of tea is {2}".format(self.getTypeTea(), string,  amount)
        return res


# x = Tea_Machine(890, 400, "green_tea", ["honey"]).returnIngr()
# print("Sum", x)
