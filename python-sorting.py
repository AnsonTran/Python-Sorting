def list_swap(obj_list, index1, index2):
    '''(list of obj, int, int) -> None
    Swaps items at <index1> and <index2> of <obj_list>.
    REQ: 0 <= index1 < len(int_list)
         0 <= index2 < len(int_list)
    >>> int_list = [0, 678, 0, 0, 321, 0]
    >>> list_swap(int_list, 4, 1)
    >>> int_list
    [0, 321, 0, 0, 678, 0]
    '''
    if index1 != index2:
        # Determine which indice is smaller/larger
        (min_index, max_index) = (index1, index2) if index1 < index2 else (index2, index1)
        # Remove the objects at those indices
        (min_obj, max_obj) = (obj_list.pop(min_index), obj_list.pop(max_index-1))
        # Swap objects in the list
        obj_list.insert(min_index, max_obj)
        obj_list.insert(max_index, min_obj)


def bubble_sort(obj_list):
    '''(list of objs) -> None
    Performs a bubble sort on a list. Stops passing through the list if there
    are no swaps being made.
    '''
    swap = True
    # list from [i:] is already sorted with largest objs
    i = len(obj_list)
    # Performs n passes, stopping if there are no swaps made or i reaches 0
    while i > 0 and swap:
        swap = False
        for j in range(i):
            # Compare adjacent objects, swap if first is greater than
            # second
            if obj_list[j] > obj_list[j+1]:
                list_swap(obj_list, j, j+1)
                swap = True
        i -= 1


def selection_sort(obj_list):
    '''(list of objs) -> None
    Performs a selection sort on a list
    '''
    if len(obj_list) > 1:
        for i in range(len(obj_list)-1):
            (smallest, smallest_index) = (obj_list[i], i)
            for j in range(i, len(obj_list)):
                print(i,j)
                if obj_list[j] < smallest:
                    (smallest, smallest_index) = (obj_list[j], j)
            list_swap(obj_list, i, smallest_index)


def insertion_sort(obj_list):
    for i in range(len(obj_list)):
        j = 0
        inserted = False
        while j < i and not inserted:
            if obj_list[i] <= obj_list[j]:
                inserted = True
                insert_obj = obj_list.pop(i)
                obj_list.insert(j, insert_obj)
            j += 1

def quick_sort_helper(obj_list, start, end):
    '''(list of objs) -> None
    Performs a quick sort on a list
    '''
    len_obj_list = end+1 - start
    if len_obj_list > 1:
        pivot = obj_list[start]
        pivot_index = start
        for i in range(start+1, end+1):
            if obj_list[i] < pivot:
                obj_list.insert(start, obj_list.pop(i))
                pivot_index += 1
        if pivot_index - start > 1:
            quick_sort_helper(obj_list, start, pivot_index-1)
        if end - pivot_index > 1:
            quick_sort_helper(obj_list, pivot_index+1, end)

def quick_sort(obj_list):
    quick_sort_helper(obj_list, 0, len(obj_list)-1)
