# Minimum Spanning Tree (Prim's and Kruskal's)

Connect all nodes at minimum cost. Prim's grows with a heap; Kruskal's sorts edges with union-find. O(E log V).

**Prerequisites:** [Union-Find (DSU)](../11-union-find/questionbank.md), [Heaps](../../concepts/11-heaps/questionbank.md)

| Done | # | Problem | Difficulty | Key idea | Solution |
|---|---|---|---|---|---|
| ☐ | 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Base form, solve it both ways | [C++](1584-min-cost-to-connect-all-points.cpp) |
| ☐ | 1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | Kruskal-style edge sorting | [C++](1631-path-with-minimum-effort.cpp) |
| ☐ | 778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | Kruskal-style edge sorting | [C++](0778-swim-in-rising-water.cpp) |
| ☐ | 1489 | [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | Hard | Rebuild the MST with and without each edge | [C++](1489-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree.cpp) |
| ☐ | 1697 | [Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) | Hard | Offline queries with sorted edges | [C++](1697-checking-existence-of-edge-length-limited-paths.cpp) |
