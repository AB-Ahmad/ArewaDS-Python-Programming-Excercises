# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#level1
print(len(it_companies))
#add twitter
print(is_campanies.add("Twitter"))

#update others

it_companies.update({'Snapchat', 'TikTok', 'Netflix'})
print(it_companies)
#remove

it_companies.remove('Google')  # Replace 'Google' with any company name from the set
print(it_companies)

#remove: Raises an error if the item to be removed is not found in the set.
#discard: Does not raise an error if the item to be removed is not found in the set.


#level2
#Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely


#join
jjoin = A.union(B)
print(jjoin)
intersect = A.intersection(B)
print(intersect)

#subsets
print(A.issubsets(B))
#disjoints
print(A.isdisjoint(B))

#Join A with B and B with A
A.update(B)
B.update(A)
print(A)
print(B)
#symmmetric diff btw A and B
sym_diff = A.symmetric_difference(B)
print(sym_diff)

#del
del A
del B
del it_companies

#level3 
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_sets = set(age)
age_len = len(age)
age_set_len = len(age_sets)
if age_len > age_set_len:
  print("sets is bigger than age")
  else;
  prinnt("age is bigger than the sets")

# #differnce btw strings,list and sets
# String: Immutable sequence of characters.
# List: Mutable, ordered collection of items, allows duplicates.
# Tuple: Immutable, ordered collection of items, allows duplicates.
# Set: Unordered collection of unique items, does not allow duplicates.




#find number of unique word
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))








