## performance analyis (accuracy)
import operator
import numpy as np

# for any item j, estimate f_hat_j satisfies f_j-m/k<=f_hat_j<=f_j
# where m is stream length, k is number of counters

# calculate errors for all items
def get_errors(counters,frequencies):
	keys = [t[0] for t in counters]
	i=0
	error= [0] * len(keys)
	for key in keys:
		error[i] = [t[1] for t in frequencies if t[0]==key][0]-counters[i][1]
		i+=1
	return(error)

def get_frequencies(data):
	unique, counts = np.unique(data,return_counts=True)
	frequencies = list(zip(unique,counts))
	return(frequencies,len(unique))

# maximum error should be less than m/k 
def test_errors(errors,stream_length,counters):
	for error in errors:
		if (error < stream_length/counters):
			continue
		else:
			return False
	print('All errors are smaller than m/k = ' + str(stream_length/counters))

	




