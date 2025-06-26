# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

# regular if statment

contry = ""
# if contry == "Egypt":
#     print(f"The Weather in {contry} is 15")
# elif contry == "KSA":
#     print(f"The Weather in {contry} is 30")
# else:
#     print("This country is not in the List!")
print(
    f"The Weather in {contry} is 15"
    if contry == "Egypt"
    else (
        f"The Weather in {contry} is 30"
        if contry == "KSA"
        else "This country is not in the List!"
    )
)


# ----------------------------------

movieRate = 18
age = 18

if age < movieRate:
    print("Movie is not good 4 U!")  # condition if true
else:
    print("Movie is good 4 U, Happy Watching")  # condition if false

# Short If
# syntax=>condition if True| If condition | Else | condition if False
print(
    f"Movie is not good 4 U" if age < movieRate else "Movie is good 4U Happy Watching"
)
