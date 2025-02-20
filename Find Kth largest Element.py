import heapq

def kth_largest(ele, k):  # Added 'k' as a parameter
    max_heap = []

    for e in ele:
        heapq.heappush(max_heap, -e)  # Using negative values to simulate a max heap

    for _ in range(k-1):  # Remove (k-1) largest elements
        heapq.heappop(max_heap)

    return -heapq.heappop(max_heap)  # Return the kth largest element

elements = [10, 34, 64, 90, 83, 70, 6]
k = 2  # Example: Finding the 1st largest element

print('kth Largest element is', kth_largest(elements, k))
