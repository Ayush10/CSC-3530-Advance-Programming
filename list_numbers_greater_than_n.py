# Program to find the number of values greater than thar number in list
number_list = [1, 2, 4, 7, 8, 10, 20, 40, 80, 100]

number = int(input("Enter any number: "))

print("The list: " + str(number_list))

count = 0
for i in number_list:
    if i > number:
        count += 1

print("The numbers greater than {0} are : {1}".format(str(number), str(count)))
