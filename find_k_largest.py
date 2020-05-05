from min_heap import MinHeap
from heapq import heappush, heappop
import sys

def findMaxK(vals, k):
    minHeap = MinHeap(k)
    for n in vals:
        if minHeap.get_size() < k:
            minHeap.push(n)
        elif minHeap.peek() < n:
            minHeap.pop()
            minHeap.push(n)
    while minHeap.get_size() > 0:
        print(minHeap.pop())
        
def findMaxK2(vals, k):
    queue = []
    for n in vals:
        if len(queue) < k:
            heappush(queue, n)
        elif queue[0] < n:
            heappop(queue)
            heappush(queue, n)
    while len(queue) > 0:
        print(heappop(queue))
            

if __name__ == "__main__":
    vals = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    vals = vals.split(' ')
    vals = [int(x) for x in vals]
    print(vals)
    print("k = " + str(k))
    findMaxK(vals, k)
    