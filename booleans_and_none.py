
# print(True and False) # False
# Print(False and True) # False
# Print(False or True) # True




# Booleans are useful for quickly checking the state of something.
# The other area Vooleans are really useful are validating data types.

# Booleans with Data types

hi ="Hello world!"

print(hi.isalpha()) # False
print(hi.islower()) # False
print(hi.isupper()) # False
print(hi.endswith(" world!")) # True
print(hi.startswith("Hello")) # True

x = 0
y = 10

print(bool(x)) # False - 0 is always False
print(bool(y)) # True
print(bool(z)) # True

# None

# None == Null in a lot of other languages

print(bool(None)) # False

x = None

print(x == False) # False
print(x == True) # False

print(x == None) # direct compariosn - more complex situation
print(x is None) # Best practice for checking if something 'is None'

print(type (x))




