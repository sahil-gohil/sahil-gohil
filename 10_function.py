# # Exercise: Functions in python

# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

# def calculate_area(base, height):
#     return print((1/2)*base*height)



# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
def calculate_area(base, height, shape = "triangle"):
    if shape == "rectangle":
        return print(base*height)
    else:
        return print((1/2)*base*height)
        
calculate_area(5,10)
calculate_area(5,10,"rectangle")

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,

# *
# **
# ***

# if input is 4 then it should print

# *
# **
# ***
# ****

# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def rtriangle(num):
    
    for i in range(num+1):
        star = ""
        for k in range(i):
            star += "*" 
        print(star)

rtriangle(5)