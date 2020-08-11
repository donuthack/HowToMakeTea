from enum import IntEnum

from .hotwater import HotWater

'''Class which returns HotWater, teatype and array of addictions'''


class Tea:
    hotWater = {}
    __teatype = int(0)
    __add = []

    def __init__(self, hw, tt, add):
        self.hotWater = hw
        self.__teatype = tt
        self.__add = add

    def AskWhat(self):
        print("How much tea in g do you want?")
        print(self.__teatype)
        print("How much adds do you want?")
        print(self.__add)
        print("How much water do you want in ml?")
        print(self.hotWater)

        hot_water = HotWater


    def calculateAmount(self):
        addsCap = len(self.__add) * 5
        search_key = 'water'
        if search_key in self.hotWater:
            return 5 + addsCap + self.hotWater['water']
        else:
            return "Its not enough temperature"

    # def capacity(self):
    # #     #     # print(11)
    # #     #     # print(self.hotWater.getHotWater())
    # #     #     # print(self.calculateAmount())
    #     return self.calculateAmount()

#
# obj = Tea(13, 1, [])
# print(obj.calculateAmount())


'''array with types of tea'''


class TypeTea(IntEnum):
    black_tea = 1
    green_tea = 2
    oolong_tea = 3
    white_tea = 4
    puerh_tea = 5
    earl_Grey = 6
    jasmine_tea = 7
    massala_tea = 8
    fruit_tea = 9
    flower_tea = 10
    leaf_tea = 11

    @property
    def __str__(self):
        return str(self.name)


'''check if value exist in array(True of False)'''
# enum_list = list(map(int, TypeTea))
# print(enum_list)

'''array with additions to tea'''


class Adds(IntEnum):
    nothing = 0
    citrus = 1
    berries = 2
    cinnamon = 3
    honey = 4
    lemon_herbs = 5
    mint = 6
    ginger = 7
    marple_syrup = 8
    almond_milk = 9
    coconut_milk = 10
    ice_cream = 11
    sorbet = 12

    @property
    def __str__(self):
        return str(self.name)
