# importing array module
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# printing original array
print("Array before updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")

print("\r")

arr[3] =1020
print("Array After updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")

arr[1] =102
print("\nArray After updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")