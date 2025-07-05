# -----------------------------------------------------
# -- Files Handling => Write and Append In Files --
# -----------------------------------------------------

#-------------------------
# ====== WRITE FILES =====
#-------------------------

# import os

# create the file if not exist
# myFile = open(r"C:\Users\Mostafa-PC\Desktop\python\Files\my-file.txt", "w")
# myFile.write("Hello from Python file with Love\n")
# myFile.write("Second Line")

# print(f"{os.getcwd()}/Files/my-file.txt")
# print(os.path.abspath(r"Files/my-file.txt"))

# myFile = open(os.path.abspath(r"Files/my-file.txt"), "w")
# myFile = open("Files/my-file.txt", "w")
# myFile.write("Hello from Python file with Love\n")
# myFile.write("Second Line")
# myFile.close() # Make sure to close the file after writing

# # readMyFile = open(os.path.abspath(r"Files/my-file.txt"), "r")
# readMyFile = open("Files/my-file.txt", "r")
# print(readMyFile.read())
# readMyFile.close()

# =================================================

# myFile = open(r"Files/fun.txt", "w")
# myFile.write("Python is fun\n" * 100)
# myFile.close()


#===================================================

# myList = ["Mostafa\n", "Khaled\n", "Wesal\n"]
# myFile=open("files/list.txt", "w")
# myFile.writelines(myList)
# myFile.close()

# ==============================================================================================================================================
# with open(os.path.abspath(r"Files/my-file.txt"), "w") as myFile:
#     myFile.write("Hello from Python file with Love\n")

# with open(os.path.abspath(r"Files/my-file.txt"), "r") as readMyFile:
#     print(readMyFile.read())

# The `with ... as ...` syntax in Python is called a **context manager**. It is commonly used for resource management, such as working with files. When you use:

# ````python
# with open("filename.txt", "w") as myFile:
#     myFile.write("Hello")
# ````

# Python automatically handles opening and closing the file for you. When the code inside the `with` block finishes (even if an error occurs), Python will automatically close the file. This helps prevent resource leaks and makes your code safer and cleaner.

# **Benefits:**
# - No need to explicitly call `close()`
# - Handles exceptions safely
# - Makes code more readable

# You can use `with` for files, network connections, database connections, and more—anywhere you need to set up and clean up resources.

# ==============================================================================================================================================


#--------------------------
# ====== APPEND FILES =====
#--------------------------

myFile = open("Files/my-file.txt", "a")
myFile.write("Hello\n")
myFile.write("Third Line\n")
myFile.close()