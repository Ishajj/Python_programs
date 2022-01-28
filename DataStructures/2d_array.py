from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

# Access 2-D array elements
print(T[0][3])

print(type(T))

# Insert values
print("Insert values")
T.insert(1, [3,2,2,2])

for x in T:
    for r in x:
        print(r, end = " ")
    print()

# Update values
print("Update values")
T[2] = [3, 5]
for x in T:
    for r in x:
        print(r, end = " ")
    print()

# Delete values
print("Delete values")

del T[3]

for x in T:
    for r in x:
        print(r, end = " ")
    print()