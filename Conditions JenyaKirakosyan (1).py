
"""#1. Write a Python program that accepts a word from the user and reverse it.

word = input("Enter string: ")
reversed = word[::-1]
print("Reversed version:", reversed)


#2. Write a Python program to count that user inputted number is even or odd.


num = int(input("Enter any number to test whether it is odd or even: "))

if (num % 2) == 0:
    print("The number is even")
else:
    print("The number is odd")



#3. Write a Python program to find is inputted number in 100 to 400 (both included). Hint(dont google task description)

num = int(input("Enter a number:"))
if (num >= 100) and (num <= 400):
    print(f"The number is between [100,400]: {num}")
    if (num % 2 == 0):
        print("The number is even")
    else:
        print("The number is odd")
else:
    print(f"The number is not in the given range[100,400]: {num}")


#4. Write a Python program that get 2 numbers from user and  retur Biggest, Median, Sum, Multiply, Divide and Subtract

numOne = int(input("Enter First Number : "))
numTwo = int(input("Enter Second Number : "))
if (numOne > numTwo):
    print(f"Biggest is : {numOne}")
else:
    print(f"Biggest is : {numTwo}")
result = (numOne + numTwo) / 2
print("Median is: ", result)
result = numOne + numTwo
print("Addition is : ", result)
result = numOne - numTwo
print("Subtraction is : ", result)
result = numOne * numTwo
print("Multiplication is : ", result)
if numTwo != 0:
    result = numOne / numTwo
    print("Division is : ", result)
else:
    print("Division by zero is not possible")

# 5. Write a Python program to get next day of a given date.
# Expected Output:
# Input a year: 2016
# Input a month[1 - 12]: 8
# Input a day[1 - 31]: 23
# The next date is [yyyy - mm - dd] 2016 - 8 - 24

year = int(input("Input a year: "))
if (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1 - 12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
elif month >= 13 and month == 0:
    print("There is no such month")
else:
    month_length = 30


day = int(input("Input a day [1 - 31] : "))

if day < month_length:
    day += 1
elif day > month_length:
    print("There is no such  date")
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))"""
