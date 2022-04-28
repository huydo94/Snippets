dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['Class'])
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

# looping techniques

# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
