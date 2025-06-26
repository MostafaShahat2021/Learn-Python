# ---------------------------------------------------
# == Caluculate Age Advanced version and training ==
# ---------------------------------------------------


# Iput Note
print("#" * 80)
print(" <= Welcome to Age Calculator => ".title().center(80, "#"))
print(" You can write the first letter or full name of the time unit ".center(80, "#"))
print("#" * 80)

# Collect age dat
age_input = input("Please Enter Your age in Numbers ")
if not age_input.isdigit():
    print("Please Enter your age in Numbers")
    exit()
age = int(age_input)

# Collect Time Unit Data
unitInput = input("Please Choose time Unit : Months, Weeks, Days ").strip().lower()
if not unitInput.isalpha():
    print(
        "Plese enter the first letter of the time unit or the full name of the time unit in LETTERS"
    )
    exit()
unit = unitInput

# Get the time units
months = int(age) * 12
weeks = int(months) * 4
days = int(age) * 365

if unit == "month" or unit == "m":
    print("You choosed the unit Months")
    print(f" You Lived for {months:,} Months ".title().center(80, "#"))
elif unit == "weeks" or unit == "w":
    print("You choosed the unit Weeks")
    print(f" You Lived for {weeks:,} Weeks ".title().center(80, "#"))
elif unit == "days" or unit == "d":
    print("You choosed the unit Days")
    print(f" You Lived for {days:,} Days ".title().center(80, "#"))
