# -----------------------
# === Function Lambda ===
# -----------------------

# [1] it has no name
# [3] You can call it inline without defining it
# [4] You can use it in return data from another function
# [5] Lambda used for simple functions and def handels the large tasks
# [6] Lambda is One Single Expression not block of code
# [7] Lambda type is function


def say_hello(name, age):
    return f"Hello {name}, your age is {age}"


# Lambda
hello = lambda name, age: f"Hello {name}, your age is {age}"


print(say_hello("Mostafa", 30))
print(hello("Mostafa Shahat", 40))

print(say_hello.__name__) # say_hello
print(hello.__name__) # <lambda>

print(type(hello)) # <class 'function'>
