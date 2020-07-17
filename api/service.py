class To_Do_Tea:

    type_of_tea = str('')
    amount_of_water = int(0)
    temperature = int(0)
    amount_of_sugar = int(0)
    boiling_temp = int(80)
    errors = []

    '''parametrized constructor'''

    '''to check if my list contains False'''


    def __init__(self, type, water, temp, sugar):
        self.type_of_tea = type
        self.amount_of_water = water
        self.temperature = temp
        self.amount_of_sugar = sugar

    def teainfo(self):
        print("You want " + self.type_of_tea + "  tea")
        print("For that you need " + self.amount_of_water + ", ")
        print("Your tea`s temperature must be " + self.temperature + ", ")
        print("You like to add " + self.amount_of_sugar + " spoons of sugar.")


    '''conditions for types of tea'''

    def isTeaType(self, type):
        if type != "":
            obj = {
                'error': False,
                'message': "You made yours first step"
            }
            return obj
        else:
            obj = {
                'error': True,
                'message': "Choose some sort of tea"
            }
            return obj


    def isTemperature(self, temp):
        if int(temp) >= self.boiling_temp:
            obj = {
                'error': False,
                'message': "You made yours second step"
            }
            return obj
        else:
            obj = {
                'error': True,
                'message': "This temperature isn`t enough for preparing"
            }
            return obj


    '''conditions for amount of sugar and water'''

    # per = (wat * float((25 / 100)))
    def isWaterSugar(self, sugar, water):
        percentage = float((float(water) * 0.25))
        if float(sugar) > percentage:
            obj = {
                'error': True,
                'message': "Too much sugar for this amount of water",
            }
            return obj
        else:
            obj = {
                'error': False,
                'message': "You made yours third step",
            }
            return obj



    '''Created 2 lists for errors and summary valuables which are inputed'''
    '''if our valuable has Error => put it in errors list'''

    def check(self):
        list = []
        errors = []
        list.append(self.isTeaType(self.type_of_tea))
        list.append(self.isTemperature(self.temperature))
        list.append(self.isWaterSugar(self.amount_of_sugar, self.amount_of_water))
        #print(list)
        for numb in list:
            # print(numb['error'] == True)
             if numb['error'] == True:
                 errors.append(numb)
        return errors



    '''check if check func return True or False.'''
    '''If True => return True and print'''
    def conclusion(self):
        isErrors = self.check()
        print("Errors", len(isErrors))
        if len(isErrors) == 0:
            res = {
                'message': "Your order: you want {0} tea For that you want {1} ml of water. Also, your waters temperature must be {2} degreeses. Beside that you would like to add {3}.".format(self.type_of_tea, self.amount_of_water, self.temperature, self.amount_of_sugar) + "to yours tea."
            }
        else:
            res = {
                'message': isErrors,
            }
        return res


obj = To_Do_Tea("red", "10", "90", "11")
#

#obj = To_Do_Tea(input("What type of tea do you want?"), input("What amount of water for tea do you like to?"), input("What water temperature must be yours tea?"), input("How much spoons of sugar woul you like to?"))

'''calling func'''

#y = obj.conclusion()
#print(y)
x = obj.check()
print(x)
