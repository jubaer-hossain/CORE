# Taking input of a graph as a matrix row and columns

nodes = int(input())
graphOne = [[0] * nodes] * nodes
print("The empty graph:", graphOne)

# Taking the graph input
for row in range(nodes):
    for column in range(nodes):
        graphOne[row][column] = int(input())

print("The graph after input:", graphOne);