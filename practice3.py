#1.Write a python program to display a user entered name followed 
#by Good Afternoon using input() function.
#Ans
# name = input("Entered your name:")
# print(f"Good Afternoon, {name}")

#2.Write a program to fill in a letter template given below with 
#name and date.
#Letter'''
#   Dear<|Name|>
#   You are selected!
#   <|Date|>
#   '''
#Ans
# letter = '''Dear <|Name|>,
# You are selected!
# <|Date|>'''
# print(letter.replace("<|Name|>","Harry").replace("<|Date|>",
#                                                  "2 october"))

#3.Write a program to detect double space in a string.
#Ans
name = "I  am studing python to  get job on data analyst"
print(name.find("  "))

#4.Replace the double space from problem 3 with single spaces.
#Ans
name = "I  am studing python to  get job on data analyst"
print(name.replace("  "," "))

#Write a program to format the following letter using eacape 
#sequence characters.
#letter = "Dear Harry,this python course is nice. Thanks!"
#Ans
print("Dear Harry, \n\t this python course is nice. \n Thanks!")