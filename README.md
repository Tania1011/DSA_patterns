#  Data Structures & Algorithm Patterns for LeetCode

##  Overview
This project contains implementations of common **Data Structures & Algorithms (DSA) patterns** used in coding interviews.  
The goal is to practice problem-solving and improve algorithmic thinking.

---

## 🚀 Implemented Patterns

-  Binary Search  
-  Find Minimum in Rotated Sorted Array  
-  Two Pointers  
-  Sliding Window (Fixed)  
-  Backtracking (Subsets)  
-  Breadth-First Search (BFS)  
-  Hash Map (Two Sum)    

---

##  Implementations & Outputs

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

<p align="center">
  <img src="https://github.com/Tania1011/DSA_patterns/screenshots/binary_search.png" width="400"/>
</p>
---
