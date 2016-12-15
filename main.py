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
		counters = int(input("How many counters would you like to use? ") or 500)
		assert(counters > 0), 'Number must be greater than 0'
		break
	except:
		print("not a valid choice")
print("you entered " + str(counters))

while True:
	item = int(input("Which item's frequency would you like to estimate? (Items are integers in [-5000,5000] ") or 0)
	if int(item) not in range(-5000,5001):
		print("not a valid choice")
	else:
		print ("you entered " + str(item))
		break

while True:
	distribution = input("Which distribution would you like to randomly generate the stream from, normal or uniform? ") or "normal"
	if distribution.lower() not in ('normal','uniform'):
		print("not a valid choice.")
	else:	
		print("you selected the " + distribution + " distribution")
		break

while True:
	try:
		stream_length = int(input("How large a stream would you like to use? ") or 100000)
		assert(stream_length>0)
		break
	except: 
		print("not a valid choice")
print("you entered " + str(stream_length))

while True:
	try:
		accuracy = input("Do you want to perform an analysis of the algorithm's accuracy? (yes or no) - Warning: It can be slow ") or "yes"
		assert(accuracy.lower() in ('yes','no'))
		break
	except:
		print("not a valid choice")
print("you said " + accuracy)

## this line functions with kernprof.py to evaluate time performance and with memory_profiler to evaluate memory use
#@profile
def main(item, counters, distribution, stream_length,accuracy):
	## generate random data
	if distribution.lower() == 'uniform':
		data = gen_unif(stream_length)
	if distribution.lower() == 'normal':
		data = gen_norm(stream_length) 	

	## run MG on data
	out = misra_gries(get_items(data),int(counters))
	try:
		estimate = out[item]
	except:
		estimate = 0
	print("The estimated frequency of item " + str(item) + " is: " + str(estimate))

	## accuracy analysis - this is slow	
	if accuracy=='yes':
		frequencies = get_frequencies(data)
		total_error = out['decrements']
		errors = get_errors(out,frequencies[0])
		n_items = frequencies[1]
		max_error = max(errors.values())
		# need if statement for case when there are no errors (more counters than unique items)
		if sum(out.values()) == 0:
			print("All counters have value zero")
		print("the estimate for your item, " + str(item) + ", was low by " + str(errors[item]))
		print("The largest error is " + str(max_error))
		print("The total error across all items is " + str(total_error))
		print("The average error per item is " + str(total_error/n_items))
		test_errors(errors,stream_length,counters)


if __name__ == "__main__":
    main(item, counters, distribution, stream_length,accuracy)