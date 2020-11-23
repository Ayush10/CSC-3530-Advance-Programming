# Program to convert Celsius to Fahrenheit
# Formula: [#Conversion formula:
# T(℉) = T(℃) x 9/5 + 32
# T(℉) = T(℃) x 1.8 + 32
# ]
# Taking user input
temp = float(input("Enter temperature in Celsius: "))
# Converting
# temp_in_fah = temp * (9 / 5) + 32
# Or
temp_in_fah = temp * 1.8 + 32
# Displaying the result
print("The Celsius temperature converted to Fahrenheit is: %0.2f" %temp_in_fah)