a = (1,2,3,6)
a = () #This is a empty tuple
a = (1,) #Tuple with only one element needs a comma
print(type(a)) #This will print the datatype of a
print(a) #This will print list of a

#Tuple method
a = (1,2,3,6,3,3,3)
no = a.count(3)
print(no)

a = (1,2,7,3,6,3,3,3)
i = a.index(3)
print(i)