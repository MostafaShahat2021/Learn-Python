# ------------------------------
# -- File Handling --
# ------------------------------

# "a" Append Open File For Appending Values, Create File If Not Exists
# "r" Read [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write Open File For Writing, Create File If Not Exists
# "x" Create Create File, Give Error If File Exists
# ------------------------------

import os

# print(os.getcwd())  # Get the current working directory
# print(os.path.abspath(__file__))  # Return an absolute path.
# print(os.path.dirname(os.path.abspath(__file__)))  # directory for the oppened file
# os.chdir(os.path.abspath(__file__))  # change current working directory

# file= open("Files/mostafa.txt") # relative path
# file= open("C:/Users/Mostafa-PC/Desktop/python/Files/mostafa.txt") # abselute  path

file = open(r"C:\Users\Mostafa-PC\Desktop\python\Files\mostafa.txt")
