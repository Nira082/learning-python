# QUESTION Write a program to print twinkle little start poem in python

# print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
# like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
# When the blazing sun is set, and the grass with dew is wet. Then you show your little
# light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
# are.
# Then the traveler in the dark thanks you for your tiny spark. How could he see where to
# go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
# As your bright and tiny spark lights the traveler in the dark, though I know not what you
# are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''')

#QUESTION install an external module and use it to perform an opertaion of your interest

# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("My name is nira khanal i am learing python to get my data analyst job")
# engine.runAndWait()

# QUESTION Write a python program to print the contents of a directory using the OS module. 
# search online for the function which does that.

import os
# specify the directory you want to list
directory_path = '/Windows'
# list all files and directories in the specified path
contents = os.listdir(directory_path)
# print each file and directory name
for item in contents:
    print(item)