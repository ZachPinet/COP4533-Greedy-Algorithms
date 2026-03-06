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
    cache = {}
    misses = 0

    for req in reqs:
        # Increment each value by 1.
        for r in cache:
            cache[r] += 1

        # Set existing pair's value back to 0.
        if req in cache:
            cache[req] = 0
            continue
        else:
            misses += 1
            if len(cache) < k:
                cache[req] = 0
            # Remove the pair with the highest value.
            else:
                lru_key = max(cache, key=lambda k: cache[k])
                cache.pop(lru_key)
                cache[req] = 0
    
    return misses


# This is Belady's Farthest-in-Future policy.
def optff(k, reqs):
    # Store the positions of all requests.
    all_pos_dict = {}
    i = 0
    for req in reqs:
        if req in all_pos_dict:
            all_pos_dict[req].append(i)
        else:
            all_pos_dict[req] = [i]
        i += 1

    cache = set()
    misses = 0
    i = 0
    for req in reqs:
        if req in cache:
            i += 1
            continue
        else:
            misses += 1
            if len(cache) < k:
                cache.add(req)
            # Find the req with the highest next pos after i.
            else:
                curr_evicted = None
                curr_max = i
                for r in cache:
                    has_future_pos = False
                    for j in all_pos_dict[r]:
                        # Find the first position after i.
                        if j > i:
                            if j > curr_max:
                                curr_evicted = r
                                curr_max = j
                            has_future_pos = True
                            break
                    
                    # If no position after i, select r for removal.
                    if has_future_pos == False:
                        curr_evicted = r
                        break

                # Remove the request from the cache.
                cache.remove(curr_evicted)
                cache.add(req)

            i += 1

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
        optff_misses = optff(k, reqs)

        # Create a new output file for each input file.
        output_file = outputs_dir / f'{input_file.name[:-4]}_output.txt'
        with open(output_file, 'w') as f:
            f.write(f"FIFO  : {fifo_misses}\n")
            f.write(f"LRU   : {lru_misses}\n")
            f.write(f"OPTFF : {optff_misses}")


if __name__ == "__main__":
    main()