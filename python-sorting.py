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
        # Remove the objs at both indices. Larger index before smallest index
        # as the larger index would be shifted down by one otherwise.
        (max_obj, min_obj) = (obj_list.pop(max_index), obj_list.pop(min_index))
        # Swap objects and insert them back in the list. Smaller index first
        # so that the larger index is shifted back in the correct place.
        obj_list.insert(min_index, max_obj)
        obj_list.insert(max_index, min_obj)


def bubble_sort(obj_list):
    '''(list of objs) -> None
    Performs a bubble sort on the input list in increasing order. To increase
    efficiency, if a pass through the unsorted items in the list yields no
    swaps, the sort terminates.
    REQ: objs in <obj_list> can be compared
    '''
    swap_made = True
    # Sorted index to the end of the list holds the largest, sorted items.
    # Index is inclusive.
    sorted_index = len(obj_list)
    # Sorts while a swap was made in the previous pass and there are at least
    # two unsorted items in the list
    while swap_made and sorted_index > 1:
        swap_made = False
        # Compare adjacent pairs of unsorted objects, from left to right
        # and swapping if the left object is larger than the right object
        for i in range(1, sorted_index):
            if obj_list[i-1] > obj_list[i]:
                list_swap(obj_list, i-1, i)
                swap_made = True
        sorted_index -= 1


def selection_sort(obj_list):
    '''(list of objs) -> None
    Performs a selection sort on the input list in increasing order.
    REQ: objs in <obj_list> can be compared
    '''
    for i in range(len(obj_list)-1):
        (smallest_obj, smallest_i) = (obj_list[i], i)
        # Look for the smallest obj from i to end of the list
        for j in range(i, len(obj_list)):
            if obj_list[j] < smallest_obj:
                (smallest_obj, smallest_i) = (obj_list[j], j)
        # Swap with the obj at position i
        list_swap(obj_list, i, smallest_i)


def insertion_sort(obj_list):
    '''(list of objs) -> None
    Performs an insertion sort on the input list in increasing order.
    REQ: objs in <obj_list> can be compared
    '''
    # Insert each obj in the list into the sorted portion [0, i)
    for i in range(len(obj_list)):
        not_inserted = True
        insert_i = 0
        # Determine the index to insert the obj
        while insert_i < i and not_inserted:
            if obj_list[i] < obj_list[insert_i]:
                # Pop obj from index <i> and insert at <insert_i>
                obj = obj_list.pop(i)
                obj_list.insert(insert_i, obj)
                not_inserted = False
            insert_i += 1


def quick_sort_helper(obj_list, start, end):
    '''(list of objs, int, int) -> None
    Performs a quick sort on the input list from index <start> to index
    <end> of <obj_list>. To perform a sort on the whole list, let <start> = 0
    and <end> = len(obj_list)-1
    REQ: objs in <obj_ist> can be compared
    REQ: 0 <= start < len(obj_list)
    REQ: start <= end < len(obj_list)
    '''
    # Length of the list
    len_obj_list = end+1 - start
    if len_obj_list > 1:
        # Choose the first object as the pivot
        pivot = obj_list[start]
        pivot_index = start
        
        # Move each object to the left or right of the pivot
        # Left for less than pivot, right for greater or equal to pivot
        # Keep track of the pivot's updated index each time
        for i in range(start+1, end+1):
            if obj_list[i] < pivot:
                obj_list.insert(start, obj_list.pop(i))
                pivot_index += 1
        # Recursively quick sort on the sublists left and right of the pivot
        if pivot_index - start > 1:
            quick_sort_helper(obj_list, start, pivot_index-1)
        if end - pivot_index > 1:
            quick_sort_helper(obj_list, pivot_index+1, end)

def quick_sort(obj_list):
    '''(list of objs) -> None
    Performs a quick sort recursively on the input list <obj_list>.
    REQ: objs in <obj_list> can be compared
    '''
    quick_sort_helper(obj_list, 0, len(obj_list)-1)


def radix_sort(list_of_int):
    '''(list of int) -> None
    Performs a radix sort on a list of ints <list_of_int>.
    '''
    # Insert all the integers into the main bin
    main_bin = list_of_int

    # Check if there is at least two int in the list to sort
    if len(list_of_int) > 1:
        # Create 10 empty bins for 0-9
        digit_bins = []
        for i in range(10):
            digit_bins.append([])
        # We can get one's digit by digit%10//1
        #            ten's digit by digit%100//10
        #        hundred's digit by digit%1000//100
        #              nth digit by digit%(n*10)//n
        curr_digit = 1
        # We also need to track when n > all numbers -> the list is sorted
        # Find the largest number in the list to make this comparison
        list_sorted = False
        largest_int = max(main_bin)

        while not list_sorted:
            for num in main_bin:
                # Determine the bin each number in main bin belongs in
                num_digit = num % (curr_digit*10)//curr_digit
                # Insert the number in its correct bin
                digit_bins[num_digit].append(num)
            # Empty the main bin
            main_bin.clear()
            # Add the items in the digit bins in ascending order
            for digit_bin in digit_bins:
                main_bin.extend(digit_bin)
                digit_bin.clear()
            # Move to the next digits place
            curr_digit *= 10
            # Check if the next iteration is needed (n > all numbers)
            list_sorted = True if curr_digit > largest_int else False
