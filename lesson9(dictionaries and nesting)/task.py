program_dictionary = {
    "Bug":'This is an error in a program that prevents the program from running',
    "Function": "This is a peace of code that you can easily run over and over again",
    "Loop": "The action of doing something over and over again",
}
# retrieve an item from a dictionary
print(program_dictionary["Bug"]) #by its key

# add a piece of data
program_dictionary["Man"] = "This is a creature created by God from the beginning in Genesis and placed in garden of Eden"

# wipe an existing dictionary
# program_dictionary={}
# print(program_dictionary)

# edit an item in a dictionary
program_dictionary['Bug'] = "This is editing"
print(program_dictionary)

# looping through the dictionary
for thing  in program_dictionary:
    print(thing) # this gives you only the keys
    print(program_dictionary[thing])