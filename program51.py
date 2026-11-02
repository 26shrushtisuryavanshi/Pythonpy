#22. Write a program to count the digits in a number
number = int(input("Enter a number: "))
count = 0
while number > 0:
    number //= 10
    count += 1
print(f"The number of digits is: {count}")