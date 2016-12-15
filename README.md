# Implementing the Misra-Gries Algorithm for deterministically estimating item frequency in a stream. 

This package generates test data streams from either the normal or uniform distribution, runs the Misra-Gries algorithm on them, and analyzes the algorithm’s performance.

# Usage
The package is built in python 3.5.2, and will not work with python 2. The memory usage analysis requires the memory_profile package as well as the psutil package, and the time line profiler requires the line_profiler package. These can be installed as follows:

pip install -U memory_profiler  
pip install psutil  
pip install line_profiler  

To run with either the time or space line profiler enabled, the @profile signature must be active (it is currently commented out):

To run the main script with time performance enabled: python kernprof.py -l -v main.py  
To run the main script with the memory profiler enabled: python -m memory_profiler main.py  

# Space Usage Analysis:

Unfortunately, the memory_profiler package I used is not incredibly accurate, as the results vary by a relatively large amount each run (even when I know for certain that all of the counters are non-empty). However, it is definitely adequate for my purposes. I did 5 test runs for each set of parameters and averaged the results, in order to control for the variation a bit, but ideally I would have done more runs or found a more accurate way to measure the space usage. 

It seems that stream length only matters for memory usage in that it implicitly determines how many unique items appear in the stream. This is why  the amount of space used for 100000 counters with 100000 stream length is significantly smaller than for 100000 counters with 1000000 stream length, even though theoretically it should only be slightly smaller: when we only sample 100000 items for the stream, there are significantly fewer than 100000 unique items, which results in a lot of potential counters which never get filled. 

There are some fluky results (memory usage increases significantly in relative terms with stream length for k=100 counters), which I attribute to either empty counters or just variability and accuracy limitations with memory_profiler. For the most part, space usage increases only slightly with stream length, as it should, and the number of counters is the main determinant of the space usage.

The theoretical space usage of the Misra-Gries algorithm is O(k(log m + log n))). The data universe I sampled from for the test runs is [-50000,50000]. Since the sign is important, items in the data universe take up to 17 bits to represent (log n <= 17). In my testing runs, the size of the data stream, m, ranges from 1e5 to 1e6, thus log m ranges from 17 to 20. Finally, in my testing runs the number of counters, k, ranges from 1e2 to 1e5. Thus, theoretically, the space usage should be O(3400-3.7 million bits). In fact, it ranges from ~13000 to ~22.5 million bits, off by a factor of 4 on the low end, and a factor of ~6 on the higher end. As the factor by which the space usage differs from the theoretical value is not constant, it seems this implementation is not optimal, but it is pretty close. It would be interesting to compare it to the space usage of the optimized Java library, but unfortunately I couldn?t figure out how to get the Java library to do what I wanted (I do not have much experience with Java).

![Theoretical vs. Observed space usage, m=100000](https://github.com/joshuaeitan/misra_gries/blob/master/m%3D100000.png)
![Theoretical vs. Observed space usage, m=500000](https://github.com/joshuaeitan/misra_gries/blob/master/m%3D500000.png)
![Theoretical vs. Observed space usage, m=1000000](https://github.com/joshuaeitan/misra_gries/blob/master/m%3D1000000.png)

#License
See the LICENSE file for license rights and limitations (MIT).

