
# 1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
#     Create a function to display the entire attribute and their values in Student class.

class Student:


    def __init__(self, student_id, student_name):

        self.student_id = student_id
        self.student_name = student_name

    def add_class(self, student_class):

        self.student_class = student_class

    def display_attributes(self):

        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Class: {self.student_class}")


student = Student(1, "John Doe")

student.add_class("Mathematics")
student.display_attributes()




# 2. Create a Vehicle class without any variables and methods

class Vehicle:
    pass



# 3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

bmw = Vehicle(300, 15)
print("BMW's maximum speed is :", bmw.max_speed)
print("BMW's mileage is:", bmw.mileage)




# 4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


studentbus = Bus("Students Bus", 180, 12)
print("Vehicle Name:", studentbus.name, "Speed:", studentbus.max_speed, "Mileage:", studentbus.mileage)



# 5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self, capacity):

        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)

    def seating_capacity(self):
        return self.capacity

studentbus = Bus()
studentbus.seating_capacity()
print(f"The seating capacity of a  studentbus is {studentbus.seating_capacity()} passengers.")
