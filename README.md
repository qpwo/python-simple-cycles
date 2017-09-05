## Python Simple Cycles

This is an algorithm for finding all the simple cycles in a directed graph.

I've simply modified [networkx][1]'s implementation to use vanilla python, not depending on their special DiGraph structure. [Original implementation.][2]

[1]: https://networkx.github.io/
[2]: https://gist.github.com/qpwo/44b48595c2946bb8f823e2d72f687cd8 

The original paper which described the algorithm:  
Donald B Johnson. "Finding all the elementary circuits of a directed graph." SIAM Journal on Computing. 1975.

### Example

```python
>>> from johnson import simple_cycles
>>> graph = {0: [7, 3, 5], 1: [2], 2: [7, 1], 3: [0, 5], 4: [6, 8], 5: [0, 3, 7], 6: [4, 8], 7: [0, 2, 5, 8], 8: [4, 6, 7]}
>>> print(tuple(simple_cycles(graph)))
([0, 7, 5, 3], [0, 7, 5], [0, 7], [0, 5, 7], [0, 5, 3], [0, 5], [0, 3, 5, 7], [0, 3, 5], [0, 3], [1, 2], [2, 7], [3, 5], [8, 7], [8, 6, 4], [8, 6], [8, 4, 6], [8, 4], [5, 7], [4, 6])
```
