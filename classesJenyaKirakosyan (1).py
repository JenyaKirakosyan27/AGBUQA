


class Students:
  def __init__(self, id, name, age, gender, department):
    self.name = name
    self.age = age
    self.gender = gender
    self.department = department
    self.id = id





  def bio(self):
      print('''
  ID: {} 
  Name: {} 
  Age: {} 
  Gender: {} 
  Department: {}'''.format(self.id, self.name, self.age, self.gender, self.department))
  def speak(self):
        print("Speaking...")
        print("My name is ", self.get_personal_information(), "I am ", self.get_age(), "years old")




  def read(self):
        print("Reading...")
        print(self.get_personal_information(), "is reading  about Computer Science and Engineering.")



  def eat(self):
        print("Eating...")
        print(self.get_personal_information(), " were having lunch at a nearby restaurant during their break.")





  def get_personal_information(self):
        return self.name



  def learn(self):
        print("Learning...")
        print(self.get_gender(),  "representatives participated in the course.")
  def get_age(self):
      return self.age


  def get_gender(self):
      return self.gender

student1 =Students("001", "John Miller",21,"Male","Computer Science")
student2 =Students("002", "Emma Smith", 20, "Female", "Computer Science")
student1.name = "John"
student1.age = 23
student2.name = "Emma"
student1.gender = "Female"
student1.bio()
student2.bio()
student1.speak()
student2.read()
student1.eat()
student1.learn()



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species




class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("This animal makes a sound: Woof!")

class Cat(Animal):
    def __init__(self, name, bread):
        super().__init__(name, species="Cat")
        self.bread = bread

    def make_sound(self):
        print("This animal makes a sound: Meow!")

class Crocodile(Animal):
    def __init__(self, color, bread):
        super().__init__(color, species="Crocodile")
        self.bread = bread
        self.color = color

    def color(self):
        print("This animal colors is: Green!")

dog = Dog("Luna", "Siberian Husky")
cat = Cat("Tango", "Abyssinian")
crocodile = Crocodile("Green","Yacare Caiman")

print("Species is:", dog.species)
print("Name is:", dog.name)
print("Dogs bread is:", dog.breed)
dog.make_sound()


print("Species is:", cat.species)
print("Name is:", cat.name)
print("Cats bread is:", cat.bread)
cat.make_sound()



print("Species is:", crocodile.species)
print("Crocodile color is: ", crocodile.color)
print("Crocodile bread is:", crocodile.bread)





class Sides():
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


class Triangle(Sides):
    def area(self):
        s = (self.side1 + self.side2 + self.side3) * 0.5
        return float((s * (s - self.side1) * (s - self.side2) * (s - self.side3))) ** 0.5



    def perimeters(self):
        p = (self.side1 + self.side2 + self.side3)
        return float(p)

side1, side2, side3 = float(input("Side1 = ")), float(input("Side2 = ")), float(input("Side3 = "))
t = Triangle(side1, side2, side3)
print('Area of triangle is :', t.area())
print("Perimeter of triangle is:", t.perimeters())
"""

class Pythagoreastheorem():
    def __init__(self, altitude, base):
        self.altitude = altitude
        self.base = base

    def hypotenuse(self):
        hypotenuse = (base **2 + altitude **2)/
        return (hypotenuse)

altitude = float(input("Altitud = "))
base = float(input("Base = "))
hipotenus = Pythagoreastheorem(altitude, base)

print("Hypotenus of the right triangle is:", hipotenus.hypotenuse())

"""

