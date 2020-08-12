import random

list = []
for i in range(random.randint(0, 50)):
    list.append({
        "teatype": random.randint(1, 11),
        "capacity": random.randint(0, 49),
        "water": random.randint(0, 50)
    })
print(12, list)

'''sort water from biggest to smallest'''


def bubbleSortWater(list):
    for index, element in enumerate(list):
        for index2, compare_element in enumerate(list):
            if list[index]['water'] < list[index2]['water']:
                list[index], list[index2] = list[index2], list[index]
    return list


print(5, bubbleSortWater(list))

'''bubble sort'''


def BubbleSort(array):
    for ind2, i in enumerate(array):
        for ind, j in enumerate(array):
            if len(array) - 1 == ind:
                break
            if array[ind2] < array[ind]:
                array[ind2], array[ind] = array[ind], array[ind2]
    return array


array = []
for i in range(random.randint(0, 20)):
    array.append(random.randint(0, 20))
print(array)

print(BubbleSort(array))

'''filter teatype: '''
'''input: number => output: all keys with that value'''

#
# def FilterTeaType(list):
a = filter(lambda element: element['teatype'] == 2, list)
print(123, a)

# o = int(input("What element do you want to return?: "))
# print(1, FilterTeaType(list))
