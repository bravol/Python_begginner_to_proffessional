def greet():
    print("Hello")
    print("How do you do!")

greet()

# A FUNCTION THAT ALLOWS INPUTS
def greet_with_name(name):
    print(f"Hello {name} ")
    print(f"How do you do {name}")

greet_with_name("Brian")

# FUNCTIONS WITH MORE THAN ONE INPUTS
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"How is {location} city")

greet_with("Brian Bravol","kampala")

# using not positional arguments, but let's use key word argument
greet_with(location="kampala", name="Brian Bravo")
