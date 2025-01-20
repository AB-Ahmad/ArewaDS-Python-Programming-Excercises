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
print(sentence.finf("because"))











