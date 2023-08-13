#create an abstract class with abstract and non abstract methods
from abc import ABC,abstractmethod
class siri(ABC):
    def bill(self):
        print("youtube")
class srihan(siri):
    def bill(self):
        print("yes")
class mom(siri):
    def bill(self):
        print("yee")
class enemy(siri):
    def bill(self):
        print("enenmy of me")
class trust(siri):
    def bill(self):
        print("yes you are correct")
s=srihan()
s.bill()
l=mom()
l.bill()
p=enemy()
p.bill()
d=trust()
d.bill()
#reate an instance for the child class in child class and call abstract methods
from abc import ABC,abstractmethod
class siri(ABC):
    def interest(self):
        print("y")
class srihan(siri):
    def interest(self):
        print("joe")
class mom(siri):
    def interest(self):
        print("yahoo")
s=srihan()
s.interest()
l=mom()
l.interest()
#Create an instance for the child class in child class and call nonabstract methods
from abc import ABC,abstractmethod
class siri(ABC):
    def bill(self):
        print("y")
class srihan(siri):
    def interest(self):
        print("joe")
class pan(srihan):
    def interest(self):
        print("clg")
class mom:
    def no(self):
        print("yahoo")
s=srihan()
s.interest()
p=pan()
p.interest()
l=mom()
l.no()
#Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods

from abc import ABC,abstractmethod
class siri(ABC):
    def interest(self):
        print("y")
class srihan(siri):
    def interest(self):
        print("joe")
