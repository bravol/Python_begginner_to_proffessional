print('Welcome to the rollercoaster')
height=int(input("What is your height in cm? "))
# comparison operators == >= <= !=
if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input('What is your age? '))
    bill=0
    # nested if
    if age <= 12:
        bill+=5
        print(f"Child ticket ${bill}.")
    elif age <= 18:
        bill+=7
        print(f"teen ticket ${bill}.")
    elif age >= 45 and age <= 55:
        bill+=0
        print("Every thing is okay: Have a free ride")
    else:
        bill+=12
        print(f"Adult ticket ${bill}.")
    want_photo=input("Do you want to have a photo take?, Type y for yes or n for No: ")
    if want_photo=="y":
        # add three dollar to the bill
        bill+=3
        print(f"Your final bill is ${bill}")
else:
    print("You have to grow taller to ride the rollercoaster")