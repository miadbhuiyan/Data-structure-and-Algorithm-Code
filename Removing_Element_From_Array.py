import array

a = array.array('i',[1,2,3,4,5])

# printing original array
print("The new created array is: ",end = " ")
for i in (a):
    print(i,end = " ")
print()

# using pop() to remove element at 2nd position
print("The popped element is : ",end= " ")
print(a.pop(2))

# printing array after popping
print("The array after pop : ",end = " ")
for i in (a):
    print(i,end = " ")
print()

# using remove() to remove 1st occurrence of 1
a.remove(1)
# printing array after removing
print("The new created array is: ",end = " ")
for i in (a):
    print(i,end = " ")
print()

# using remove() to remove 1st occurrence of 1
a.remove(3)
# printing array after removing
print("The new created array is: ",end = " ")
for i in (a):
    print(i,end = " ")
print()