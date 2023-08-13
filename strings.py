#different ways of create a string
k="kusuma"
print(k)
#concatenate strings using +operator
k="sridevi"
s="kusuma"
c=k+s
print(c)
#finding length of a string
a="keka"
d=len(a)
print(d)
# Extract a string using Substring.

# Searching in strings using index()
str3 = 'kashish'
str1 = 'ish'
str2 = 'h'
print("Position of ish:",str3.index(str1))
print("Position of h:",str3.index(str2))
print()

# Matching a String Against a Regular Expression With matches().
from ast import Str
import re
Substr = 'Madara'
str6 = 'Madara once said- Wake up to relity nothing goes as planned in this cursed world'
print(re.match(Substr,str6))
print()

#compare to,comparing strings
k="sri"
h="srii"
if k==h:
    print("yes")
else:
    print("not")
#starts with
k="sir"
s=k.startswith("s")
print(s)
#ends with
k="sir"
s=k.endswith("r")
print(s)
#searching in strings using index()
k="10kutty20"
print(k.index('kutty'))
#convert inter object to string
s=100
d=str(s)
print(s)
#searching in strings using index
k="10kutty20"
print(k.index('t'))
#replacing character in string using replace
k="10kutty20"
print(k.replace('kutty','chintu'))
#splitting strings with split
k="10kutty20"
print(k.split())

#converting to upper case and lower case
k="daniel"
print(k.upper())
print(k.lower())
#extracting a string using substring
k="10kutty20"
print(k[3:5])
#trimmming strings with strip()
a="kusuma  " 
print(a.rstrip())

#
a="kusu"
k=a[::-1]
print(k)




