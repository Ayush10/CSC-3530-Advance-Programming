# Program to find max numbers using function
def maximum(num1, num2):
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result


def main():
    num1 = 5
    num2 = 10
    print("The max number between {0} and {1} is {2}.".format(str(num1), str(num2), str(maximum(num1, num2))))


if __name__ == "__main__":
    main()
