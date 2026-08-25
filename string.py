str = "this is first string"
str2 = " this is second string"
str3 = str1 +  str2          # concates both the string
print(str3)                
print(len(str1))             # tells the length of the string
print(str1.endswith("ing"))  # tells whether it ends with 'ing' or not
print(str1.count("i")        # count total 'i' present in the string


# string slicing
str = "Amazing"
print(str[0:3])                  # prints from starting index 0 and ending index 3
print(str[:4])                   # prints from starting index 0 and ending index 4
print(str[3:])                   # prints from starting index 3 and till last index
print(str[-3:-1])                # prints from starting index -4 and ending index -1
print(str.replace("i","o"))      # replace the word "i" with "o" and prints the string
print(str.upper())               # capitalizes first word of the string   
print(str.lower())               # Output: "amazing"
print(str.startswith("Am"))      # Output is False
print(str.find("z")                           
