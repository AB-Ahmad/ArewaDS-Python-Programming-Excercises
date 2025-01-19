#variable declaraton
age = 24 
height = 28.7
complex_number = 2+ 3j

print("Age",age,"Height",height,"complex_number",complex_number)

# Calculate area of a triangle
base = float(input("\nEnter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area_of_triangle = 0.5 * base * height
#print(f"The area of the triangle is {area_of_triangle}")
print("The area of the triangle is",area_of_triangle)


# Calculate perimeter of a triangle
a = float(input("\nEnter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter_of_triangle = a + b + c
print("The perimeter of the triangle is ",perimeter_of_triangle)

# Calculate area and perimeter of a rectangle
length = float(input("\nEnter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print(f"The area of the rectangle is " area_of_rectangle)
print(f"The perimeter of the rectangle is",perimeter_of_rectangle)
# calculate the slope of y = 2x-2
#by difrentiation to get my slope whc=ich isequal to 2
m= 2 # slope
print("slope = ",m )
x-intercepts = 1 # when y = 0
y-intercepts = -2 # when x = 0

#slope and euclidean distance
# m= y2=y1/x2-x1 and point is (2,2) and (6,10)
x1,y1,x2,y2 = 2,2,6,10
m2 = (y2-y1)(x2-x1)
e_distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("The slope is",m2)
print("The euclidean ditance is"e_distance)

#comaprarison of the two previous calculated slopes
print("comparison of the 2 slopes", m == m2)

# Length comparison and falsy statement
python_len = len("python")
dragon_len = len("dragon")
print("Is length of 'python' equal to 'dragon'?", python_len == dragon_len)

# Check 'on' in both 'python' and 'dragon'
print("'on' in both 'python' and 'dragon':", "on" in "python" and "on" in "dragon")

# Check 'jargon' in sentence
sentence = "I hope this course is not full of jargon."
print("'jargon' in sentence:", "jargon" in sentence)

# Convert length of 'python' to float and string
python_len_float = float(python_len)
python_len_str = str(python_len)
print("Float length:", python_len_float, "String length:", python_len_str)



# Calculate pay
hours = float(input("\nEnter hours worked: "))
rate = float(input("Enter rate per hour: "))
weekly_pay = hours * rate
print(f"Your weekly earning is {weekly_pay}")


# Display table
print("\n1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")










