a = \
    int(input('''Enter your choice:
 1. Bubble Sort
 2. Insertion Sort
'''))
if a == 1:
    list1 = list(eval(input('Enter your list (comma separated): ')))
    n = len(list1)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list1[j] > list1[j + 1]:
                (list1[j], list1[j + 1]) = (list1[j + 1], list1[j])
    print ('The sorted list is:', list1)
if a == 2:
    list1 = list(eval(input('Enter your list (comma separated): ')))
    for i in range(1, len(list1)):
        key = list1[i]
        j = i - 1
        while j >= 0 and key < list1[j]:
            list1[j + 1] = list1[j]
            j = j - 1
        else:
            list1[j + 1] = key
    print ('The sorted list is:', list1)
