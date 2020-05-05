class MinHeap:
    def swap(self, a: int, b: int) -> None:
        tmp = self.queue[a]
        self.queue[a] = self.queue[b]
        self.queue[b] = tmp
        
    def get_size(self) -> int:
        return self.next_index - 1

    def push(self, val: int) -> None:
        # print(self.queue)
        if self.next_index == len(self.queue) + 1:
            return
        cur_index = self.next_index
        self.queue[cur_index] = val
        prev_index = cur_index
        cur_index = int(cur_index / 2)
        while cur_index >= 1:
            if self.queue[cur_index] <= val:
                break
            self.swap(cur_index, prev_index)
            prev_index = cur_index
            cur_index = int(cur_index / 2)
        self.next_index += 1

    def pop(self) -> int:
        # print(self.queue)
        if self.next_index <= 1:
            return -1
        ret_val = self.queue[1]
        last_item = self.queue[self.next_index - 1]
        self.queue[1] = last_item
        cur_index = 1
        self.next_index -= 1
        while cur_index * 2 < self.next_index:
            if self.queue[cur_index * 2] >= last_item and (self.next_index == cur_index * 2 + 1 or self.queue[cur_index * 2 + 1] >= last_item):
                break
            elif self.queue[cur_index * 2] < self.queue[cur_index * 2 + 1] or self.next_index == cur_index * 2 + 1:
                self.swap(cur_index, cur_index * 2)
                cur_index = cur_index * 2
            else:
                self.swap(cur_index, cur_index * 2 + 1)
                cur_index = cur_index * 2 + 1
        return ret_val
                
    def peek(self) -> int:
        if self.next_index <= 1:
            return -1
        return self.queue[1]
        
    def __init__(self, capacity):
        self.queue = [0] * (capacity + 1)
        self.next_index = 1
        self.size = 0
        
        
if __name__ == "__main__":
    heap = MinHeap(10)
    heap.push(3)
    heap.push(1)
    heap.push(5)
    heap.push(2)
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())