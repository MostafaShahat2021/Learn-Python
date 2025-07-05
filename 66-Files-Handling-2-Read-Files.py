# --------------------------------
# -- File Handling => Read File --
# --------------------------------


myFile = open(r"C:\Users\Mostafa-PC\Desktop\python\Files\mostafa.txt", "r")
# print(myFile) # file data object
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)

# print(myFile.read())
# print(myFile.read(5))

# print(myFile.readline(5))
# print(myFile.readline())
# print(myFile.readline())

# print(myFile.readlines())
# print(myFile.readlines(50))
# print(type(myFile.readlines()))

for line in myFile:
  print(line)
  if line.startswith("07"):
    break
# close file
myFile.close()