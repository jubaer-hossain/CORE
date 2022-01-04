from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # the offsets in the eight directions
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        def bfs(x, y):
            visited = set()
            queue = deque([(0, 0)])
            steps = 0

            while queue:
                curr_level_cnt = len(queue)
                # iterate through the current level
                for i in range(curr_level_cnt):
                    curr_x, curr_y = queue.popleft()
                    if (curr_x, curr_y) == (x, y):
                        return steps

                    for offset_x, offset_y in offsets:
                        next_x, next_y = curr_x + offset_x, curr_y + offset_y
                        if (next_x, next_y) not in visited:
                            visited.add((next_x, next_y))
                            queue.append((next_x, next_y))

                # move on to the next level
                steps += 1

        return bfs(x, y)

def minKnightMoves(x: int, y: int) -> int:
    # Knight moves: total 8 moves
    offsets = [(1, 2), (2, 1), (1, -2), (2, -1)]
               (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
    
    def bfs(x, y):
        queue = deque([(0, 0)])
        visited = set()
        steps = 0

        while queue:
            currentLength = len(queue)

            for i in range(currentLength):
                curr_x, curr_y = queue.popleft()
                if (curr_x, curr_y) == (x, y):
                    return steps
                
                for offset_x, offset_y in offsets:
                    next_x, next_y = curr_x + offset_x, curr_y + offset_y
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))

            steps += 1
    return bfs(x, y)

def minKnightMoves(x: int, y: int) -> int:
    # Knight moves: total 8 moves
    offsets = [(1, 2), (2, 1), (1, -2), (2, -1),
               (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
    
    startRow, startCol = getRowCol(x)
    endRow, endCol = getRowCol(y)
    
    def bfs(startRow, startCol, endRow, endCol):
        queue = deque([(startRow, startCol)])
        visited = set()
        steps = 0

        while queue:
            currentLength = len(queue)

            for i in range(currentLength):
                curr_x, curr_y = queue.popleft()
                if (curr_x, curr_y) == (endRow, endCol):
                    return steps
                
                for offset_x, offset_y in offsets:
                    next_x, next_y = curr_x + offset_x, curr_y + offset_y
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))

            steps += 1
    return bfs(startRow, startCol, endRow, endCol)

def getRowCol(x):
    cnt = 0
    board = {}
    for i in range(8):
        for j in range(8):
            board[cnt] = (i, j)
            cnt += 1
    
    row, col = board[x]
    #print(board)
    return row, col


print(minKnightMoves(0, 1))
print(minKnightMoves(19, 36))

getRowCol(1)












def solution(x, y):
    # Knight moves: total 8 moves
    offsets = [(1, 2), (2, 1), (1, -2), (2, -1),
               (-1, -2), (-2, -1), (-1, 2), (-2, 1)]
    
    cnt = 0
    board = {}
    for i in range(8):
        for j in range(8):
            board[cnt] = (i, j)
            cnt += 1
    
    startRow, startCol = board[x]
    endRow, endCol = board[y]
    
    def bfs(startRow, startCol, endRow, endCol):
        queue = deque([(startRow, startCol)])
        visited = set()
        steps = 0

        while queue:
            currentLength = len(queue)

            for i in range(currentLength):
                curr_x, curr_y = queue.popleft()
                if (curr_x, curr_y) == (endRow, endCol):
                    return steps
                
                for offset_x, offset_y in offsets:
                    next_x, next_y = curr_x + offset_x, curr_y + offset_y
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))

            steps += 1
    return bfs(startRow, startCol, endRow, endCol)

# def getRowCol(x):
#     cnt = 0
#     board = {}
#     for i in range(8):
#         for j in range(8):
#             board[cnt] = (i, j)
#             cnt += 1
    
#     row, col = board[x]
#     #print(board)
#     return row, col

print(solution(0, 1))