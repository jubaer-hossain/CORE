'''
Recursive approach that returns a new reversed string
Time: O(N)
Space: O(N) -> Because of the recursive call stack
'''
def reverseStringRecursive(word):
    if len(word) == 1:
        return word
    return reverseStringRecursive(word[1:]) + word[0]

'''
Recursive call stack for the word "Input":
Call 1 -> reverseStringRecursive("Input") -> 👆Returns: "tupn" + "I". Which is the last paused function call on the call stack.
    Call 2 -> reverseStringRecursive("nput") -> 👆Returns: "tup" + "n". Takes "tup" and adds "n" and returns "tupn" to Call 1
        Call 3 -> reverseStringRecursive("put") -> 👆Returns: "tu" + "p". Takes "tu" and adds "p" and returns "tup" to Call 2
            Call 4 -> reverseStringRecursive("ut") -> 👆Returns: "t" + "u". Takes "t" and adds "u" and returns "tu" to Call 3
                Call 5 -> reverseStringRecursive("t") -> 👆Returns "t" to Call 4 because length of string "t" is 1 which is Base Case
'''

print(reverseStringRecursive("Input"))

'''
In place swapping of the characters using recursive approach.
Time: O(N)
Space: O(N) -> In place but still takes N memory because of the recursive call stack
'''
def reverseStringRecursiveInPlace(word):
    def swapHelper(left, right, string):
        if left < right:
            string[left], string[right] = string[right], string[left]
            swapHelper(left + 1, right - 1, string)

    swapHelper(0, len(word) - 1, word)

'''
Iterative approach with two pointers and in place swap.
Time: O(N)
Space: O(1)
'''
def reverseStringIterative(word):
    left, right = 0, len(word) - 1
    while left < right: # Because we never need to swap the very middle character
        word[left], word[right] = word[right], word[left]
        left, right = left + 1, right - 1
        