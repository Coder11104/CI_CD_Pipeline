def is_prime(n):
    # Handle cases for numbers less than 2
    if n <= 1:
        return False
    
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # n is divisible by i, so it's not a prime number
    
    return True  # n is prime if no divisors were found

# Input number
num = int(input("Enter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
