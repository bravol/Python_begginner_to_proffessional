piano_keys = ['a','b','c','d','e','f','g']

piano_tuple = ('do', 're', 'mi', 'fa', 'so', 'la', 'ti')

print(piano_keys[2:5])
print(piano_keys[2:]) # from 2 to last number
print(piano_keys[:5]) # from 1 to 5

print(piano_keys[2:5:2]) # slip the second one in range of 2:5

print(piano_keys[::2]) # I want every second item
print(piano_keys[::-1]) # I want start from the end back to the beginning

print(piano_tuple[2:5]) # it can also work with tuple