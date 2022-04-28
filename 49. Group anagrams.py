# O(N * K * logK) time | O(N * K) Space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        result = defaultdict(list)

        for string in strs:
            result[tuple(sorted(string))].append(string)
        
        return result.values()


# O(n * k + n * 26) time | O(n * k + n * 26) space
# O(NK) time | O(NK) space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections

        result = collections.defaultdict(list) # (list) means the default value is lists. Will raise a key error if it's empty. n * a space

        for string in strs: # O(n) time
            
            charCount = [0] * 26 # Initializing 0 for all letters. n * a = 26 space time

            for char in string: # O(n * k) time
                charCount[ord(char) - ord("a")] += 1 # Getting ASCII value. c = 99 - a = 97 => 2 idx in array and increasing that idx by 1
            
            result[tuple(charCount)].append(string)
        
        return result.values() # Only list of values [["bat"],["nat","tan"],["ate","eat","tea"]]

