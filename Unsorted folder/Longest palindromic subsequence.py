# abaxyzzyxf

# O(n^2) time | O(1) space
def longestPalindromicSubstring(string):
    currentLongest = [0, 1]

    for i in range(1, len(string)):
        odd = getLongestPalindrome(string, i - 1, i + 1) # Returns a touple
        even = getLongestPalindrome(string, i - 1, i) # Returns a touple

        longest = max(odd, even, key = lambda x: x[1] - x[0])
        
        currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])

    
    return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindrome(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    
    return [left + 1, right] # Because the right part excludes the last element that broke the while loop but left part starts with that index


print(longestPalindromicSubstring("abaxyzzyxf"))

# Nieve approach

def longestPalindromicSubstringNieve(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j + 1] # Because excludes the last element
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
    return longest

def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left < right: # For odd sized strings left and right will cross together
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

print(longestPalindromicSubstringNieve("abaxyzzyxf"))

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(longestPalindromicSubstring("abaxyzzyxf"), "xyzzyx")
    
    def test_case_2(self):
        self.assertEqual(longestPalindromicSubstring("a"), "a")
        
    def test_case_3(self):
        self.assertEqual(longestPalindromicSubstring("it's highnoon"), "noon")

    def test_case_4(self):
        self.assertEqual(longestPalindromicSubstring("noon high it is"), "noon")

    def test_case_5(self):
        self.assertEqual(longestPalindromicSubstring("abccbait's highnoon"), "abccba")
    
    def test_case_6(self):
        self.assertEqual(longestPalindromicSubstring("abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"), "zzzzzzzzzzzzzzzzzzzz")
    
    def test_case_7(self):
        self.assertEqual(longestPalindromicSubstring("abcdefgfedcba"), "abcdefgfedcba")
