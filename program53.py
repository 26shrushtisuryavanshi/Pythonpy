#24. Write a program to reverse a number
number = int(input("Enter a number: "))
reversed_number = 0
while number > 0:
    reversed_number = reversed_number * 10 + number % 10
    number //= 10
print(f"The reversed number is: {reversed_number}")