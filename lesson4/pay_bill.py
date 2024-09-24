import random

friends=["Alice", "Bob","Charlie","David","Emmanuel"]

# 1 OPTION
print(random.choice(friends)) # pic at random

# 2 OPTION
random_index= random.randint(0,4)
print(friends[random_index])

# NESTED LISTS
fruit = ["strawberry", "mango"]
vegetables = ["Spinach","Tomatoes", "Potatoes"]
combined_list = fruit+vegetables
dirty_dozen = [fruit,vegetables] #nested list
print(dirty_dozen)
print(combined_list)