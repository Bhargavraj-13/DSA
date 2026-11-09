// 846. Hand of Straights
// https://leetcode.com/problems/hand-of-straights/
// Difficulty: Medium | Topic: Greedy

#include <bits/stdc++.h>
using namespace std;

// Write your solution below this line.

class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size()%groupSize!=0) return false; // size check

        sort(hand.begin(),hand.end());
        unordered_map<int,int> freq;

        for(int h : hand) freq[h]++;

        for(int h : hand){
            if(freq.find(h) != freq.end() && freq[h]!=0){
                for(int i=0;i<groupSize;i++){
                    if(freq.find(h+i) == freq.end() || freq[h+i]==0) return false;
                    else freq[h+i]--;
                }
                // if(freq[h]==0) freq.erase(h);
            }
        }

        return true;
    }
};

/*
Explanation:
  If the number of cards isn't a multiple of groupSize, the cards can't be
  split evenly, so return false straight away.

  Greedy idea: the smallest card left over must start a group, because no
  smaller card exists for it to join. So:
    - Sort the hand and count how many of each card there are (freq).
    - Walk through the cards in ascending order. When a card h still has
      copies left, it is the smallest card left, so build the group
      h, h+1, ..., h+groupSize-1 and use up one copy of each.
    - If any card in that run is missing or used up, the group can't be
      completed, so return false.
  If every group can be built, return true.

  A card with freq 0 was already used by an earlier group, so it is skipped.
  freq.find() is checked before freq[] so that missing cards aren't
  accidentally added to the map with a count of 0.

Complexity:
  Time:  O(n log n) for sorting. Each card is used up once across all
         groups, so building the groups adds only O(n).
  Space: O(n) for the frequency map.

Dry run:
  hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
  9 % 3 == 0, so carry on.
  sorted = [1, 2, 2, 3, 3, 4, 6, 7, 8]
  freq   = {1:1, 2:2, 3:2, 4:1, 6:1, 7:1, 8:1}

  h | freq[h] | action                      | freq after
  --+---------+-----------------------------+------------------------------------
  1 |    1    | build group 1, 2, 3         | {1:0, 2:1, 3:1, 4:1, 6:1, 7:1, 8:1}
  2 |    1    | build group 2, 3, 4         | {1:0, 2:0, 3:0, 4:0, 6:1, 7:1, 8:1}
  2 |    0    | skip (already used)         |
  3 |    0    | skip                        |
  3 |    0    | skip                        |
  4 |    0    | skip                        |
  6 |    1    | build group 6, 7, 8         | all 0
  7 |    0    | skip                        |
  8 |    0    | skip                        |

  Answer: true, with groups [1,2,3], [2,3,4] and [6,7,8].

  hand = [1, 2, 3, 5], groupSize = 2: the group 1, 2 works, but the group
  starting at 3 needs a 4, which is missing, so the answer is false.

Note:
  The solution is my own. I used AI to help write this explanation, so my
  ideas are explained in a clear, standard way that anyone can follow.
*/
