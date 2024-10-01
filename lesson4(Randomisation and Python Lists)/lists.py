states=['manchester','liverpool','newcastle']
print(f"the states are {states}")
print(states[0]) # first item
print(states[-1]) # last item

states[0]="Man United" # altering any item in the list
print(states)

# ADDING TO THE LIST
states.extend(["Chelsea", "Arsenal"])
print(states)
# REMOVE
states.remove("Man United")
print(states)