#write a program to read text file
#write a program to read a file stream
f=open('C:/Users/HP/Desktop/1.txt' , "r")
print(f.read())
#to read a file stream particular index using seek()
print(f.seek(20))
#write a program to write text to.txt file using input stream
f=open('C:/Users/HP/Desktop/1.txt' , "w")
print(f.write("kusuma"))
#read a file  stream support  random access
import linecache
print(linecache.getline('C:/Users/HP/Desktop/1.txt' ,7))
file3 = open("C:/Users/HP/Desktop/1.txt","r+")
print(file3.readline(11))
print()
