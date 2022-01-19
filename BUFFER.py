    # O(nc) time | O(nc) space, where n = number of items pairs and c = our total capacity
def knapsackProblem(items, capacity):
    knapsackValues = [[0 for column in range(0, capacity + 1)] for row in range(0, len(items) + 1)]

    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]

        for c in range(0, capacity + 1):
            if currentWeight > c:
                knapsackValues[i][c] = knapsackValues[i - 1][c]
            else:
                knapsackValues[i][c] = max(knapsackValues[i - 1][c], knapsackValues[i - 1][c - currentWeight] + currentValue)
    
    return [knapsackValues[-1][-1], getKnapsackValues(items, knapsackValues)]

def getKnapsackValues(items, knapsackValues):
    sequence = []
    i = len(items) - 1
    c = len(items[0]) - 1

    while i > 0:
        if knapsackValues[i][c] == knapsackValues[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    
    return list(reversed(sequence))