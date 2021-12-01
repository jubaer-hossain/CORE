
def longestPeak(array):
    peaks = []
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks.append(i)
    length = 0
    right = 0
    left = 0
    i = 0
    while i < len(peaks):
        idx = peaks[i]
        for r in range(idx + 1, len(array)):
            if array[r] < array[r - 1]:
                right += 1
            else:
                break

        for l in reversed(range(0, idx)):
            if array[l] < array[l + 1]:
                left += 1
            else:
                break

        length = max(left + right + 1, length)
        left = 0
        right = 0
        i += 1

    return length

import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(longestPeak(array), expected)
    
    def test_case_2(self):
        array = []
        expected = 0
        self.assertEqual(longestPeak(array), expected)
    
    def test_case_3(self):
        array = [1, 3, 2]
        expected = 3
        self.assertEqual(longestPeak(array), expected)