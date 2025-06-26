# -------------------------
#  -- Control Flow --
#  -- Nestied If   --
#  -- Make Decisions --
# ------------------------

uName = input("What's Your Name?").strip().capitalize()
uContry = input("What's Your Country?").strip()
isStudent = input("Are You a Student? answer with \"Yes\" or \"No\"").strip().capitalize()
cName = "Pyathon Course"
cPrice = 100

if uContry == "Egypt" or uContry == "Sudan":
    if isStudent == "Yes":
        print(f"Hi, {uName} becuse you sre a Student from {uContry}")
        print(f'the "{cName}" price is: ${cPrice - 90 }')
    else:
        print(f"Hi, {uName} becuse you are from {uContry}")
        print(f'the "{cName}" price is: ${cPrice - 80 }')
elif uContry == "KSA" or uContry == "Kuwait":
    print(f"Hi, {uName} becuse you are from {uContry}")
    print(f'the "{cName}" price is: ${cPrice - 30 }')
else:
    print(f"Hi, {uName} becuse you are from {uContry}")
    print(f'the "{cName}" price is: ${cPrice -10}')
