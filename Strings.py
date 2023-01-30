

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 60.2

# print(f"{name} is {years} years old and {height_cm}cm tall" )

# F-strings allows us to use methods /evaluations too

name = snoopy
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!!!!")

# F-strings to specify precsion in rounding and decimals

pi = 3.14159265359

print(f"pi to 3 decimal places: {pi: .3f}") # pi to 3 decimal places
print(f"pi to 3 decimal places: {pi: .5f}") # pi to 5 decimal places

score = 16
max_score = 26

