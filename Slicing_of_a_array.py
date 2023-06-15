import array as arr
l=[1,2,3,4,5,6,7,8,9,10]

a = arr.array('i',l)
print("initial array: ")
for i in (a):
    print(i,end = " ")

slicing_array = a[3:8]
print("\nSlicing of a Array in Range 3-8: ")
print(slicing_array)

# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)

# Printing elements from
# beginning till end
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)