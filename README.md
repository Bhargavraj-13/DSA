# DSA Roadmap

Work through the concepts in order, since each one builds on earlier ones. The algorithms table shows when to start each one.

## Concepts

| Topic | Focus | Questions |
|---|---|---|
| [Arrays](concepts/01-arrays/questionbank.md) | In-place updates, running state, matrix traversal and interval handling. | 14 |
| [Strings](concepts/02-strings/questionbank.md) | Character counting, parsing, palindromes and building output efficiently. | 14 |
| [Hashmap](concepts/03-hashmap/questionbank.md) | Constant-time lookup, frequency counting and storing what you have already seen. | 13 |
| [Two Pointers](concepts/04-pointers/two-pointers/questionbank.md) | Move two indices with a rule that safely discards options. Usually needs sorted or symmetric input. | 12 |
| [Sliding Window](concepts/04-pointers/sliding-window/questionbank.md) | Keep a contiguous range valid: expand right, shrink left. Use for subarray and substring constraints. | 12 |
| [Binary Search](concepts/05-binary-search/questionbank.md) | Search sorted data, or binary search the answer when feasibility is monotonic. | 12 |
| [Stacks and Queues](concepts/06-stacks-and-queues/questionbank.md) | Nested structure, last-unresolved state and monotonic stacks for next greater or smaller problems. | 13 |
| [Linked Lists](concepts/07-linked-lists/questionbank.md) | Pointer rewiring, dummy heads and fast and slow pointers. | 13 |
| [Recursion](concepts/08-recursion/questionbank.md) | Base cases, trusting the smaller call and reasoning about the call stack. | 11 |
| [Backtracking](concepts/09-backtracking/questionbank.md) | Choose, explore, undo. Prune early and handle duplicates deliberately. | 13 |
| [Trees](concepts/10-trees/questionbank.md) | Binary tree recursion, BST ordering, construction and values returned from subtrees. | 15 |
| [Heaps](concepts/11-heaps/questionbank.md) | Repeated access to the smallest or largest item, and the top k pattern. | 10 |
| [Tries](concepts/12-tries/questionbank.md) | Prefix trees for shared prefixes, dictionary search and bitwise XOR queries. | 8 |
| [DFS](concepts/13-dfs/questionbank.md) | Go deep first using recursion or a stack. Covers tree paths, grids and reachability. | 13 |
| [BFS](concepts/14-bfs/questionbank.md) | Explore level by level. Finds shortest paths in unweighted graphs and grids. | 13 |
| [Graphs](concepts/15-graphs/questionbank.md) | Modelling problems as nodes and edges: traversal, cycles, ordering and connectivity. | 13 |
| [Greedy](concepts/16-greedy/questionbank.md) | Commit to the locally best choice, and be able to argue why it stays safe. | 12 |
| [Dynamic Programming](concepts/17-dp/questionbank.md) | Define state, write the transition, then choose memoisation or tabulation. | 15 |
| [Bit Manipulation](concepts/18-bit-manipulation/questionbank.md) | XOR properties, masks, shifts and counting bits per position. | 12 |
| [Math](concepts/19-math/questionbank.md) | Number properties, modular reasoning, overflow and geometry. | 13 |

## Algorithms

Some problems appear in both a concept and an algorithm list because they can be practised either way.

| Topic | Start after | Focus | Questions |
|---|---|---|---|
| [Kadane's Algorithm](algorithms/01-kadane/questionbank.md) | Arrays | Best subarray ending here: extend it or restart. O(n) time, O(1) space. | 8 |
| [Prefix Sum and Difference Array](algorithms/02-prefix-sum-difference-array/questionbank.md) | Hashmap | O(n) preprocessing for O(1) range sums, and O(1) range updates applied in one final pass. | 8 |
| [Boyer-Moore Voting](algorithms/03-boyer-moore-voting/questionbank.md) | Arrays | Cancel out differing votes to find majority candidates. O(n) time, O(1) space, then verify. | 4 |
| [Merge Sort](algorithms/04-merge-sort/questionbank.md) | Recursion | Divide, sort, merge. O(n log n) and stable. The merge step can also count pairs. | 5 |
| [Quick Sort and Quickselect](algorithms/05-quick-sort-quickselect/questionbank.md) | Recursion | Partition around a pivot. Average O(n log n) to sort and average O(n) to select the kth item. | 6 |
| [Floyd's Cycle Detection](algorithms/06-floyd-cycle-detection/questionbank.md) | Linked Lists | Slow and fast pointers meet inside a cycle, then a reset finds its entry. O(n) time, O(1) space. | 5 |
| [KMP](algorithms/07-kmp/questionbank.md) | Strings | Use the longest proper prefix-suffix table to avoid re-scanning text. O(n + m). | 8 |
| [Rabin-Karp](algorithms/08-rabin-karp/questionbank.md) | Strings and Hashmap | Rolling hash for fast substring comparison. Expected O(n + m). Watch for collisions. | 6 |
| [Z-Algorithm](algorithms/09-z-algorithm/questionbank.md) | KMP | Z[i] is the longest match between the string and its suffix at i. O(n). | 4 |
| [Manacher's Algorithm](algorithms/10-manacher/questionbank.md) | Strings | Reuse mirrored palindrome radii to find all palindromes. O(n). | 4 |
| [Union-Find (DSU)](algorithms/11-union-find/questionbank.md) | Graphs | Near-constant merge and find with path compression and union by rank or size. | 9 |
| [Topological Sort](algorithms/12-topological-sort/questionbank.md) | Graphs | Order a DAG with Kahn's in-degree BFS or DFS finishing order. O(V + E). | 7 |
| [Dijkstra's Algorithm](algorithms/13-dijkstra/questionbank.md) | Graphs and Heaps | Single-source shortest paths with non-negative weights. O(E log V) with a heap. | 8 |
| [Bellman-Ford](algorithms/14-bellman-ford/questionbank.md) | Dijkstra's Algorithm | Relax every edge V-1 times. Handles negative weights and detects negative cycles. O(VE). | 4 |
| [Floyd-Warshall](algorithms/15-floyd-warshall/questionbank.md) | Bellman-Ford | All-pairs shortest paths by trying each node as an intermediate. O(V^3). | 5 |
| [Minimum Spanning Tree (Prim's and Kruskal's)](algorithms/16-mst-prim-kruskal/questionbank.md) | Union-Find and Heaps | Connect all nodes at minimum cost. Prim's grows with a heap; Kruskal's sorts edges with union-find. O(E log V). | 5 |
| [Tarjan's Algorithm](algorithms/17-tarjan-bridges-scc/questionbank.md) | Graphs | Use discovery and low-link times to find bridges, articulation points and SCCs. O(V + E). | 4 |
| [Segment Tree and Fenwick Tree](algorithms/18-segment-tree-fenwick/questionbank.md) | Trees | Range queries with point or range updates. O(log n) per operation. | 8 |
| [Sieve of Eratosthenes and Euclid's GCD](algorithms/19-sieve-and-gcd/questionbank.md) | Math | Generate primes in O(n log log n), and compute GCD in O(log min(a, b)). | 8 |
