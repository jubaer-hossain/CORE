"""
Queue in python is a First In First Out(FIFO) data structure. It has primarily two operations.
5 - 13 - 8 - 2 - 10

Enqueue(insert):
After inserting 6 the queue will look like:
5 - 13 - 8 - 2 - 10 - 6

Dequeue(remove/pop):
After removing 5 the queue will look like:
13 - 8 - 2 - 10 - 6
"""
import queue


def queueImplementationUsingList():
    queueUsingList = [5, 13, 8, 2, 10]

    # Enqueue: O(n) Time
    queueUsingList.append(6) # 5 - 13 - 8 - 2 - 10 - 6

    # Dequeue: O(n) Time
    queueUsingList.pop(0) # 13 - 8 - 2 - 10 - 6

    print(f'The final Queue using list is: {queueUsingList}')


"""
Double ended queue. Python built in data structure. Only Deque is iteratable
"""
def deque():
    from collections import deque
    print("\nDEQUE:")

    q = deque()
    
    # Enqueue: O(1) Time
    q.append(5)
    q.append(13)
    q.append(8)
    q.append(2)
    q.append(10)
    print(f'Queue using deque is: {q}') # Queue using deque is: deque([5, 13, 8, 2, 10])

    # Dequeue: O(1) Time
    m = q.popleft() # m = 5
    rightItem = q.pop() # rightItem = 10
    print(m) # 5
    print(f'Right item is {rightItem}')

    print(f'Queue after popping left element and right element: {q}') # Queue after popping left element deque([13, 8, 2])
    print(f'The reversed queue is: {deque(reversed(q))}')
    print(q)
    for idx, value in enumerate(q):
        print(idx, value)
    
    # Some useful deque methods
    q.appendleft(12) # Appends 12 on the left side of the queue
    n = q.count(12) # Returns the number of elements in the queue equal to 12
    
    q.extend([11, 22, 33]) # Adds 3 elements at the end of the queue
    print(q)

    q.extendleft([32, 44, 55]) # Adds 32 to the left, then 44 then 55. -> deque([55, 44, 32, 12, 10, 2, 8, 13, 11, 22, 33])
    print(q)

    arr = list(q) # Converts the queue into list

    idx = q.index(12) # Returns the first match of 12 within the queue
    idxInRange = q.index(12, 0, 8) # Returns the first match of 12 at or after start and before index stop. So here 8 is excluded

    q.remove(12) # Removes the first occurance of 12
    q.rotate(1) # Pushes the queue to 1 in circular order
    q.rotate(-1) # Rotation in backwords


def fifoQueue():
    from queue import Queue
    print("\nFIFO QUEUE:")

    qu = Queue()
    qu.put(12)
    qu.put(13)
    qu.put(14)
    qu.put(115)
    print(qu) # <queue.Queue object at 0x104185790>
    print(qu.qsize())
    print(qu.get()) # 12 Removes and return the last item from the queue
    print(qu.empty()) # False
    print(qu.put_nowait(1222)) # 1222 - 115 - 14 - 13
    print(qu.qsize()) # 4


def lifoQueue():
    from queue import LifoQueue
    print("\nLIFO QUEUE/STACK:")

    stack = LifoQueue()
    stack.put(12)
    stack.put(11)
    stack.pop() # Does the exact same thing as get

    print(f'{stack}')
    print(stack.get())
    print(stack.qsize())


# Driver code
# queueImplementationUsingList()
deque()
fifoQueue()


