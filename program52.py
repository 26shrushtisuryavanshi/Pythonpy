#23. Write a program to find the sum of the digits of a number.
number = int(input("Enter a number: "))
sum_of_digits = 0
while number > 0:
    sum_of_digits += number % 10
    number //= 10
print(f"The sum of the digits is: {sum_of_digits}")