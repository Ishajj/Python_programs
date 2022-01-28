import collections
# ChainMap work as stacks, type of data structure to manage multiple dictionaries together as one unit.
# The combined dictionary contains the key and value pairs in a specific sequence eliminating any
# duplicate keys.

dict1 = {'day1': 'Mon', 'day2': 'Tue', 'day3': 'Wed'}
dict2 = {'day4': 'Thu', 'day5': 'Fri', 'day6': 'Sat'}

res = collections.ChainMap(dict1, dict2)

print(res.maps, '\n')

print("Keys.{}".format(list(res.keys())))
print("Values.{}".format(list(res.values())))

print("All elements in the list")
for key, val in res.items():
    print(key + ":" + val)