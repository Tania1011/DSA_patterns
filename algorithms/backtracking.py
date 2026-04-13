# Backtracking Algorithm: Subsets
# Time Complexity: O(2^n)

def find_subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop() # Backtrack step

    backtrack(0, [])
    return result

# Data for CLI Display
numbers = [1, 2, 3]
print(f"Generating all subsets for: {numbers}")
subsets = find_subsets(numbers)
print(f"Total subsets: {len(subsets)}")
print(f"Subsets: {subsets}")