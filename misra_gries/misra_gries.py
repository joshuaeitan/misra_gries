from collections import Counter
from pprint import pprint
 
def misra_gries(stream, k):
    counters = Counter()
    for item in stream:
        ## case 1: item already has counter or there are empty counters
        if item in counters or len(counters) < k:
            counters[item] += 1
        ## case 2: item doesn't have counter and there are no empty counters
        else:
            for item in list(counters.keys()):
                counters[item] -= 1
                if counters[item] == 0:
                    del counters[item]
    return counters.most_common(k)

## need to yield one item to misra-gries at a time to simulate a data stream
def get_items(data):
	for item in data:
		yield item

