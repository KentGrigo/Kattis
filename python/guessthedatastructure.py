from collections import deque
import heapq

class Bag:
    def __init__(self, name, push, pop):
        self.name = name
        self.isCandidate = True
        self.pushFunc = push
        self.popFunc = pop

    def push(self, value):
        self.pushFunc(value)

    def pop(self):
        try:
            return self.popFunc()
        except IndexError:
            return None

def initializeBags():
    bags = []
    
    stack = []
    bags.append(
        Bag("stack",
        stack.append,
        stack.pop
    ))

    queue = deque()
    bags.append(
        Bag("queue",
            queue.append, 
            queue.popleft
    ))

    priorityQueue = []
    bags.append(
        Bag("priority queue",
            lambda value: heapq.heappush(priorityQueue, -value), 
            lambda: -heapq.heappop(priorityQueue)
    ))

    return bags


while True:
    try:
        numberOfCommands = int(input())
    except EOFError:
        break

    bags = initializeBags()

    for _ in range(numberOfCommands):
        commandType, value = list(map(int, input().split()))
        for bag in bags:
            if not bag.isCandidate:
                continue

            if commandType == 1:
                bag.push(value)
            else:
                result = bag.pop()
                if result != value:
                    bag.isCandidate = False

    candidates = list(filter(lambda bag: bag.isCandidate, bags))
    numberOfCandidates = len(candidates)
    if numberOfCandidates == 0:
        print("impossible")
    elif numberOfCandidates == 1:
        onlyCandidate = candidates[0]
        print(onlyCandidate.name)
    else:
        print("not sure")
