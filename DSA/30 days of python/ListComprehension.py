import string

'''string to character list'''
# way1
str1 = 'Python'
lst1 = list(str1)
# print(lst1)
#  way 2
str = 'Learning'
lst = [i for i in str]  # this is list comprehension
# print(lst)


'''generating numbers'''
num = [i for i in range(11)]

sq = [i * i for i in range(11)]

'''list of tuples'''
tup = [(i, i * i * i) for i in range(11)]
# print(tup)

'''can be combined with if expression'''
even_numbers = [i for i in range(10) if (i & 1) == 0]
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
# filter +ve nos and even
pos = [i for i in numbers if i > 0 and i % 2 == 0]

'''flattening a 3d array very imp'''
td_array = [[1, 2, 3], [4, 5, 6], [3, 6, 7]]
flat_arr = [number for row in td_array for number in row]
# print(flat_arr)

'''LAMBDA FUNCTION VERY IMP'''
# it returns avalue
add = lambda a, b : a + b
# print(add(3,4))

square = lambda x: x*x
# print(square(5))

'''lambda in another function imp'''
def power(x):
    return lambda n : x ** n

two_ki_power_three = power(2)(3)#see how it is written
# print(two_ki_power_three)

four_ki_power_five = power(4)(5)
# print(four_ki_power_five)

'''problem 1'''
list_of_tuples = [(i,1,i,i*i,i*i*i,i*i*i*i,i*i*i*i*i) for i in range(11)]
# print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country[0].upper(),country[0][:3].upper(),country[1].upper()] for row in countries for country in row]
output2 = [{'country':country[0].upper()
            ,'city':country[1].upper()} for row in countries for country in row]
# print(output2)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output_names = [name[0]+' '+name[1] for row in names for name in row]
print(output_names)