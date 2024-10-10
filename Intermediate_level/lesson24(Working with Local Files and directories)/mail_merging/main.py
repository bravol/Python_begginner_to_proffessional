PLACE_HOLDER = "[name]"

with open("./input/names/names.txt") as names_file:
    names = names_file.readlines() # make them to be in list
    print(names)

# writing letters to many people
with open("./input/letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACE_HOLDER,stripped_name)
        with open(f"./output/ready_to_send/letter_for_{stripped_name}.docx", mode='w') as completed_letter:
            completed_letter.write(new_letter)

