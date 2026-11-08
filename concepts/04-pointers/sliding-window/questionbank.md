# Sliding Window

Keep a contiguous range valid: expand right, shrink left. Use for subarray and substring constraints.

**Prerequisites:** [Two Pointers](../two-pointers/questionbank.md), [Hashmap](../../03-hashmap/questionbank.md)

| Done | # | Problem | Difficulty | Key idea | Solution |
|---|---|---|---|---|---|
| ☐ | 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | Fixed window sum | [C++](0643-maximum-average-subarray-i.cpp) |
| ☐ | 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Jump left past the repeat | [C++](0003-longest-substring-without-repeating-characters.cpp) |
| ☐ | 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | Shrink while valid | [C++](0209-minimum-size-subarray-sum.cpp) |
| ☐ | 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Window minus max frequency | [C++](0424-longest-repeating-character-replacement.cpp) |
| ☐ | 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | Fixed window counts | [C++](0567-permutation-in-string.cpp) |
| ☐ | 438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | Fixed window counts | [C++](0438-find-all-anagrams-in-a-string.cpp) |
| ☐ | 904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | At most two distinct | [C++](0904-fruit-into-baskets.cpp) |
| ☐ | 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | At most k zeros | [C++](1004-max-consecutive-ones-iii.cpp) |
| ☐ | 1248 | [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) | Medium | At most k minus at most k-1 | [C++](1248-count-number-of-nice-subarrays.cpp) |
| ☐ | 992 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Hard | At most k minus at most k-1 | [C++](0992-subarrays-with-k-different-integers.cpp) |
| ☐ | 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Need and have counters | [C++](0076-minimum-window-substring.cpp) |
| ☐ | 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Monotonic deque | [C++](0239-sliding-window-maximum.cpp) |
