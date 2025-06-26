# ---------------------------
# -- Practical Slice Email --
# ---------------------------

# email = "mostafa@egylink.com"
# userName = email[: email.index("@")]
# domain = email[email.index("@")+1:]
# print(userName)
# print(domain)

# name = 'What\'s Your Name?'.lower()
# domain= input("What's Your Domain?")
# print(f"Your Email is {name}@{domain}")

name = input('What\'s Your Name?').strip().capitalize()
email = input("What's Your Email?").strip()

print(f"Hello {name} Your Email is {email}")
print(f"Your user name is {email[:email.index("@")]} \nyour Domain is {email[email.index("@")+1:]}")


