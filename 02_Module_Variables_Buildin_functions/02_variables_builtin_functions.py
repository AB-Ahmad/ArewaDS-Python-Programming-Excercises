# DAY 2 : 30 DAYS OF PYTHON PROGRAMMING
 
FIRST_NAMME = "Ahmad"
LAST_NAME = "BALA"
FULL_NAME = "Ahmad Bala"
COUNTRY = "Nigeria"
CITY = "Joa"
age = 24
year = 2025
is_married = False
is_true = True
is_light_on = True


#A multiply variable declare in a single line
Namee, state_origin,my_age = "Ahmad","Kano",24

#checking the dtata types of this variables
print(type(FIRST_NAMME))
print(type(LAST_NAME))
print(type(FULL_NAME))
print(type(COUNTRY))
print(type(CITY))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#lenght of my first name
print(len(FIRST_NAME))
#COMPARING THE LENGTH OF FIRST NAME AND LAST NAME
print("The length of first name is",len(FIRST_NAME), "while the length of last name is ",len(LAST_NAME))


num_one = 5
num_two = 4

# Arithmetic operation
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
#or uing
#
#import math 
#floor_division = math.float(num_one/num_two)


# Circle calculations
radius = 30  
pi = 3.14159
#formula for area of  circle = pi x radius xx2
area_of_circle = pi * (radius ** 2)
circum_of_circle = 2 * pi * radius

print("\nCircle Calculations:")
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

# Take radius as input and calculate the area
user_radius = float(input("\nEnter the radius of a circle: "))
user_area_of_circle = pi * (user_radius ** 2)
print("Area of Circle with user radius:", user_area_of_circle)

# Get user inputs
user_first_name = input("\nEnter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")

print("\nUser Information:")
print(f"First Name: {user_first_name}")
print(f"Last Name: {user_last_name}")
print(f"Country: {user_country}")
print(f"Age: {user_age}")


print("\nPython Reserved Words:")
help("keywords")



