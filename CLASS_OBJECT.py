# PYTHON CLASS
# * python is a object-oriented programming language
# * class is a blueprint to create object
# * Small representation of class - object

# Creating a class named my class
class my_class:
    number = 90


# Creating a object
c1 = my_class()
print(f"c1.number: {c1.number}")


# Will understand the init function
# * constructor
# * init function is automatically called when a object of the class is created
# * Self parameter: self parameter is the reference to the current instance to the class
#   it is not compulsory to use the word self it can be anything.But it should be the
#   first parameter of any function in the class.
class my_class1:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # str function
    def __str__(self):
        return f"{self.name}-{self.age}"

    # Method inside the class
    def myfunction(self):
        print(f"My name: {self.name} and my age: {self.age}")


# Creating a object
obj = my_class1("Vaishnav", 21)
# calling the method using the object
obj.myfunction()
# Printing the object
print(f"obj name : {obj}")
