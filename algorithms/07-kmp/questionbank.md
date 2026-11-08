# KMP

Use the longest proper prefix-suffix table to avoid re-scanning text. O(n + m).

**Prerequisites:** [Strings](../../concepts/02-strings/questionbank.md)

| Done | # | Problem | Difficulty | Key idea | Solution |
|---|---|---|---|---|---|
| ☐ | 28 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | Easy | Base form | [C++](0028-find-the-index-of-the-first-occurrence-in-a-string.cpp) |
| ☐ | 459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | Easy | Period from the LPS table | [C++](0459-repeated-substring-pattern.cpp) |
| ☐ | 796 | [Rotate String](https://leetcode.com/problems/rotate-string/) | Easy | Search in the doubled string | [C++](0796-rotate-string.cpp) |
| ☐ | 686 | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) | Medium | Search in the repeated text | [C++](0686-repeated-string-match.cpp) |
| ☐ | 1367 | [Linked List in Binary Tree](https://leetcode.com/problems/linked-list-in-binary-tree/) | Medium | KMP state during DFS | [C++](1367-linked-list-in-binary-tree.cpp) |
| ☐ | 214 | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | Hard | LPS of s + separator + reverse(s) | [C++](0214-shortest-palindrome.cpp) |
| ☐ | 1392 | [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | Hard | Direct LPS result | [C++](1392-longest-happy-prefix.cpp) |
| ☐ | 3008 | [Find Beautiful Indices in the Given Array II](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/) | Hard | KMP matches plus two pointers | [C++](3008-find-beautiful-indices-in-the-given-array-ii.cpp) |
