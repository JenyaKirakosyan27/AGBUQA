# 1. Write a program to display all three-digit numbers.

for i in range(100, 1000):
    print(i, end=", ")

# 2. Write a program to display all odd three-digit numbers.


for i in range(100, 1000):
    if i % 2 != 0:
        print(i)

# 3. Write a program to display even five-digit numbers in one line.

for i in range(10000, 99999):
    if i % 2 == 0:
        print(i, end=", ")

# # 4. Write a program to display all numbers till 1000, which are divided both by 5 and 7.
number = int(input("Pleas input a number :"))
for i in range(0, number):
    if i % 5 == 0 and i % 7 == 0:
        print(i, )


# # 5. Write a program to display every third element of the list.
def evry_third_number(myList):
    result = []
    count = 3
    result.append(myList[0])
    while len(myList) > 0:

        if count > 0:
            myList.pop(0)
        else:
            result.append(myList[0])
            myList.pop(0)
            count = 3
        count -= 1
    return result


myList = [1, 12, 2, 23, 3, 4, 69, 5, 6, 456, 7, 8, 100, 9, 10, 45, 78, 52]
print(evry_third_number(myList))

# 6. Write a program to display only lowercase elements from the list. Note: list contains at least 15 - 20 elements.

myList = ["ARMENIA", "japan", "germany", "CanAda", "PinAustralia", "Brazil", "france", "Mexico", "italy", "China",
          "InDia", "Indonezia", "argentina", "Russia", "South afric", "united kingdom", "saudi arabia"]
resultList = []
for item in myList:
    if item[0].islower():
        resultList.append(item)
print(resultList)

