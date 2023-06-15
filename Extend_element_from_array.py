# Python program to demonstrate

# Adding Elements to a Array

# importing "array" for array creations

import array as arr

# array with int type

a = arr.array('i', [1, 2, 3, 4, 5])

# printing original array

print("The before array extend  : ", end=" ")

for i in range(0, 5):
    print(a[i], end=" ")

print()

# creating an array with using extend method

a.extend([6, 7, 8, 9, 10])

# printing original array

print("\nThe array after extend :", end=" ")

for i in range(0, 10):
    print(a[i], end=" ")

print()