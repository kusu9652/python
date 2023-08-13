#write a program finally block
try:
    k=5/0
    print(k)
except ZeroDivisionError:
    print("cant divide")
finally:
    print("this is always executed")
#write a program arithmetic exception
    # to generate a arithmetic exception
try:
    k=5//0
    print(k)
except ArithmeticError:
    print("this is raising an error")
else:
    print("success")
#multiple blocks
try:
    a=7
    b=0
    d="hmkc"
    c=a+d
except ZeroDivisionError:
    print("this is raising an error")
except ArithmeticError:
    print("an error")
except TypeError:
    print("type error")
#create your own exception
try:
    print(x)
except NameError:
    print("var x is not deined")
else:
    print("something")
#io exception is.
def him():
    try:
     f=open("foo.txt",'r')
    except(IOError):
        print("noo")
him()
#program file not found exception

try:
    f=open("foo12.txt",'r')
    print(f)
except FileNotFoundError:
    print("noo such file")


#program class not found
class B():
    def n(self):
        print("nafo")
class c(B):
    def lkfio(self):
        print("fbfffff")
try:
    raise B()
except:
    print("not found class")

#
class a:
    def mh(self):
        print("ku")
k=a()
k.mh()
#
a = [1, 2, 3,4,5,6]
try:
    print ("reverse element = ",a[::-1])
 
    # Throws error since there are only 6 elements in array
    print (" first six element = ",a[:5])
    
except:
    print ("An error occurred")

print()

b = [6,5,4,3,2,1]
try:
    a == b
except:
    print("They are not equal")
else:
    print("Both Equal") 

print()


























































































































































































