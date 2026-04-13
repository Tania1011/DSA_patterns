# Find the First certain number in a sorted boolean array
# nums = [1, 3, 5, 7, 9]
# target = 5
# print(binary_search(nums, target))  # Output: 2
def find_boundary(arr:list[bool])-> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index=mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

if __name__ == "__main__":
    arr = [False, False, False, True, True, True]
    print(f"The boundary index is: {find_boundary(arr)}")

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted numbers: ").split()))
    target = int(input("Enter target: "))
    result = binary_search(nums, target)
    if result != -1:
        print("Found at index:", result)
    else:
        print("Not found")


