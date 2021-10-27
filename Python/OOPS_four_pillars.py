# Python Demonstration of four pillars of Object-Oriented Programming
"""Four Pillars of Object-Oriented Programming system(OOPS) are
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
"""
# Object-Oreinted Programming in Python

## Encapsulation: To enclose something in or as if in a capsule
# Encapsulation is the process of wrapping up variables and methods into a single entity
# Here, the variables "name", "reg_no", "branch" && the method "intro" is bundled into a single unit (i.e., "Fresher" class)

# Creating a class named 'Fresher'
class Fresher:
    # Constructor
    def __init__(self):
        self.name = "Sonakshi"
        self.reg_no = "BL.EN.U4XXXXXXXX"
        self.branch = "Computer Science Engineering"

    # An "intro" method
    def intro(self):
        print(
            "Hello All!\nI'm {} from {}. My registration number is {}".format(
                self.name, self.branch, self.reg_no
            )
        )


# Initialising an object for Fresher class
new_student = Fresher()
new_student.intro()

# Change the branch and name
new_student.name = "Shilpa"
new_student.branch = "Mechanical Engineering"
new_student.intro()

# OUTPUT:
""" 
Hello All!
I'm Sonakshi from Computer Science Engineering. My registration number is BL.EN.U4XXXXXXXX
Hello All!
I'm Shilpa from Mechanical Engineering. My registration number is BL.EN.U4XXXXXXXX
"""

## Inheritance: To receive a quality, characteristic, etc., from your parents or family
# Inheritance allows us to define a class that inherits methods and properties from another class.
# Creating the "Parent" and "Child" classes, where "Child" class inherits "Parent" class methods and variables.

# Creating a base class - "Parent" class
class Parent:
    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    def display(self):
        print("Hello! I'm from Parent class")
        print("My name: ", new_parent.getName(), "\n")


# Sub class inheriting "Parent" class
class Child(Parent):

    # Constructor
    def __init__(self, name, age):
        # reusing "Parent" class initialisation function
        Parent.__init__(self, name)
        self.age = age

    # To get age
    def getAge(self):
        return self.age

    # Overwriting Parent class method "display"
    def display(self):
        print("Hello! I'm from Child class")
        print(
            "My name: ", new_child.getName(), "\nMy age: ", new_child.getAge()
        )  # can access getName() method from "Parent" class throught inheritence


# Creating an object for the Parent class
new_parent = Parent("Sahi")
new_parent.display()  # cannot access age as the initialisation of "Parent" class expects only one parameter "name"

# Creating an object for "Child" class
new_child = Child("Bahu", "23")
new_child.display()

# Output:
"""
Hello! I'm from Parent class
My name:  Sahi 
Hello! I'm from Child class
My name:  Bahu 
My age:  23
"""

## Abstraction: Hiding irrelevant data and showing only necessary details.
# Abstraction hides the internal implementations of a process or method from the user
# let's assume we are importing "ABC" class (an Abstract class) from "abc" package,
# then through abstraction, we hides all details (i.e., all data members in "ABC" class) and make visible only available details (here, it's "sides" method in "Polygon" class)

# Abstract class
from abc import ABC

# "Polygon" class inheriting abstract class "ABC"
class Polygon(ABC):
    # abstract method
    def sides(self):
        pass


class Triangle(Polygon):  # inherting "Polygon" class
    def sides(self):
        print("Hi! I'm Triangle. I has 3 sides")


class Pentagon(Polygon):  # inherting "Polygon" class
    def sides(self):
        print("Hi! I'm Pentagon. I has 5 sides")


class Hexagon(Polygon):  # inherting "Polygon" class
    def sides(self):
        print("Hi! I'm Hexagon. I has 6 sides")


# Creating objects for the inherited classes
# Triangle() class and invoking "sides" method
t = Triangle()
t.sides()
# Pentagon() class and invoking "sides" method
p = Pentagon()
p.sides()
# Hexagon() class and invoking "sides" method
h = Hexagon()
h.sides()

# Output:
"""
Hi! I'm Triangle. I has 3 sides
Hi! I'm Pentagon. I has 5 sides
Hi! I'm Hexagon. I has 6 sides
"""

## Polymorphism: The condition of occurrence in several different forms (or) Polymorphism refers to the use of a single method/operator to represent different types in different scenarios.
"""
Python can use multiple classes in the same way, through polymorphism.
To serve this purpose, we can create a loop that iterates through a tuple of objects.
This will allow us to call methods without looking at the class to which the object points.
"""
# Creating a "Sample" class
class Sample:
    def function(self):
        print("This function is invoked from 'Sample' class.")


# Creating a "Random" class
class Random:
    def function(self):
        print("This function is invoked from 'Random' class.")


# Creating objects for the classes "Sample" and "Random"
obj1 = Sample()
obj2 = Random()
for method in (obj1, obj2):  # creating a loop to iterate through the obj1, obj2
    method.function()

# Output:
"""
This function is invoked from 'Sample' class.
This function is invoked from 'Random' class.
"""
