# Bellman-Ford

Relax every edge V-1 times. Handles negative weights and detects negative cycles. O(VE).

> LeetCode has few direct Bellman-Ford problems and no classic negative-cycle one. For that, use CSES [High Score](https://cses.fi/problemset/task/1673) and [Cycle Finding](https://cses.fi/problemset/task/1197).

| Done | # | Problem | Difficulty | Key idea |
|---|---|---|---|---|
| ☐ | 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | K+1 relaxation rounds |
| ☐ | 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Base relaxation practice |
| ☐ | 1334 | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | Run it from every node |
| ☐ | 1928 | [Minimum Cost to Reach Destination in Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) | Hard | Layered relaxation over time |
