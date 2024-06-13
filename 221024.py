'''
values = [2,1,2,5,3,6,3,5,4,1,7,1]
values = list(set(values))
print('values = ', values)


numbers = (1,2,3,4,5,6,7,8,9,10,11,12)          # numbers = tuple(range(1, 13))
numbers[1::2]
print('numbers =', numbers[1::2])
'''

year = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892, 9783129]
year[6:]            # year[-3:] // 뒤에서 3개만 추출.
population[6:]
print('year =', year[6:])
print('population =', population[6:])
