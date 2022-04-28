# O(n) time | O(n) space
class Solution(object):
    def isPalindrome(self, s):
        newStr = ""

        for char in s:
            if char.isalnum(): # checks if a character is alpha numeric
                newStr += char.lower() # converts a character to lowercase

        return newStr == newStr[::-1] # O(n) space

# Approach-2: Two pointers
# O(n) time | O(1) space
class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True

    # Determines if a character is alpha numeric
    def alphaNum(self, char):
        return(ord('A') <= ord(char) <= ord('Z') or
               ord('a') <= ord(char) <= ord('z') or
               ord('0') <= ord(char) <= ord('9'))

        