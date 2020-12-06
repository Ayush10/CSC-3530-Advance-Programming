# Program to check if the number is odd or even and if even then add 5 till sum becomes 100
# Taking user inputs
value = int(input("Enter any number: "))

total = 0

if value % 2 == 0:
    print("The number {0} is even.".format(value))
    total += value
    if total >= 100:
        print("The sum of the given number {0} is {1}.".format(total))
    else:
        total += 5
        if total >= 100:
            print("The sum of the given number {0} is {1}.".format(total))
        else:
            total += 5
            if total >= 100:
                print("The sum of the given number {0} is {1}.".format(total))
            else:
                total += 5
                if total >= 100:
                    print("The sum of the given number {0} is {1}.".format(total))
                else:
                    total += 5
                    if total >= 100:
                        print("The sum of the given number {0} is {1}.".format(total))