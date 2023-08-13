#create a dictionary atleast 5 key value pairs of student id and name
#adding values
dict={"id":"121","name":"kusuma","age":"17","college":"mic","class":"cse A"}
print(dict)
#updating values
dict.update({"age":"18"})
print("update key",dict)
#accessing values
print(dict.keys())
print(dict.values())
#nested loops
dict={1:{"id":"121","name":"kusuma","age":"17","college":"mic","class":"cse A"},
2:{"id":"122","name":"siri","age":"19","college":"mic","class":"cse A"}}
#access values of nested loop
print(dict.values())
#print keys
print(dict.keys())
print(dict)
#access values of nested loop
print(dict.values())
#del a value from dictionary
del dict[1]["id"]
print(dict[1])
    
