# Matrix is a special case of two dimensional array where each data element is of strictly
# same size. So every matrix is also a two dimensional array but not vice versa.

from numpy import *
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])

m = reshape(a, (7, 5))
print(m)

# Access values
print("Accessing values")
print(m[2][3])

# Adding a row
print("Add row")
m_r = append(m, [['Avg', 34, 45, 6, 4]], 0)
print(m_r)

# Add column
print("Add column")
m_i = insert(m_r,[5], [[1], [2], [3], [4], [5], [6], [7], [8]], 1)
print(m_i)

# delete row
print("Delete row")
m = delete(m_i, [2], 0)
print(m)

# update a row
print("Update row")
m[0] = ['Th', '22', '33', '33', '44', '21']
print(m)