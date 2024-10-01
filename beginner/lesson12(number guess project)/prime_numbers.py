prime_numbers = []  # List to store prime numbers
number = int(input("Please enter the number range from 1 to..: "))

def is_prime(n):
    if n <= 1:  # Numbers less than 2 are not prime
        return False
    if n == 2:  # 2 is a prime number
        prime_numbers.append(n)
        return True
    for num in range(2, int(n ** 0.5) + 1):  # Check divisibility up to the square root of the number
        if n % num == 0:
            return False
    prime_numbers.append(n)  # Append prime number to the list
    return True

# Check for prime numbers from 1 to the input number
for i in range(1, number + 1):
    is_prime(i)

print(f"The prime numbers between 1 and {number} are {prime_numbers}")  # Output the list of prime numbers

