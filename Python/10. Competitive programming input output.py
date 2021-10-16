'''
Competitive programming inputs
'''
# Taking a integer input
n = int(input())
print(type(n), n)

# Taking string input. Python 3 only
string = input()
print(type(string))

'''
Only fixed number of inputs
a b c
1, 2, 3
'''
a, b, c = map(int, input().split())
print(a + b + c)

'''
Integers but not fixed/pre-determined amount
a, b, c, d......
1, 2, 3, 4......
'''
# Using list comprehension
all = [int(i) for i in input().split()]
sum = 0
for i in all:
    sum += i
print(sum)

'''
5
1 2 3 3 5
'''
n = int(input())
arr = [int(i) for i in input().split()]

'''
n
n1
n2
n3

3
44
545
23
'''
n = int(input())
for i in range(n):
    brr = int(input())
print(brr)

'''
T test cases and each has an array:
2
4
1 2 3 4 
6
4 3 1 5 6 2
'''
testCases = int(input())
for i in range(testCases):
    n = int(input())
    arr = [int(idx) for idx in input().split()]
    print(arr)

'''
A matrix such as graph:
4
0 1 2 3
1 0 1 1 
1 1 0 3
1 2 2 0
'''
n = int(input())
for i in range(n):
    arr = [int(idx) for idx in input().split()]