# 1. Write a program to construct the following pattern.
#       *
#       * *
#       * * *
#       * * * *
#       * * * * *
#       * * * *
#       * * *
#       * *
#       *

# i = 0
# size = 5
# while i < size:
#     print("* " * i)
#     i += 1
# while i > 0:
#     print("* " * i)
#     i -=1
# symbol = "* "
# i = 1
# size = 5
# component = 1
#
# while i != 0:
#     if i == size:
#         component = -1
#     print(symbol * i)
#     i += component

# 2. Write a program to create the multiplication table (from 1 to 10) of a number.
# Input a number: 6
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 6
# i = 1
# tableNumber= int(input("Input a tablenumber: "))
# while i <= 10:
#     print(n, 'x', i, '=', tableNumber*i, end='')
#     i += 1
#     print()
#
#
#
# 3. Write a program to print alphabet pattern 'O'
#    Expected Output:
#          *
#        *   *
#        *   *
#        *   *
#        *   *
#        *   *
#          *
#
# print("  * ")
# i = 0
# while i < 5:
#     print("*   *")
#     i += 1
# print("  * ")

part = 3
while part < 3:
    if part != 2:
        print(" * ")
    else:
        i = 0
        while i < 5:
            print("*  *")
            i += 1
    part -= 1










# 4. Calculate the sum of all numbers from 1 to a given number from user

# number = int(input("Number: "))
# sum = 0
# i = 0
# while i <= number:
#     sum = sum + i
#     print(sum)
#     i = i + 1

# number = int(input("Number: "))
# result = 0
# print(f"Sum from 1 to {number} is :", end = "")
# while number > 0:
#     result += number
#     number -= 1
# print(result)

# 5. Write a program to check whether a specified list is sorted or not


# myList1 = [11, 23, 42, 51, 67]
# print("Given list : ", myList1)
# myList1_copy = myList1[:]
# myList1_copy.sort()
# if (myList1 == myList1_copy):
#     print("Yes, List is sorted.")
# else:
#     print("No, List is not sorted.")
