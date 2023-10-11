# 1. Write a function to multiply all the numbers in a given list
def multiplyList(myList):

    result = 1
    for i in myList:
        result = result * i
    return result

list1 = [1, 2, 3,4]
print(multiplyList(list1))


# 2. Write a function that takes a list and returns a new list with unique elements of the first list
def get_unique_numbers(numbers):
    uniquelist = []

    for number in numbers:
        if number in uniquelist:
            continue
        else:
            uniquelist.append(number)
    return uniquelist
numbers = [20, 20, 30, 30, 40]
print(get_unique_numbers(numbers))

# 3. Write a function to print the even numbers from a given list.

def get_even_numbers(numbers):
    evennum = []
    for i in numbers:
        if i % 2 == 0:
            evennum.append(i)
    return evennum
print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))





#4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
      # Sample String : 'The quick Brow Fox'
      # Expected Output :
      # No. of Upper case characters : 3
      # No. of Lower case Characters : 12

def upper_lower(string):
  letters = {"UPPER_CASE": 0, "LOWER_CASE": 0}
  for char in string:
    if char.isupper():
      letters["UPPER_CASE"] += 1
    elif char.islower():
      letters["LOWER_CASE"] += 1
    else:
      pass
  print("Sample String : ", string)
  print("No. of Upper case characters : ", letters["UPPER_CASE"])
  print("No. of Lower case Characters : ", letters["LOWER_CASE"])


upper_lower('The quick Brown Fox')





# 5. Write a Python function that takes a number as a parameter and check the number is prime or not
#Option 1
def test_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, "is not prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not prime number")


(test_prime(456))

#Option 2
def check_prime(number):
    if number > 1:
        for i in range(2, number ):
            if number % i == 0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")

n = int(input("Enter the number: "))
check_prime(n)
