# Program to print values greater than the arithmetic mean of the given list
random_list = [0, 6, 4, 5, 7, 8, 9]
# List contains the values greter than the arithmetic mean of the given elements
final_list = []

# Initializing mean to 0 to define the scope of the variable that is global
mean = 0
total = 0

# Finding the arithmetic mean
for i in random_list:
    total += i
    mean = sum(random_list) / len(random_list)

for i in random_list:
    if i > mean:
        final_list.append(i)

# Displaying Results
print("The given random list is: " + str(random_list))
print("The arithmetic mean obtained of the given elements is: %.2f" % mean)
print("The new list which contains values greater than the arithmetic mean is: " + str(final_list))
