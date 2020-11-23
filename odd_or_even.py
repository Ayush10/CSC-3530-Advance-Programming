# Program to check odd or even
# Taking user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# Declaring initial value of sum to make it global
sum = 0
extra_sum = 0
# Checking if the user input satisfies the condition
if a % 2 == 0 and b % 2 == 0:
    sum = a + b
    # Since we need to add in terms of multiples of 5 declaring another variable with
    # initial value of 5
    c = 5
    # Checking the second condition
    while sum <= 100:
        sum = sum + c
        c = c + 5
        # When sum reaches more than 100, Safety Measure
        if sum > 100:
            extra_sum = sum - 100
    # To satisfy the condition of the question
    sum = sum - extra_sum
    # Printing the obtained results
    print("""The numbers are {0} and {1} and the sum is {2}.
    We also got extra sum of {3}.""".format(a, b, sum, extra_sum))
# When the numbers are odd, Simply printing the result with no further calculations
else:
    print("""The numbers {0} and {1} are odd so no further processing.""".format(a, b, sum, extra_sum))
    