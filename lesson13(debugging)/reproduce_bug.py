from random import randint
dice_images=["1","2","3","4","5","6"]
# dice_num = randint(1,6)  6 was out of range
dice_num = randint(0,6)
print(dice_images[dice_num])