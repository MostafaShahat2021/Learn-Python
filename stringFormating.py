# --------------------------
# String Formating (Old Way)
# --------------------------

# name = "Mostafa"
# age = 40
# rank = 10

# print("My Name is: " + name)
# print("My Name is: " + name + "and my age is: " + age ) # TypeError

# print("My Name is: %s" % "Mostafa")
# print("My Name is: %s" % name)

# print("My Name is: %s and my age is: %d" % (name, age))
# print("My Name is: %s and my age is: %d and my Rank is : %f" % (name, age, rank))

# %s => str
# %d => int | number \ digit
# %f => float \ floating point number

# n = "Mostafa"
# l = "Python"
# y = 10
# print("My name is: %s I'm %s Developer with %d years of Exp" % (n, l, y))

# Cntrol float nubmer
# myNumber = 10
# # print("My number is: %d" % myNumber)
# print("My number is: %f" % myNumber)
# print("My number is: %.2f" % myNumber)
# print("My number is: %.1f" % myNumber)

# Truncate String
# longStr= "Hello El-zero web school people, I love you all"
# print("Message is: %s" % longStr)
# print("Message is: %.5s" % longStr)


# ---------------------------
# String Formating (New Way)
# ---------------------------

# name = "Mostafa"
# age = 40
# rank = 10

# print("My Name is: " + name)
# print("My Name is: " + name + "and my age is: " + age ) # TypeError

# print("My Name is: {}".format("Mostafa"))
# print("My Name is: {}".format(name))

# print("My Name is: {} and my age is: {}".format(name, age))
# print("My Name is: {:s} & age is: {:d} & Rank is: {:f}".format(name, age, rank))

# --------------------
# {:s} => str
# {:d} => number
# {:f} => float
# ---------------------
# =========================================================================================
n = "Mostafa"
l = "Python"
y = 10
print("My name is: {} I'm {} Developer with {} years of Exp".format(n, l, y))

# # Cntrol float nubmer
myNumber = 10
# print("My number is: %d" % myNumber)
print("My number is: {}".format(myNumber))
print("My number is: {:f}".format(myNumber))
print("My number is: %.2f" % myNumber) # Old
print("My number is: {:.2f}".format(myNumber)) # New

#===============================================================
# Format in V 3.6+
myName="Mostafa"
myAge=40
print("My name is: {myName} and my age is {myAge}")
print(f"My name is: {myName} and my age is {myAge}")
#===============================================================