""" Fixed Size Sliding Window
# Given an array(list) nums =[1, 2, 3, 7, 4, 1], k=3, then the output would be 14 as the largest length 3 
# subarray sum is given by [3,7,4] which sums to 14.

# Find the maximum average of any subarray of size k. Return the sum of every k-length block.
# Find the subarray of length k with the largest/smallest X.

# Example: input: 0 1 2 3 4
# Output: 2
# Explanation: If the number of nodes is even, then return the second middle node.
# input: 0 1 2 3 4 5
# Output: 3
"""




def sliding_window_fixed(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for right in range(k, len(nums)):
        left = right - k
        window_sum += nums[right] - nums[left]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Enter window size: "))

    result = sliding_window_fixed(nums, k)

    print("Output:", result)          
        