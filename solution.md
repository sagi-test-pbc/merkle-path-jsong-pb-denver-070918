
# Merkle Paths


```python
# Merkle Path Example

import math

total_levels = math.ceil(math.log(16, 2))
merkle_path = []
index = 10
for i in range(total_levels):
    merkle_path.append(index)
    index = index // 2
print(merkle_path)
```

### Try it

#### Get the Merkle Path for an item at index 13 (0-base) in 27 items.


```python
import math

num_items = 27
index = 13

# get the total number of levels possible (math.ceil(math.log(num_items, 2)))
num_levels = math.ceil(math.log(num_items, 2))
# initialize merkle path array
merkle_path = []
# loop through number of levels
for _ in range(num_levels):
    # add the index to merkle path
    merkle_path.append(index)
    # index integer div by 2 to get the index at the next level
    index = index // 2
# print merkle path
print(merkle_path)
```

### Test Driven Exercise


```python
def merkle_path(index, total):
    '''Returns a list of indexes up the merkle tree of the node at index if
    there are a total number of nodes'''
    # initialize the path
    path = []
    # calculate number of levels (math.ceil(math.log(total, 2)))
    num_levels = math.ceil(math.log(total, 2))
    # loop through each level
    for _ in range(num_levels):
        # add the index to path
        path.append(index)
        # index becomes integer divide by 2 (use: index = index // 2)
        index = index // 2
    # return the path
    return path
```
