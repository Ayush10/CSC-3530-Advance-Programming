# Program to remove duplicate elements from list
# Creating two list
list1 = [1, 2, 3, 1, 2, 3, 4, 5]
list2 = []

# Showing on the console what items are repeated on the list
print("The list with duplicates is: " + str(list1))

# Adding non-repeated elements on the second list
for item in list1:
    if item not in list2:
        list2.append(item)

print("The new list after removing duplicates is: " + str(list2))
