from enum import IntEnum

from howtomaketea.api.tea.hotwater import HotWater

'''Class which returns HotWater, teatype and array of addictions'''


class Tea:
    hotWater = {}
    teatype = int(0)
    add = [0]
    list = []

    def __init__(self, hw, tt, add):
        self.hotWater = hw
        self.teatype = tt
        self.add = add

    def AskWhat(self):
        input("How much tea in g do you want?")
        print(self.teatype)
        input("How much adds do you want?")
        print(self.add)
        input("How much water do you want in ml?")
        print(self.hotWater)

    def calculateAmount(self):
        return self.teatype+self.add+self.hotWater

    def capacity(self):
        # print(11)
        # print(self.hotWater.getHotWater())
        return self.calculateAmount()


obj = Tea(12, 6, 3)
print(obj.capacity())

'''array with types of tea'''


class TypeTea(IntEnum):
    black_tea = 1
    green_tea = 2
    oolong_tea = 3
    white_tea = 4
    puerh_tea = 5
    earl_Grey = 6
    jasmine_tea = 7
    masala_tea = 8
    fruit_tea = 9
    flower_tea = 10
    leaf_tea = 11

    @property
    def __str__(self):
        return str(self.value)


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
    almound_milk = 9
    coconut_milk = 10
    ice_cream = 11
    sorbet = 12

    @property
    def __str__(self):
        return str(self.value)
