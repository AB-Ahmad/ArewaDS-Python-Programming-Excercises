# Concatenate strings
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')
print('Coding' + ' ' + 'For' + ' ' + 'All')

# Declare variable
company = "Coding For All"
print(company)
print(len(company))

print(company.upper)
print(company.lower)

print(capatilze(company))
print(title(comapny))
print(swapcase(comapny))

#slice 
print(comapny[0:6))

#check coding incompany variable

print("is coding contain in  company varibale: ", "coding" in company)
#using find fuction
print(company.find('Coding'))
print(company.replace("coding", "python"))

print(company.replace("ALL",""))
my_string = "coding for all"
print(my_string.split(" "))

m_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(m_string.split(","))

#index chck
print(my_string.index(10))
#indexing
print(my_string[0])
print(my_string[-1])
print(my_string[10])
# acronymn
print(''.join([word[0] for word in "Python For Everyone".split()]))
print(''.join([word[0] for word in "Coding For All".split()]))

#
print(company.index("C"))
print(company.index("F"))

print("Coding For All People".rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))


sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find('because'))
print(sentence.rindex('because'))

# starts or ends with of a String 
print(company.startswith('Coding'))
print(company.endswith('coding'))

print(sentence[sentence.find('because'):sentence.rindex('because'))
print(sentence.replace('because because because', ''))

# String starts or ends with
print(company.startswith('Coding'))
print(company.endswith('coding'))

# Remove trailing spaces
print('   Coding For All      '.strip())

# Check valid identifiers
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Join libraries with hash and spac
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# Tab escape sequence
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# String formatting
radius = 10
area = 3.14 * radius ** 2

print("The area of a circle with radius:",radius, "is", int(area),"meters square.")

# Math operations with string formatting
x, y = 8, 6
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y:.2f}")# to 2 decimal places
print(f"{x} % {y} = {x % y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} ** {y} = {x ** y}")












