"""# 1.Write a Python program that print list elements count.


colors = ["Green", "Red", "Blue", "White", "Yellow", "Brown", "Violet", "Red", "Yellow"]
print(colors)
print(type(colors))
print(colors.count("Yellow"))


# 2. Write a Python list use add, remove, elements use insert, append, pop, remove and extend methods.


people = ["Albus","Draco", "Harry", "Ronald"]
print(f"Peoples are: {people}")
people.remove("Draco")
print(f"People remove: {people}")
people.append("Neville")
print(f"People append: {people}")
people.insert(3,"Oliver")
print(f"People insert: {people}")
people.pop(2)
print(f"People pop:{people}")

people2 = ["Myrtle", "Petunia", "Lily", "Hermiona", "Ginny"]
people.extend(people2)
print(f"People extend: {people}")


# 3. Write a Python program to check if a list is empty or not

stationery = ["pen","pencil","glue","scissors"]

if len(stationery) == 0:
    print("The list is empty :")
    print(len(stationery))
else:
    print(f"The list is not empty: {stationery}")
    print(len(stationery))


# 4. Write a Python program to create a tuple with different data types.

myTuple = ("apple", True, 12.4, 56, "abc",False)
print(f"My tuple is:{myTuple}")
print(f" The type is :", type(myTuple))
print(f" The lenght is :", len(myTuple))


# 5. Write a Python program to create a tuple of numbers and print one item.

numbers = (1, 5, 6, 7, 45, 58, 68, 3, 455, 123)
print(numbers)
print(numbers[0])

# 6. Write a Python program to get the 4th element from the last element of a tuple.

countries = ("Armenia", "Belgium", "Cyprus", "France", "Greece", "Italy")
print("4th element from the : ", countries[3])
print("4th element from the last element : ", countries[-4]) """