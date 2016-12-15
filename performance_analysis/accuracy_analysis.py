## performance analyis (accuracy)
import operator
import numpy as np
from collections import Counter

# for any item j, estimate f_hat_j satisfies f_j-m/k<=f_hat_j<=f_j
# where m is stream length, k is number of counters

# calculate error for each items
def get_errors(counters,frequencies):
	items = [t[0] for t in frequencies]
	counted = list()
	for key in list(counters.keys()):
		if key =='decrements':
			continue
		counted.append(key)
	uncounted = [item for item in items if item not in counted]
	errors = Counter()
	## errors for items that don't have counters are their actual frequencies
	for item in uncounted:
		errors[item]+=[t[1] for t in frequencies if t[0] == item][0]
	for item in counted:
		errors[item]+=[t[1] for t in frequencies if t[0] == item][0]-counters[item]
		return(errors)

def get_frequencies(data):
	unique, counts = np.unique(data,return_counts=True)
	frequencies = list(zip(unique,counts))
	return(frequencies,len(unique))

# maximum error should be less than m/k 
def test_errors(errors,stream_length,counters):
	for error in errors.values():
		if (error < stream_length/counters):
			continue
		else:
			return False
	print('All errors are smaller than m/k = ' + str(stream_length/counters))

