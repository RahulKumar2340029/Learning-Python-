import os
import random
import sys
from statistics import *
import math
import string

'''os for creating directory, changing, reading content, etc.'''
# os.mkdir('testos.py')
'''get current working directory'''
# print(os.getcwd())
'''remove working directory'''
# os.rmdir('testos.py')

'''testing sys'''
# print('Welcome {}, Enjoy {} challenge'.format(sys.argv[1], sys.argv[2]))
# print(sys.maxsize)
'''environment path'''
# print(sys.path)
'''version'''
# print(sys.version)

'''testing statistics mean median ...'''
ages = [55, 42, 54, 85, 65, 32, 12, 14, 15, 11]
# print(mean(ages))
# print(median(ages))
# print(mode(ages))
# print(math.frexp(20))

# print(dir(sys))
'''testing random'''
'''val between 0 - 0.9999'''
# print('{:.4f}'.format(random.random()))
'''random between a and b randint(a,b)'''
# print(random.randint(1, 5))

# level 1
# def random_user_id():
#     characters = string.ascii_letters + string.digits
#     user_id = ''.join(random.choice(characters) for _ in range(6))
#     return user_id
#
# print(random_user_id())
'''problem 2'''
# def user_id_gen_by_user():
#     length = int(input('Enter length: '))
#     count = int(input('Enter how many passcode u want? '))
#     characters = string.ascii_letters + string.digits
#     for _ in range(count):
#         user_id = ''.join(random.choice(characters) for _ in range(length))
#         print(user_id)
# user_id_gen_by_user()

'''problem 3'''


# def rgb_color_gen():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = 'rgb (%d, %d, %d)' % (r, g, b)
#     return rgb

'''LEVEL 2'''
# def list_of_hexa_colors():
#     characters = 'abcdef' + string.digits
#     hexa_color = '#'+''.join(random.choice(characters) for _ in range(6))
#     return hexa_color

'''problem 2'''
# def list_of_rgb_colors():
#     rgb_arr = []
#     for _ in range(random.randint(1,10)):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         rgb = 'rgb(%d,%d,%d)' % (r, g, b)
#         rgb_arr.append(rgb)
#     return rgb_arr
# print(list_of_rgb_colors())

'''problem 3'''

# def generate_colors(str,f1,f2):
#     if(str == 'hexa'):
#         return f1
#     else:
#         return f2
# print(generate_colors('rgb',list_of_hexa_colors(),list_of_rgb_colors()))

'''LEVEL 3'''
'''problem 1'''
'''this is where i stuck for a moment'''
# def shuffle_list(a: list)->list:
#     shuffled_list = a[:]
#     random.shuffle(shuffled_list)
#     return shuffled_list

# print(shuffle_list([1,2,3,'rahul',{'name':'rahul','age':'22'}]))

'''v imp problem 2'''

# def unique_7_nos():
#     unique_nos = random.sample(range(0,9),7)
#     return unique_nos

# print(unique_7_nos())