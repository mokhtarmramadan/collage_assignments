# Write a Python program to sum of three given integers. However,
#if two values are equal sum will be zero.
first, second, third = input("Numbers: ").split(" ")
summation = float(first) + float(second) + float(third)
if first == second or first == third or second == third:
    summation = 0
    print(summation)
else:
    print(summation)

