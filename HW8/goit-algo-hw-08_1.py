import heapq


def merge_k_lists(sorted_lists):
    # Merge k sorted_lists in one sorted_list
    # :param sorted_lists: List of k sorted_lists
    # :return: One sorted_list

    # minimum_heap

    heap = []

    # Initialize of heap: add fist elements from each list

    for i, sorted_list in enumerate(sorted_lists):
        if sorted_list:  # Check if the list is empty
            heapq.heappush(
                heap, (sorted_list[0], i, 0)
            )  # value, index of list, index of element

    result = []

    # Add mim elements from each lists
    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        result.append(value)

        # if list has an element, add next into the heap
        if element_index + 1 < len(sorted_lists[list_index]):
            next_value = sorted_lists[list_index][element_index + 1]
            heapq.heappush(heap, (next_value, list_index, element_index + 1))
    return result


sorted_lists = [
    [2, 5, 17, 28, 96, 99],
    [1, 2, 63, 78],
    [17, 32, 48, 64, 99]]

merged_list = merge_k_lists(sorted_lists)
print(f"Merged sorted list: {merged_list}")
