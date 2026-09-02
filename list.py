marks = [23,34,34,35,39,55,67]
print(marks)                  # prints the list
print(type(marks))            # tells type of data type       
print(len(marks))             # tells length of the list 
print(marks[3])
marks[2]="45"                 # adding it to the list as list are mutable 
print(marks)
print(marks[1:3])             # list is mutable
print(marks[1:])              # prints list from first index 


list = [2,4,5,6,7]
print(list)
list.append(10)                # adds 10 to end of list
print(list)
list.reverse()                 # reverse the list in reverse 
print(list)  
list.remove(2)                # removes 2 from the list
print(list)   
list.insert(3,8)              # inserts 8 at index 3
print(list)
list.pop(2)                   # removes element at index 2
print(list)
list.sort()                   # sort the list
print(list)
list.extend([3,8])            # adds the elements at the end of list
print(list)
list.clear()                  # clears the list 
print(list)
