#empty lists
dog = {}
dog["name"] = "bingo"
dog["colour"] = "brown"
dog["legs"] = 4
dog["age"] = 7

print(dog)



# Create a student dictionary
student = {
    'first_name': 'Ahmad',
    'last_name': 'Bala',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'Machine Learning'],
    'country': 'Nigeria',
    'city': 'jos',
    'address': '111 bauchi road'
}

print("\nStudent dictionary:", student)

# Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# Get the value of skills and check the data type
skills = student['skills']
print("\nSkills:", skills)
print("Type of skills:", type(skills))

# modification
student['skills'].extend(['Data Analysis', 'Cloud Computing'])
print("\nUpdated skills:", student['skills'])

# dictionary keys 
keys = list(student.keys())
print("\nDictionary keys:", keys)

# Get the dictionary values as a list
values = list(student.values())
print("\nDictionary values:", values)

# Change the dictionary to a list of tuples using items() method
tuples_list = list(student.items())
print("\nDictionary as list of tuples:", tuples_list)

# Delete one of the items in the dictionary
del student['address']
print("\nStudent dictionary after deleting 'address':", student)

# Delete one of the dictionaries
del dog
print("\nDog dictionary deleted.")
