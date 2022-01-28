"""Heap is a special tree structure in which each parent node is less than or equal to its child node.
 Then it is called a Min Heap. If each parent node is greater than or equal to its child node then
  it is called a max heap. It is very useful is implementing priority queues where the queue item with
   higher weightage is given more priority in processing."""
# create heap
import heapq

H = [21, 1, 45, 78, 3, 5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

# insert into heap
import heapq

H = [21, 1, 45, 78, 3, 5]
# Covert to a heap
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H, 8)
print(H)

# Remove element from the heap
heapq.heappop(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)
