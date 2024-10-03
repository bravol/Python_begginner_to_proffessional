# Pyramid height
height = int(input("Enter the height of the pyramid: "))

# Loop to print each row
for i in range(1, height + 1):
    # Print spaces for left alignment
    print(' ' * (height - i), end='')
    # Print stars in each row
    print('*' * (2 * i - 1))
