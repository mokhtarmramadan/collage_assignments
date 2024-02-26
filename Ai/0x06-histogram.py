import numpy
# Write a Python program to create a histogram from a given list of integers
int_list = [1 , 3, 4, 5, 6, 3, 3]
data = numpy.array(int_list)
histogram = numpy.histogram(data)
print(histogram)
