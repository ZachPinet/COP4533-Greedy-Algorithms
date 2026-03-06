# COP4533-Greedy-Algorithms

### Info

Zach Pinet - UFID 5701-3785

To run the program, simply run src/main.py as a Python file. 

Any input files should be placed into inputs/ as a .txt file. Every input file will be run on, and a unique output file (also .txt) will be generated for each.

## Q1: Empirical Comparison

| Input File | k   | m   | FIFO | LRU | OPTFF |
| ---------- | --- | --- | ---- | --- | ----- |
| InputFile1 | 5   | 50  | 39   | 39  | 28    |
| InputFile2 | 10  | 50  | 41   | 41  | 34    |
| InputFile3 | 3   | 50  | 18   | 20  | 14    |

OPTFF does indeed have the fewest misses.
FIFO and LRU are roughly equal.

## Q2: Bad Sequence for LRU or FIFO

My InputFile3 has k = 3 and OPTFF has fewer misses than both FIFO and LRU. OPTFF had 14 misses, while the other two had 18 and 20 misses. OPTFF is a benchmark and so it is always the most optimal.

## Q3: Prove OPTFF is Optimal

If there is an optimal algorithm A, it must have no fewer misses than OPTFF. At any point where A diverges and removes a different element from cache as OPTFF does, either both elements do not appear again, or the two elements will need to be swapped back in again at some point in their respective algorithms. This is because any element swapped out of the cache that appears again must be swapped back in at some point.