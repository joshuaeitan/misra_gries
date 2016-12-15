from collections import Counter

def misra_gries(stream, k):
    counters = Counter()
    for item in stream:
        ## case 1: item already has counter or there are empty counters
        if item in counters or len(counters) < k:
            counters[item] += 1
        ## case 2: item doesn't have counter and there are no empty counters
        else:
            for key in list(counters.keys()):
                counters[key] -= 1
                counters["decrements"]+=1
                if counters[key] == 0:
                    del counters[key]
    return counters

## yield one item to misra-gries at a time to simulate a data stream
def get_items(data):
	for item in data:
		yield item

