import array as arr
a = arr.array('i', [10,24,33,42,55,65,74,89])

for i in range(0,8):
    print(a[i], end =" ")
print("\r")

print("The index of 1st occurrence of 24 is : ", end = " ")
print(a.index(24))

print("The index of 1st occurrence of 55 is : ", end = " ")
print(a.index(55))

print("The index of 1st occurrence of 74 is : ", end = " ")
print(a.index(74))
