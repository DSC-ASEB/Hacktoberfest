# Python has a set of built-in methods which can be used on lists

# Creating a "Things" list and "Languages" list
Things = ['pen', 'pencil', 'phone']
Languages = ['Kannada', 'Telugu', 'Tamil']

# To add an element at the end of the list
print("***---------------append() Operation---------------***")
## append() operation to add 'book' to "Things" list
print("Before appending 'book' to 'Things' list: Things = ", Things)
Things.append('book')   # Things = ['pen', 'pencil', 'phone', 'book']
print("After appending 'book' to 'Things' list: Things = ", Things) 

# To add a list at the end of the another list
## append() operation to append 'Languages' list to "Things" list
print("Before appending Languages list: \nThings = ", Things, "\nLanguages = ", Languages)
Things.append(Languages)   # Things = ['pen', 'pencil', 'phone', 'book', ['Kannada', 'Telugu', 'Tamil']]
print("After appending Languages list: \nThings = ", Things, "\nLanguages = ", Languages) 

# To add an element at the specified position
print("\n***---------------insert() Operation---------------***")
## insert() operation to add 'mask' to the "Things" list at the starting
print("Before insert() operation: Things = ", Things)
Things.insert(0, 'mask')            # Things = ['mask' ,'pen', 'pencil', 'phone', 'book', ['Kannada', 'Telugu', 'Tamil']]
print("After insert() operation 'mask' at index 0: Things = ", Things)

## insert() operation to insert the 'Malayalam' element in "Things[5]" list (sublist in "Things" list) at index '2'
print("Before insert() operation at Things[5]: Things = ", Things)
Things[5].insert(2, "Malayalam")    # Things = ['mask', 'pen', 'pencil', 'phone', 'book', ['Kannada', 'Telugu', 'Malayalam', 'Tamil']]
print("After insert() operation 'Malayalam' at Things[5] at index '2': Things = ", Things)

# To find the index of the first element with the specified value
print("\n***---------------index() Operation---------------***")
## index() operation to find the index of the 'mask' in "Things" list
print("Things list: Things = ", Things)
print("Index of 'mask' in 'Things' list: ", Things.index("mask"))      # returns '0' (since mask is the starting element of the "Things" list)

## index() operation to find the 'Tamil' element in "Things[5]" list (sublist in "Things" list)   
print("Index of 'Tamil' in 'Things[5]' list: ", Things[5].index("Tamil") )   # returns '3' (since 'Tamil' element is of index '3' in Things[5] list)

# To remove an element at the specified position
print("\n***---------------pop() Operation---------------***")
# pop() operation to remove an element from the list
## by default, if no index is specified in pop(), last element in the list will be popped.
print("Before pop() operation on 'Things' list: Things = ", Things)
Things.pop()    # Things = ['mask', 'pen', 'pencil', 'phone', 'book']
print("After pop() operation on 'Things' list: Things = ", Things)

## if index is specified, corresponding element is removed from list.
print("Before pop() operation on 'Things' list at index '0': \nThings = ", Things)
Things.pop(0)   # Things = ['pen', 'pencil', 'phone', 'book']
print("After pop() operation on 'Things' list at index '0': \nThings = ", Things)

# To remove an element with the specified value from the list
print("\n***---------------remove() Operation---------------***")
## remove() operation to remove an element
print("Before remove() operation: \nThings = ", Things)
Things.remove("pen")    # Things = ['pencil', 'phone', 'book']
print("After removing 'pen' from the 'Things' list: \nThings = ", Things)

# To make a copy of the list
print("\n***---------------copy() Operation---------------***")
## copy() operation to copy of the 'Languages' list in 'Lang' list
print("Copying the Languages list into 'Lang' list")
Lang = Languages.copy() # Lang = ['Kannada', 'Telugu', 'Malayalam', 'Tamil']
print("After copy() operation: Lang = ", Lang)

## list() operation to make a copy of the 'Things' list 'Accessories' list
print("list() operation on 'Things' list to copy into 'Accessories' list")
Accessories = list(Things) # Accessories = ['pencil', 'phone', 'book']
print("Accessories list: ", Accessories)

# To count the number of elements with the specified value in the list
print("\n***---------------count() Operation---------------***")
## count() operation to find frequency of an element "2" in numbers list
numbers = [1, 2, 3, 2, 1, 2, 2, 1, 2, 3, 4, 5, 2, 4, 5, 4, 5, 6]
print("numbers List: numbers = ", numbers, "\ncount of number '2' in numbers list: ", numbers.count(2))    # returns 6 (frequency of the number '2' in numbers list is 6)

# To add all the elements from one list to other list
## extend() operation to add the elements from "Languages" list to "Things" list
print("\n***---------------extend() Operation---------------***")
print("Before extend() operation: \nLanguages = ", Languages, "\nThings = ", Things)
Languages.extend(Things)     # Languages = ['Kannada', 'Telugu', 'Malayalam', 'Tamil', 'pencil', 'phone', 'book'] 
print("After extend() operation: \nLanguages = ", Languages, "\nThings = ", Things)

## using '+' operator to add the elements of "Things" list to "Lang" list
print("Before using '+' operator: \nLang = ", Lang, "\nThings = ", Things)
Lang = Lang + Things   # Lang = ['Kannada', 'Telugu', 'Malayalam', 'Tamil', 'pen', 'pencil', 'phone', 'book']
print("After using '+' operator: \nLang = ", Lang, "\nThings = ", Things)

# To reverse the order of the list
print("\n***---------------reverse() Operation---------------***")
## reverse() operation to reverse the list
print("Accessories list before reversing: \nAccessories = ", Accessories)
Accessories.reverse()        # Accessories =  ['book', 'phone', 'pencil']
print("After the reverse() operation on Accessories list: \nAccessories = ", Accessories)

# To sort the list
print("\n***---------------sort() Operation---------------***")
## sort() operation to sort the list
print("Before the sort() operation: \nLang = ", Lang)
Lang.sort()         # Lang = ['Kannada', 'Malayalam', 'Tamil', 'Telugu', 'book', 'pencil', 'phone']
print("After the sort() operation on Lang list: \nLang = ",Lang)
print("Before the sort() operation: \nnumbers = ", numbers)
numbers.sort()      # numbers =  [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6]
print("After the sort() operation on numbers list: \nnumbers = ", numbers)

# To remove all the elements from the list
print("\n***---------------clear() Operation---------------***")
## clear() operation to remove all elements from 'Languages' List
print("Before clear() operation on Languages List: \nLanguages = ", Languages)
Languages.clear()       # Langugaes = []
print("After clear() operation on Languages List: \nLanguages = ", Languages)
