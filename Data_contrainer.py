''' In this file we use Data Container to Store data
    1 . LIST
    2 . Tuple
    3 . Dictionary
'''

# LIST 

# Store the data in squance way  and Different data type
std = ["abc",190,'male', "dehli",80,70,98,79]

# Print the whole list 
print(std)  

# Print the data throw index
print(std[3])  # "city"

# Add the data in List
std.append(90)
print(std)

# Remove the element in list
std.remove(90)
print(std)

# Print the revers list
print(std[::-1])

# Print data throw loop statement
for i in std:
    print(i) # print data index by index

# Crate a list throw loop statement
l1= [i*i for i in range(10)] # Square of numbers 0 - 9
print(l1)

l2= [i*2 for i in range(11)] # Table of 2
print(l2)

# # Add two list
l3 = l1 +l2
print(l3)


#  Tuple 
# Tuple are also use store data as list 
# Tuple are immutable ( Once you creat tuple you cannot change tuple dirrctly )

std = ("abc",190,'male', "dehli",80,70,98,79)

print(std)
print(type(std))

print(std [0]) # print by index

# Print data by loop 
for i in std :
    print(i)

# Change in Tuple 
s = list(std)      # Convert to list
s[3] = "Mumbai"    # Modify list element
std = tuple(s)     # Convert back to tuple
print(std)  

# Dictionary
# Dictionary are use store in a Key - Value Pair
# Dictionary are mutable
# Dictionary are uniqe keys but values may be duplicate 

std = {
    "name" : "abc",
    "Roll no" : 121,
    "Gender" : "male",
    "city": "dehli",
    "math" :94,
    "english" : 80,
    "hindi" : 75,
    "SSt" :89

}

# print(std)
print(type(std))

# Print data by key
print(std["city"])
print(std["Roll no"])

# Print all keys
print(std.keys())

# Print all values
print(std.values())

# Print all Pairs 
print(std.items())