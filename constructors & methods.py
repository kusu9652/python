#write a program concept attribute of constructor
#apply all public,protected,private methods and default to constructor
class student:
    def __init__(self,age,name,salary):
        self.age=age  #public attribute
        self._name=name #protected attribute
        self.__salary=salary #private attribute
        
obj=student("18","kusu","35,000")
print(obj.age)        
#call the constructors(default and argument constructors) of super class from a child in python
class Employee:
    def __init__(self,age):
        self.age=age
    def uh(self):
        print("kusu")
k=Employee("9")
k.uh()
obj=Employee("17")
print(obj.age)
#write a class default constructor 1 argument constructor,2 argument constructor call all from main class

class Employee:
    
    def uh(self):
        print("vug")

    def __init__(self,age):
        self.age=age
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def uh(self):
        print("anti")
k=Employee("23","hima")
k.uh()
obj=Employee("17","hit")
print(obj.age)
s=Employee("78","suri")
print(s.age,s.name)
