#!/bin/sh
python kernprof.py -l -v main.py 200 500
python  -m memory_profiler main.py 200 500