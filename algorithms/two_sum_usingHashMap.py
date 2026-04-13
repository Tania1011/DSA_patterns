""" Two Sum
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example: input: nums=[2,7,11,15], target =9 
# Output:[0,1] 
# Explanation: because nums[0] + nums[1] == 9, we return [0,1]
"""


def two_sum(arr: list[int], target: int) -> list[int]:
    num_to_index = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []



if __name__ == "__main__":
    print("Enter numbers separated by space:")
    arr = [int(x) for x in input().split()]
    
    print("Enter target:")
    target = int(input())
    
    result = two_sum(arr, target)
    
    if result:
        print("Output:", result)
    else:
        print("No solution found")
        

    