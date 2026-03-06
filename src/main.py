from pathlib import Path
from collections import deque


# This reads an input file to extract its values.
def read_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    # The first line gets k and m.
    k, m = map(int, lines[0].strip().split())
    
    # The second line gets all the requests.
    reqs = list(map(int, lines[1].strip().split()))
    
    return k, m, reqs


# This is the First-In, First-Out policy.
def fifo(k, reqs):
    cache = deque()
    cache_set = set()
    misses = 0
    
    for req in reqs:
        # Check set for req because deque is not iterable.
        if req in cache_set:
            continue
        else:
            misses += 1
            if len(cache) < k:
                cache.append(req)
                cache_set.add(req)
            # Remove the first req in the cache.
            else:
                evicted = cache.popleft()
                cache_set.remove(evicted)
                cache.append(req)
                cache_set.add(req)
    
    return misses


# This is the Least Recently Used policy.
def lru(k, reqs):
    lru_dict = {}
    misses = 0

    for req in reqs:
        # Increment each value by 1.
        for r in lru_dict:
            lru_dict[r] += 1

        # Set existing pair's value back to 0.
        if req in lru_dict:
            lru_dict[req] = 0
            continue
        else:
            misses += 1
            if len(lru_dict) < k:
                lru_dict[req] = 0
            # Remove the pair with the highest value.
            else:
                lru_key = max(lru_dict, key=lambda k: lru_dict[k])
                lru_dict.pop(lru_key)
                lru_dict[req] = 0
    
    return misses


# This is the main function.
def main():
    cwd = Path.cwd()
    inputs_dir = cwd / 'inputs'
    outputs_dir = cwd / 'outputs'
    
    # Run the eviction policies on each input file.
    for input_file in sorted(inputs_dir.glob('*.txt')):
        
        k, m, reqs = read_file(input_file)
        fifo_misses = fifo(k, reqs)
        lru_misses = lru(k, reqs)

        # Create a new output file for each input file.
        output_file = outputs_dir / f'{input_file.name[:-4]}_output.txt'
        with open(output_file, 'w') as f:
            f.write(f"FIFO  : {fifo_misses}\n")
            f.write(f"LRU   : {lru_misses}\n")


if __name__ == "__main__":
    main()