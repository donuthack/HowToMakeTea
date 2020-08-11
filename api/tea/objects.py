import random


list = []
for i in range(random.randint(0, 100)):
    list.append({
    "teatype": random.randint(1, 11),
    "capacity": random.randint(250, 1000),
    "water": random.randint(100, 1000)
})
print(list)


'''sort water from biggest to smallest'''
def getValue(list):
    return list['water']


list.sort(key=getValue, reverse=True)
print(list)

# '''teatype, capacity, water, list => return True or False in bool look using sort, decrease increase'''
# def increaseDecrease(teatype, capacity, water, list):
#     list.sort(())
