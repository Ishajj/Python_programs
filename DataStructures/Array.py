from array import *
arr = array('i', [3,5,7,8])

# Access array element by index
print(arr[3])

# Access all elements in array
for x in arr:
    print(x)

# Insert element at given position
print("Insertion")
arr.insert(0, 23)

for x in arr:
    print(x)

# Delete element at given position
print("Deletion")
arr.remove(23)

for x in arr:
    print(x)

# Search element at given position
print("Search")
print(arr.index(7))

# Update element
print("Updation")
arr[0] = 90

for x in arr:
    print(x)
