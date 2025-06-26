# -------------------------
#  -- Control Flow --
#  -- if, elif, else   --
#  -- Make Decisions --
# ------------------------

uName = input("What's Yor Name?").strip().capitalize()
uContry = input("What's Your Contry?").strip().upper()
cName = "Pyathon Course"
cPrice = 100

if uContry == "Egypt":
    print(f"Hello {uName} becuse you are from {uContry}")
    print(f'the "{cName}" price is: ${cPrice - 80 }')
elif uContry == "KSA":
    print(f"Hello {uName} becuse you are from {uContry}")
    print(f'the "{cName}" price is: ${cPrice - 30 }')
else:
    print(f"Hello {uName} becuse you are from {uContry}")
    print(f'the "{cName}" price is: ${cPrice -10}')
