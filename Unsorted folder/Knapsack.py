# O(nc) time | O(nc) space, where n = number of items and c = knapsack capacity
def knapsackProblem(items, capacity):
    knapsackValues = [[0 for column in range(0, capacity + 1)] for row in range(0, len(items) + 1)] # Total items + 1 rows and Total Capacity + 1 columns
    """
    First imagine that you have only one row. You are filling that row with Zeros. Let's say you need 10 Zeros. 
    Here 10 is actually the number of columns in the first row.

    Then we need to multiply 10 columns with 5 rows lets say
    """
    for i in range(1, len(items) + 1): # Because first row is our base case where we don't take any items. Must start from 1 otherwise we will get index out of range error
        currentValue = items[i - 1][0]
        currentWeight = items[i - 1][1]

        for c in range(0, capacity + 1): # If we start from 0 or 1 it doesn't make any difference
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)

    return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues, items):
    sequence = []
    i = len(knapsackValues) - 1
    c = len(knapsackValues[0]) - 1

    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1) # We are only adding indices not the actual items info
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break

    return list(reversed(sequence))