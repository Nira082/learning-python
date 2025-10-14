# Types of strings
a = 'Nira'
b = "Nira"
c = '''Nira'''
print(a)
print(b)
print(c)

#String slicing
name = "Harry"
nameshort = name[2:4]
print(nameshort)

#negative slicing
name = "Harry"
print(name[0:3]) #This is string slicing
print(name[-4:-1]) #This is negative slicing
print(name[1:4]) #This is the way to get string 
                   #slicing form negative slicing
print(name[:])                   

#Slicing with skip value
word = "idjekfoekfoefkeo"
print(word[1:9:2])

#String functions
name = "Harry"
print(len(name))
print(name.endswith("y"))
print(name.startswith("H"))
print(name.capitalize())