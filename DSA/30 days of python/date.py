from datetime import datetime, date

now = datetime.now()
# print(now)
month = now.month
# print(month)
timestamp = now.timestamp()
# print(timestamp)

'''difference bw two points in time'''
today = date(year=2024,month=7,day=1)
birth_Date = date(year=2001,month=1,day=3)
age = today - birth_Date

'''Exception handling'''

# try:
#     print(10 + '5')
# except Exception as e:
#     print('something went wrong',e)

# try:
#     name = input("Enter name ")
#     birth_year = input("Enter your birth year ")
#     age = 2024 - birth_year
#     print('you are {} and your age is {}'.format(name,age))
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('Zero division error')
# finally:
#     exit(5)

'''PACKING AND UNPACKING'''
''' * FOR TUPLES AND ** FOR DICT'''
lst = [1,5,9,6,3,7]
# unpacking# print(*lst)
def sum_of_nums(a,b,c,d,e,f):
    return a+b+c+d+e
# error below
# print(sum_of_nums(lst))
# print(sum_of_nums(*lst))

'''can also unpack in range(A,D) A B C D'''
normal = range(1,30)
# print(*normal)
# below also unpack in list
# print(list(normal))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, swe, nor ,*rest = countries
# print(fin,swe,nor,rest)

'''unpacking dict very imp'''
def person_info(name,age,city):
    return f'{name} lives in {city} and his age is {age}'

dic = {'name': 'Rahul','city':'Warsaw','age':'22'}
# print(person_info(**dic))
'''packing concept *args for list and **kwargs for dict'''
def sum_all(*args):
    total = 0
    for item in args:
        total+=item
    return total
# print(sum_all(1,2,3,4,4))
# print(sum_all(44,55,6))

'''spreading in python'''
list1 = [1,2,3]
list2 = ['a','b','c']
# list3 = [0,*list1,*list2]
# print(list3)

# for index,item in enumerate(countries):
    # if item == 'Finland':
        # print(f'{item} found in countries at index {index}')

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion']
fruits_and_veg = []
for f, v in zip(fruits, vegetables):
    fruits_and_veg.append({f'fruit:{f}, veg:{v}'})
# print(fruits_and_veg)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, e, r = names
# print({'nordic_countries':nordic_countries},{'e':e},{'r':r})

'''File Handling'''

# f = open('./files.txt','x')
# f = open('./files.txt')
# txt = f.read(10)
# txt3= f.readline()
# txt2 = f.readlines()
# print(txt2)
# print(txt)
# f.close()

'''writing'''
# with open('./files.txt','a') as f:
#     f.write('This is the end of file appended')
#
# f = open('./files.txt')
# txt = f.readlines()
# print(txt)
# f.close()

'''deleting file'''
# import os
# # os.remove('./files.txt')
# '''what if file not exist and you wnat to remove so better to write like this'''
# if os.path.exists('./files.txt'):
#     os.remove('./files.txt')
# else:
#     print('File not exists')

import json
person_json = '''{
    "name":"rahul",
    "age":"25",
    "education":"masters",
    "profession":"sde"
}'''

person_dict = json.loads(person_json)
print(type(person_dict))
# print(person_dict)
'''dict to json'''

person_json2 = json.dumps(person_dict,indent=4)
print(type(person_json2))
#  JSON does not have type, it is a string type.
'''saving a json file'''

with open('./json_example.json','w',encoding='utf-8') as f:
    json.dump(person_json2,f,ensure_ascii=False,indent=4)

