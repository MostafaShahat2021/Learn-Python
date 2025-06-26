# ----------------------
# -- String Methodes --
# ----------------------

# --------
# strip()
# --------

# a = "I Love Python"
# b = "     I love Python     "
# len() => string, tuple,list length
# print(len(a))

# strip() => remove spaces from all string
# rstrip() => remove spaces from right side only
# lstrip() => remove spaces from left side only

# print(b)
# print(b.rstrip())
# print(b.lstrip())
# print (b.strip())

# c = "#### I Love Python ####"
# print(c.strip())
# print(c.rstrip("#"))
# print(c.lstrip("#"))
# print(c.strip("#"))

# --------
# title()
# --------
# str = "i love 2d grafics and 3g tech and python"
# print(str.title())
# print(str.capitalize())

# --------
# zfill()
# --------
# d, e, f = "1", "11", "111"
# print(d)
# print(e)
# print(f)
# print(d.zfill(3))
# print(e.zfill(3))
# print(f.zfill(3))

# --------
# upper()
# lower()
# --------
# name= "mostafa shahat"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print (name.title())

# --------
# split() rsplit()
# --------
# str = "I Love Python and javascript"
# print(str.split())  # split string into a list (split by space by default)
# print(type(str.split()))

# str2 = "I-Love-Python-and-javascript"
# print(str2.split("-"))

# print(str2.split("-", 2))

# # rsplit()
# print(str2.rsplit("-", 2))

# --------
# center()
# --------
# name= "Mostafa"
# print(name.center(13))
# print(name.center(13, "#"))
# print(name.center(11, "@"))

# --------
# count()
# --------

# word= "I love python and PHP becuse PHP is easy"
# print(word.count("PHP"))
# print(word.count("PHP", 0,25))

# --------
# swapcase()
# --------

# str = "I Love Python"
# str2 = "i lOVE pYTHON"
# print(str.swapcase())
# print(str2.swapcase())

# --------
# statswith()
# endswith()
# --------

str = "I Love Python"
print(str.startswith("I"))
print(str.startswith("P"))
print(str.startswith("P", 7, 12))

print(str.endswith("n"))
print(str.endswith("s"))
print(str.endswith("e", 2,6))
