import sys
from math import log10 # Get the log base 10 function
from random import random # Get the random number generator function

def benfordWrapper(digits):
	num = 0 # Set the number to return to 0
	for i in range(1,digits + 1): # For each number of digits
		num += benford(i) * 10**(digits - i) # Take the benford digit, and multiply it by it's place in the
	return num

def benford(digit):
	# Begin: Calcuate distrubtion
	dist = [float(0)] * 10 # Initialize Benford distribution array
	if digit == 1: # If this is the first digit, the distrubtion is calcuated slightly different
		for i in range(1,10): # For every integer in 1 to 9 (incluive)
			dist[i] = log10(1 + 1/float(i)) # Calcuate it's Benford dist
	else:
		for i in range(0,10): # For every integer in 0 to 9 (incluive)
			j = 10**(digit - 2) # The lower sum bound (inclusive)
			high = 10**(digit - 1) # The upper sum bound (exclusive)
			while j < high: # Calc the distrubtion
				val = float(1 + 1/(10 * j + float(i)))
				dist[i] += log10(val)
				j+=1
	# /End: Calcuate distrubtion
	# Begin: Generate a Benford number
	rand = random()
	numsum = dist[0]
	i = 0
	while rand > numsum: # Find the first number for which the random number is smaller than the summed distributions of the numbers smaller than it
		i += 1
		numsum += dist[i]
	return i
	# /End: Generate a Benford number

# Begin: Handle CLI usage
if len(sys.argv) != 2: # If they providd an incurrent number of arguments, display an error
	print 'You must provide the number of digits you want the number to be. If you want a five-digit number, try running `benford.py 5`.'
else:
	print benfordWrapper(int(sys.argv[1]))
