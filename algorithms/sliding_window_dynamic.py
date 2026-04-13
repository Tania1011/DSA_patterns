""" Sliding Window (when windows size is not fixed): 
# Find the length of the longest substring with at most K unique characters.
# What is the smallest subarray with a sum greater than a target?
# Return the longest window where a certain rule is valid.

# Find the length of the longest substring of a given string without repeating characters.

# Input: abccabcabcc
# Output: 3
# Explanation: The longest substrings are abc and cab, both of length 3.

# input: aaaabaaa
# Output: 2
# Explanation: ab is the longest substring, with a length of 2
"""


from collections import defaultdict

def longest_substring_without_repeating_characters(s: str) -> int:
    longest = 0   # the maximum longest string 
    l = 0         # marks the start of the sliding window
    counter = defaultdict(int) # keeps a track of how many times a character appears in the sliding window

    for r, char in enumerate(s):
        counter[char] += 1

        while counter[char] > 1:  # duplicate character = if a character appears more than once
            counter[s[l]] -= 1    # fixing window by shrinking the window from the left
            l += 1                # move forward by 1

        longest = max(longest, r - l + 1) # calculate a valid window size, if it large than longest size->update it

    return longest


if __name__ == "__main__":
    s = input("Enter a string: ")
    result = longest_substring_without_repeating_characters(s)
    print("Output:", result)          
        