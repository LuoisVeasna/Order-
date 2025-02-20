
import heapq

def heap_sort(elements):
    heapq.heapify(elements)
    sorted_list = []

    for _ in range(len(elements)):  # Use underscore (_) for unused loop variable
        x = heapq.heappop(elements)
        sorted_list.append(x)

    return sorted_list  # Return sorted list

elements = [12, 14, 8, 7, 3, -5, 6, 2]
sorted_elements = heap_sort(elements)  # Store the sorted result

print('Sorted List is', sorted_elements)  # Print the correct variable
