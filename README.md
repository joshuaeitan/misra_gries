# Implementing the Misra-Gries Algorithm for deterministically estimating item frequency in a stream. 

This package generates test data streams from either the normal or uniform distribution, runs the Misra-Gries algorithm on them, and analyzes the algorithm’s performance.

# Usage
The package is built in python 3.5.2, and will not work with python 2. The memory usage analysis requires the memory_profile package as well as the psutil package, and the time line profiler requires the line_profiler package. These can be installed as follows:

pip install -U memory_profiler
pip install psutil
pip install line_profiler

To run the main script with time performance enabled: python kernprof.py -l -v main.py
To run the main script with the memory profiler enabled: python -m memory_profiler main.py

#License
See the LICENSE file for license rights and limitations (MIT).

