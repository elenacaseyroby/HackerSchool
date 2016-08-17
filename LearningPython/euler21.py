"""
Problem 21:

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def sumProperDivisors(number):
	proper_div = 0
	for i in range(number-1): #don't want to include number itself
		counter = i+1 #or "0"
		if number%(counter) == 0:
			proper_div = proper_div + counter
	return proper_div

def sumAmicableNumbers(number):
	proper_div = [None] * (number+1)
	sum_of_amicable = 0
	#finds sum of proper divisors for all numbers between 1 and number
	for i in range(number):
		counter = i+1
		proper_div[counter] = sumProperDivisors(counter)

	for z in range(number):
		counter = z+1
		if proper_div[counter] <= number:
			if proper_div[proper_div[counter]] == counter and proper_div[counter] != counter:
				sum_of_amicable = sum_of_amicable + proper_div[counter]
				print "d("+str(counter)+") = "+str(proper_div[counter])+" and d("+str(proper_div[counter])+") = "+str(proper_div[proper_div[counter]])

	print "The sum of the amicable numbers under "+str(number)+" is "+str(sum_of_amicable)

print "This program will find the sum of all amicable numbers under any given number.  Please enter a number to find the sum of the amicable numbers beneath it:"
number = int(raw_input())
sumAmicableNumbers(number)

