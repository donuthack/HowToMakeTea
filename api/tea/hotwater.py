class HotWater:
    water = int(0)
    temp = int(0)
    boiling_temp = int(100)
    result = ()

    # res = ()

    def __init__(self, water, temp):
        self.water = water
        self.temp = temp

    def setHotWater(self):
        percentage = float((float(self.water) * 0.95))
        if self.temp >= self.boiling_temp:
            self.result = {
                'error': False,
                'message': 'Continue to prepare',
                'water': percentage
            }
            return self.result
        else:
            self.result = {
                'error': True,
                'message': 'Your water must be under 100 degreese',
                'water': percentage
            }
            return self.result

    def getHotWater(self):
        if len(self.result) == 0:
            return {
                "error": True,
                "message": "You must boil yours water"
            }
        else:
            return self.result


# obj = HotWater(135, 989)
#
# print(obj.setHotWater())
