# https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/

# python program to demonstrate inheritance

'''
Base or Super class. Note object in bracket.
Generally, object is made ancestor of all classes

in python 3.x "class Person" is equivalent to "class Person(object)"
'''

'''
class Person(object):
    
    # Constructor
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
        
    # To check if this person is employee
    def isEmployee(self):
        return False


      
# Inherited aka Sub Class (Note person in bracket)
class Employee(Person):
    
    # Here we return true
    def isEmployee(self):
        return True
'''

#################################

# Python example to check if a class is subclass of another
'''
class Base(object):
    pass # empty class
    
class Derived(Base):
    pass # empty class
    
'''



###############################

# Python example to show working of multiple inheritance
