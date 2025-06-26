# ---------------------
# -- FUNCTIONS --
# ---------------------


# function syntax
def function_name():
    print("Hello Python from inside fubction")


# function call
# function_name()


def hello():
    return "Hello Python"


dataFromFunction = hello()
# print(dataFromFunction)
# ---------------------------------------------------------

# --------------------------------------
# -- function Parametrs and Arguments --
# --------------------------------------


def say_hello(name):  # parameter
    print(f"Hello {name}")


# say_hello("Mostafa") #argument

# ------------------------------


def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Integers Only Allowed!")
    else:
        print(n1 + n2)


# addition(2,3)
# addition(2,"3")


def fullName(first, middle, last):
    print(
        f"Hello {first.strip().capitalize()} {middle.strip().capitalize().upper():.1s} {last.capitalize()}"
    )


# fullName("mostafa", "shahat", "sayed")

# ======================================================================================

# ----------------------------------------------------
# -- function packing and unpacking Arguments *Args --
# ----------------------------------------------------


# *args allows a function to accept any number of positional arguments. Inside the function, args is a tuple containing all extra positional arguments passed.
# packed as a tuple

# print(1,2,3)
myList = [1, 2, 3]
# print(myList)
# print(*myList)


# def say_hello(n1, n2, n3, n4):
#     people = [n1, n2, n3, n4]
#     for name in people:
#         print(f"Hello {name}")

# say_hello("Mostafa", "Khaled", "Eslam", "Asser")


# Use [ *args ] to pack arguments in to a tuple When you don't know in advance how many arguments wiil be passed to the function
def say_hello(*people):
    for name in people:
        print(f"Hello {name}")


# say_hello("Mostafa", "Khaled", "Eslam", "Asser")


def show_details(name, *skills):
    print(f"Hello {name} your skills is:")
    for skill in skills:
        print(skill)


# show_details("Mostafa", "Html", "Css", "Js", "Python")

# ======================================================================================

# ----------------------------------------------------
# -- Function Default Parameters --
# ----------------------------------------------------


# if your function has only one defualt parameter it should be the last
def say_hello(name, age, country="Unknown"):
    print(f"Hello {name}, your age is {age}, and your country is {country}")


# say_hello("Mostafa", 40, "Egypt")
# say_hello("Mohamed", 30)

# =====================================================================================

# ---------------------------------------------------------------------
# -- Function Packing Unpacking Keyword Arguments **KWArgs --
# ---------------------------------------------------------------------

# **kwargs allows a function to accept any number of keyword arguments. Inside the function, kwargs is a dictionary containing all extra named arguments.
# packed as a dict

def show_skills(*skills):
    print(type(skills))  # tuple
    for skill in skills:
        print(skill)


# show_skills("Js", "Py", "MySQL")


# def show_skills(**skills):
#     print(type(skills))  # dict
#     # print(skills)
#     for skill, value in skills.items():
#         print(f"{skill} => {value}")


# show_skills(Js="80%", Py="75%", MySQL="67%")



mySkills = {"Js": "80%", "Py": "75%", "MySQL": "67%"}

def show_skills(**skills):
    print(type(skills))  # dict
    # print(skills)
    for skill, value in skills.items():
        print(f"{skill} => {value}")


# print(mySkills)
# show_skills(mySkills) # Error
# show_skills(**mySkills) # unpack the dict


