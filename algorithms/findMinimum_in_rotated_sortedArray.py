# Find Minimum in Rotated Sorted Array = Find the First True in a Sorted Boolean Array
# A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. 
# Find the index of the minimum element in this array.
# Input: [30, 40, 50, 10, 20]
# Output: 3
# Explanation: the smallest element is 10, and its index is 3.iter
# Input: [3, 5, 7, 11, 13, 17, 19, 2]
# Output: 7
# Explanation: The smallest element is 2. and its index is 7.

def find_min_rotated(arr:list[int])-> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        # if <= last element, then belongs to lower half
        if arr[mid]<=arr[-1]:
            boundary_index=mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

if __name__ == "__main__":  
    arr = [4, 5, 3, 7, 0, 1, 2]
    print(f"The minimum element in the rotated sorted array is: {arr[find_min_rotated(arr)]}")
    