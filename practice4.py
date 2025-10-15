#Wrtie a program to store seven Marks in a list 
#entered by the user.
#Ans
# a = ["Apple","Orange","Grapes","Banana","Mango","Blackberry",
#      "Leichi"]
Marks = []
f1 = input("Enter Marks here:")
Marks.append(f1)
f2 = input("Enter Marks here:")
Marks.append(f2)
f3 = input("Enter Marks here:")
Marks.append(f3)
f4 = input("Enter Marks here:")
Marks.append(f4)
f5 = input("Enter Marks here:")
Marks.append(f5)
f6 = input("Enter Marks here:")
Marks.append(f6)
f7 = input("Enter Marks here:")
Marks.append(f7)
print(Marks)

#Write a program to accept marks of 6 students and display them
#in a sorted manner.
#Ans
marks = []
m1 = int(input("Enter Marks here:"))
marks.append(m1)
m2 = int(input("Enter Marks here:"))
marks.append(m2)
m3 = int(input("Enter Marks here:"))
marks.append(m3)
m4 = int(input("Enter Marks here:"))
marks.append(m4)
m5 = int(input("Enter Marks here:"))
marks.append(m5)
m6 = int(input("Enter Marks here:"))
marks.append(m6)
marks.sort()
print(marks)

#Check that a tuple cannot be changed in python. 
#Ans
a = (2,3,6,8,"nira")
a[3] = "odek"

#Write a program to sum a list with 4 numbers.
#Ans
l = [3,3,5,1]
print(sum(l))

#Write a program to count the number of Zeros in the following tuple: 
# a = (7,0,8,0,0,9)
#Ans
a = (7,0,8,0,0,9)
n = a.count(0)
print(n)