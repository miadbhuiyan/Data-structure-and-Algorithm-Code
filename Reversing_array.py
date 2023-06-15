import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])

# Print the original array
print("Original array:", *my_array)

# Reverse the array in place
my_array.reverse()

# Print the reversed array
print("Reversed array:", *my_array)