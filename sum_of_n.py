# Program that prints the num of n natural numbers
# N is given by the user
number = int(input("Enter any number: "))

a = 1
numbers = ""
total = 0

while a <= number:
    temp = a
    a = a + 1
    numbers = numbers + " + " + str(temp)
    total += temp
    print(numbers)

print("The sum of {0} from the given range of natural numbers {1} is {2}.".format(numbers, number, total + 1))
