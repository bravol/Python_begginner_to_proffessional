def format_name(first_name, last_name):
    formated_name = first_name.title() + " " + last_name.title()
    return f"formatted name is {formated_name}"

print(format_name("lumala", 'bRiaN'))

# more than one return statement
def format_name_2(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You did not provide the names."
    formated_name = first_name.title() + " " + last_name.title()
    return f"formatted name is {formated_name}"

print(format_name_2("", ""))
