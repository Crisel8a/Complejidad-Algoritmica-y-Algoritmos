# using two pointers to check if a string is a palindrome
def isPalindrome(s):
    left = 0
    right = len(s) - 1

    # Continue looping while the two pointers
    # have not crossed
    while left < right:
        # If the characters at the current positions
        # are not equal
        if s[left] != s[right]:
            return False

        # Move the left pointer to the right and
        # the right pointer to the left
        left += 1
        right -= 1

    # If no mismatch is found, return True (palindrome)
    return True


s = "abba"
print(isPalindrome(s))
