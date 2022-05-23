# Bucket sort(frequency) and hashmap for count approach
# O(n) time | O(n) space
def topKFrequent(self, nums, k):
    counts = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        counts[n] = 1 + counts.get(n, 0) # O(n) ST

    for number, count in counts.items(): # O(n) ST
        freq[count].append(number) # Adding each number's frequency

    res = []
    for i in reversed(range(len(nums) + 1)): # O(n) time cause cause we are only traversing at most N frequencies
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


                