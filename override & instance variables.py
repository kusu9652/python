#1.A,B and C are classes
A is a super class B is a sub class of A. C is a sub class of B

class A():
    def uff(self):
        print("hi")
class B(A):
    def uff1(self):
        print("ha")
class C(B):
    def uff2(self):
        print("hm")
k=A()
k.uff()
#create 3 methods in each class,2methods are specific to each class and third method (override)should be in all three classes A,B C
class A():
    def show(self):
        print("inside parent1")
    def uff1(self):
        print("ha")
    def uff2(self):
        print("hm")


class B(A):
    def display(self):
       print("inside parent2")
    def display2(self):
        print("inside")

class C(B):
    def display(self):
        print("you")
    def rehook2(self):
        print("we")

d=C()
d.display()
d.show()
#  call an overide method with super class reference B and C class objects
class kusu():
    def jerk(self):
        print("challey")
class kusu1(kusu):
    def jerk2(self):
        print("abbo")
class kusu2(kusu1,kusu):
    def jerk3(self):
        print("ammadu")
k=kusu2()
k.jerk3()
k.jerk()
        
#kj
class Bird:
    def intro(self):
        print("theewe")
    def flight(self):
        print("most of birds")
class sparrow(Bird):
    def flight(self):
        print("spam")
class parrot(Bird):
    def flight(self):
        print("high")
o=Bird()
o.intro()
o.flight()
o.intro()
d=sparrow()
d.flight()
l=Bird()
l.intro()
j=parrot()
j.flight()
#runtime polymorphism with data members/instance variables.repeat the above process only for data members
class cat:
    def __init__(self,name,age):
        self.name=name#instance variable
        self.age=age
        print("name",name)
    def ji(self):
        print("goo")
    def boo(self):
        print("hu")
class monkey(cat):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def loo(self):
         print("p")
k=cat("jick","10")
k.ji()
p=monkey("jack","18")
p.boo()
#super class reference to B and C
class A():
    def show(self):
        print("inside")
class B(A):
    def show(self):
        print("king")
class C(B):
    def show(self):
        super().show()
        print("QUEEN")
class D(C):
    def show(self):
        super().show()
        
o=D()
o.show()
      
    
