
# Function 1: Returns a number multiplied by 2
def double(number):
    return number * 2


# Function 2: Returns True if the score is 50 or more
def is_pass(score):
    return score >= 50


# Function 3: Returns a greeting with a name
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Test the three functions
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))
