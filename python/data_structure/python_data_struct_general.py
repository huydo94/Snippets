# https://docs.python.org/3/tutorial/datastructures.html

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)

# To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# There is a way to remove an item from a list given its index instead of its value: the del statement. 
# This differs from the pop() method which returns a value. The del statement can also be used to remove slices 
# from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:]