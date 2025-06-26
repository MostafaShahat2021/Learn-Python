# -------------------------------------
# -- Practical Your Age Full Details --
# ---------------------------------------

# age input
age = int(input("What's Your Age?").strip())

# Get age in all time units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = hours * 60

# Output
print(f"You Lived For:")
print(f"{months} months")
print(f"{weeks:,} weeks")
print(f"{days:,} days")
print(f"{hours:,} hours")
print(f"{minutes:,} minutes")
