""" Valid Palindrome
Given a string s, determine if it is a palindrome considering only alphanumeric characters and ignoring cases.
Example: 
Input: s="A man,  a plan, a canal: Panama"
Output: true
Explanation: After removing non=alphanumeric characters, it 

Input: s= "race a car"
Output: false
Explanation: After removing non-alphanumeric characters, it 
"""

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum(): # Note 1, 2
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower(): # ignore case
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    s = input("Enter string: ")

    result = is_palindrome(s)

    print("Output:", "true" if  result else "false")