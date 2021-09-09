
# A simple example for class
class Test:
    
    # Sample method
    def fun(self):
        print("Hello")
        
# Driver code

# sample class with init method
class Person:
    
    # init method or constructor
    def __init__(self, name):
        self.name = name
    
    # Sample method
    def say_hi(self):
        print("Hello, my name is", self.name)
        
###################################
##

'''
Python program to show that the variables with a value assigned in
class declaration, are c;ass variables and variables inside methods and 
constructors are instance variable
'''
'''
# Class for CSS student
class CSStudent:
    
    # Class variable
    stream = "cse"
    
    # The init method or constructor
    def __init__(self,roll):
        
        # instance variable
        self.roll= roll
           
'''


#Python program to show that we can create instance variables inside methods

'''
# Class for CS Student
class CSStudent:
    
    # Class Variable
    stream = "cse"
    
    # The init method or constructor
    def __init__(self, roll):
        
        # instance variable
        self.roll= roll
        
    # Adds an instance variable
    def setAddress(self, address):
        self.address = address
        
    # Retrieves instance variable
    def getAddress(self):
        return self.address

'''

# Class for CS Student
class CSStudent:
    
    # Class Variable
    stream = "cse"
    
    # The init method or constructor
    def __init__(self, roll,address):
        
        # instance variable without using set and get
        self.roll= roll
        self.address= address
        
    
a=CSStudent(100, "uganda")
########################


class Test:
    pass