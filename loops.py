d="Bright IT Carrer"
for ele in d:
    print(" ",ele)
#write a program to print 1 to 20 numbers using while loop
i=1
n=20
while i<=n:
    print(" ",i)
    i=i+1
#program to equal operator and not equal operator
s="mom"
l="mom"
d="dad"
if s==l:
    print("equal")
else:
    print("not")
#not equal
s="mom"
l="mom"
d="dad"
if s!=d:
    print("not equal")
else:
    print("equal")
#write a program to print even and odd numbers
n=2
if n%2==0:
    print("even:",n)
else:
    print("odd",n)
#odd
n=3
if n%2==0:
    print("even:",n)
else:
    print("odd",n)
#to print largest number among three
a=10
b=20
c=30
if a>b and a>c:
    print("a is largest",a)
elif b>c and a>c:
    print("b is largest",b)
else :
    print("c is largest",c)
#palindrome
s="mom"
k=s[::-1]
print(k)
if s==k:
    print("yes",k)
else:
    print("no")
#prime
n=12
if n>1:
    for i in range(2,n//2):
        if n%i==0:
            print("its not prime",n)
else:
    print("is a prime",n)
#d0 while

i=1
n=10
print("num",n)
n=n+1
if i<n:
 print("n",n)
 # Write a program to print even number between 10 and 20 using while.

a = 10
b = 20
print("Even Numbers Between 10 to 20: ",end=" ")
while a <= b:
    if(a % 2 == 0):
        print("{0}".format(a),end=" ")
    a = a + 1
print()

# Write a program to print 1 to 10 using the do-while loop statement.

a = 1
print("Print 1 to 10 using the do-while loop statement:",end=" ")
while True:
    print(a,end=" ")
    a = a + 1
    if(a > 10):
        break 
print()

# Write a program to find Armstrong number or not.

a = int(input('Enter a number to check if its armstrong or not: '))
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")



