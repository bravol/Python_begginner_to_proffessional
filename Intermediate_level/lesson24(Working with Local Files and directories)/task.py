# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)



with open("my_file.txt", mode = 'a') as file:
    file.write("\nNew text 2.")

# if no file, it is created automatically
with open("new_file.txt", mode = 'w') as file:
    file.write("New text 2.")
