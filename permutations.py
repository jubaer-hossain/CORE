def permutations(array):
    permutations = []
    permutationHelper(array, [], permutations)
    return permutations

def permutationHelper(array, currentPermutations, permutations):
    if not len(array) and len(currentPermutations):
        return permutations.append(currentPermutations)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPermutation = currentPermutations + [array[i]]
            permutationHelper(newArray, newPermutation, permutations)
            



def permutationsWithSwap(array):
    permutations = []
    permutationHelper(0, array, permutations)
    return permutations

def permutationWithSwapHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationWithSwapHelper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]




inputArray = [1, 2, 3]
print(permutations(inputArray))