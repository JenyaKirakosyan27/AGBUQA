#Exercise 1: Write a Python function called calculate_average that takes a list of numbers as input and returns the average (mean) of those numbers. Test your function with the following list: [10, 20, 30, 40, 50].

def Average(mylist):
    return sum (mylist) / len(mylist)

mylist = [10,20,30,40,50]
average = Average(mylist)
print("Average of the list = ", round(average))








#Exercise 2: Create a Python class called Rectangle with two attributes: width and height. Implement a method named calculate_area that calculates and returns

class Rectangle():
    def __init__(self, whidth, height):
        self.whidth = whidth
        self.height = height


    def area (self):
        return self.height * self.whidth
myrectangle = Rectangle(14,10)
print("Area of rectangle:", myrectangle.area())







