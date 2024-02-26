import numpy
# calculate the sum of three given numbers
# if the values are equal then return thrice of their sum
first, second, third = input("Please enter three numbers: ").split(' ')

summation = numpy.sum([float(first), float(second), float(third)])

if first == second == third:
    print(summation * 3)
else:
    print(summation)
