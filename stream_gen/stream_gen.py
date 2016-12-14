#generate random data stream
import numpy as np
from numpy import random

# generate data from uniform dist (random integers, this will show worst-case accuracy)
def gen_unif(stream_length):
	unif = random.randint(-500,500,stream_length)
	return(unif)

# generate integers from normal dist with high variance (this will show best case, when items that aren't counted are infrequent)
def gen_norm(stream_length):	
	norm = random.normal(0,100,stream_length).astype(int)
	return(norm)

