# This program stores my personal information and course goal in variables,
# then prints them out into a natural-sounding introduction.

# Creating the required variables
name = "Jinar"
age = 22
favourite_language = "Python"
goal = "build my own web applications from scratch"

# Displaying four lines of output using the variables
print(f"Hello! My name is {name}.")
print(f"I am {age} years old and love working with technology.")
print(f"My absolute favourite programming language to use is {name if favourite_language == 'Python' else favourite_language}.")
print(f"My main goal for this course is to learn how to {goal}.")
