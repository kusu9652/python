#write a function to add integer values in array
def func():
    arr=[6,7,9]
    print("sum:",sum(arr))
func()
#average value of array of integers
def func():
    arr=[6,7,9]
    p=len(arr)
    print("avg:",(sum(arr)/p))
func()
# find index of an array element
arr=[1,8,9]
l=arr.index(8)
print("index:",l)
#test if array contains specific value
def func():
    arr=[1,6,4]
    if 6 in arr:
        print("yes",arr)
    else:
        print("no")
func()
#remove a specific element of copy of an array
def uf():
    arr=[1,3,6]
    arr.remove(3)
    print("removing:",arr)
uf()
#copy an array to another array
def func():
    arr=[]
    arr1=[1,7,3]
    arr2=arr1.copy()
    print("copy:",arr2)
func()
#to insert an element in specific position in array
def func():
    arr1=[1,3,5]
    arr1.insert(2,6)
    print("insert:",arr1)
func()
#min and max value of an array

def func():
    arr=[1,5,8]
    print("min:",min(arr))
func()

#max
def func():
    arr=[1,5,8]
    print("max:",max(arr))
func()


#reverse of an array of integer values
def func():
    arr=[1,5,8]
    k=arr[::-1]
    print("reverse:",k)
func()
#find duplicate values of an array
l=[1,7,7,2,6,6]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end="\n")

#common values in bw two array
arr = ['k','a','s','h','i']
arr1 = ['s','h','g']
print("Common values in given arrays:",set(arr).intersection(arr1))


#Initialize array
arr = [11,22,33,11,44,55]
finalarr = [] #empty array
#Using loop to remove duplicated elements
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)
#remove duplicate elements in array
from collections import OrderedDict
l=[1,3,5,5,6,7,7,9]
s=OrderedDict.fromkeys(l)
print(list(s))
#find second largest number in array
l=[7,1,9]
print("sort:",sorted(l)[-2])
#write a method even and oddd num in list
l=[2,4,3,5,7,6]
even=0
odd=0
for num in l:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("{0}even numbers and {1}odds.".format(even,odd))
# Write a function to get the difference of largest and smallest value.

#Initialize array
arr = [10,6,11,13,14]
arr.sort() #Sorting in ascending order
print("Diffrence of largest and smallest value:",arr[4]-arr[0])

# Write a method to verify if the array contains two specified elements(12,23).

#Initialize array
arr = [1,12,19,23,33,54]
#using loop to find if array contains specific elements
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")


i=4
fact=0
for i in range(1,18):
    fact=fact*i
    print("fact",fact)
