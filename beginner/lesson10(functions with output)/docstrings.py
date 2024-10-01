
# more than one return statement
def format_name_2(first_name, last_name):
    """Take the first and the last name to return the full name
    with title case version of the name"""

    if first_name == "" or last_name == "":
        return "You did not provide the names."
    formated_name = first_name.title() + " " + last_name.title()
    return f"formatted name is {formated_name}"

print(format_name_2("", ""))
