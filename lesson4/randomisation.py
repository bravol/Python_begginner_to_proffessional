import random
from lesson4.my_module import my_favorite_number

random_integer=random.randint(1 ,my_favorite_number)
print(random_integer)


# random float point numbers
random_number_0_to_1 = random.random() * 10 #include 0 but never include 1
print(random_number_0_to_1)
random_float=random.uniform(1,10)
print(random_float)

random_heads_or_tails= random.randint(0,1)
if random_heads_or_tails==0:
    print("Heads")
else:
    print("Tails")
