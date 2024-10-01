import random
from random import randint


# dice_images=["1","2","3","4","5","6"]
# # dice_num = randint(1,6)  6 was out of range
# dice_num = randint(0,6)
# print(dice_images[dice_num])
#
# year = int(input("What is your year of birth? "))
# if 1980 < year < 1994:
#      print("You are a millennial")
# elif year >= 1994:
#      print("You are a Gen Z.")

# DEBUGGERS
# https://pythontutor.com
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item  = (new_item + item)
        b_list.append(new_item)
    print(b_list)


mutate([1,2,3,5,8,13])

# TIPS FOR DEBUGGING
# take a break
# ask a friend
# ask stack overflow
