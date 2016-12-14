from misra_gries.misra_gries import * 
from stream_gen.stream_gen import *
from performance_analysis.accuracy_analysis import *
import sys
import os

## user inputs number of counters, item to estimate frequency for, 
## distribution to use to generate random data, stream length to generate
## thanks to Huy Nguyen (https://www.huyng.com/posts/python-performance-analysis) for performance analysis suggestions
## thanks to Robert Kern for the time line profiler, and Fabian Pedregosa for the memory line profiler

while True:
	try:
		counters = int(input("How many counters would you like to use? "))
		assert(counters > 0), 'Number must be bigger than 0'
		break
	except:
		print("not a valid choice")

while True:
	item = input("Which item's frequency would you like to estimate? (Items are integers in [-500,500] ")
	if int(item) not in range(-500,501):
		print("not a valid choice")
	else:
		print ("you entered " + item)
		break

while True:
	distribution = input("Which distribution would you like to randomly generate the stream from, normal or uniform? ")
	if distribution.lower() not in ('normal','uniform'):
		print("not a valid choice.")
	else:	
		print("you selected the " + distribution + " distribution")
		break

while True:
	try:
		stream_length = int(input("How large a stream would you like to use? "))
		assert(stream_length>counters)
		break
	except: 
		print("not a valid choice")

## this line functions with kernprof.py to evaluate time performance and with memory_profiler to evaluate memory use
@profile
def main(item, counters, distribution, stream_length):
	## generate random data
	if distribution.lower() == 'uniform':
		data = gen_unif(stream_length)
	if distribution.lower() == 'normal':
		data = gen_norm(stream_length) 	

	## run MG on data
	out = misra_gries(get_items(data),int(counters))
	try:
		estimate = [t[1] for t in out if t[0] == int(item)][0]
	except:
		estimate = 0
	print("The estimated frequency of item " + item + " is: " + str(estimate))

	## accuracy analysis
	frequencies = get_frequencies(data)
	errors = get_errors(out,frequencies[0])
	items = frequencies[1]
	max_error = max(errors)
	test_errors(errors,stream_length,counters)

	print("The largest error is " + str(max_error))
	print("The total error across all items is " + str(sum(errors)))
	print("The average error per item is " + str(sum(errors)/items))


if __name__ == "__main__":
    main(item, counters, distribution, stream_length)