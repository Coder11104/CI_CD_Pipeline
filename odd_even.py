def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input number
num = int(input("Enter a number: "))

# Check if the number is even or odd
result = check_even_odd(num)
print(f"The number {num} is {result}.")
