from howtomaketea.api.tea.hotwater import HotWater

from enum import IntEnum


class Tea:
    HotWater = int(0)
    teatype = int(0)
    add = [0]

    def __init__(self, hw, tt, add):
        self.HotWater = hw
        self.teatype = tt
        self.add = add


    def getCapacity(self):
        return TypeTea(), Adds()


'''types of tea'''


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


print(int(TypeTea.white_tea))

# enum_list = list(map(int, TypeTea))
# print(enum_list)

'''additions to tea'''


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


print(int(Adds.lemon_herbs))


# t = TypeTea()
# a = Adds()
#
# obj = Tea()
