# O(n) time | O(1) space
def hasSingleCycle(array):
    START_IDX = 0
    currentIdx = START_IDX

    numElementsVisited = 0

    # 1. We run the loop until we visited EXACTLY N elements
    while numElementsVisited < len(array):

        # 2. This one line checks if the array has multiple cycle or broken single cycle where there is a cycle but we never visit certain elements
        if numElementsVisited > 0 and currentIdx == START_IDX:
            return False

        # 3. Increase elements visited and get nextIdx
        numElementsVisited += 1
        nextIdx = getNextIdx(currentIdx, array)

        # 4. Update currentIdx
        currentIdx = nextIdx

    # 5. Finally we need to check if we are at START when we broke out of the loop
    return currentIdx == START_IDX


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]

    nextIdx = (currentIdx + jump) % len(array)

    # i = 0, 1, 2, 3, 4
    #  [-6, 2, 3, 4, 5] Basically an array of len 5 has the last idx at i = 4. So if nextIdx = -1 then it means its the last idx of the array. So we can get that by adding the negative idx with the len of the array
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
        


