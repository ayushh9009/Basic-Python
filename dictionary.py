# dictionary methods

student = {
"name" : "ramesh ",
"subjects" : {
"phy" : 34,
"chem" : 45,
"math" : 66
}
}
print(list(student.keys()))                         # prints keys of dictionary
print(list(student.values()))                       # prints values  
print(student.update({"city" : "delhi"})            # added city in student
print(student.items())                              # prints key-value pair    
