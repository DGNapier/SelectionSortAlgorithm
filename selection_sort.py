my_array = [2, 6, 5, 1, 3, 4]


def selection_sort(array):
    """This is a basic selection sort algorithm.
    
    This modifies the input array by repeatedly finding the min element from the
    unsorted portion and swaps it with the first unsorted element.
    
    Args:
        array (list): The list of elements to be sorted
        
    Returns:
        None: The array is sorted in place
        
    Example:
        array = [2, 6, 5, 1, 3, 4] \n
        selection_sort(array) \n
        array \n
        [1, 2, 3, 4, 5, 6]"""

    for i in range(0, len(array) - 1):  # This defines the sort takes an array as an input. The outer loop i iterates from 0 to len(array) - 2. pylint: disable=line-too-long
        current_minimum_index = i  # We start by assuming the element in the first index is the smallest pylint: disable=line-too-long
        for j in range(i + 1, len(array)):  # Then this worked to iterate, comparing if an element at index j is smaller than the current_min_index pylint: disable=line-too-long
            if array[j] < array[current_minimum_index]:  # If there is an element at j that is smaller than i, it sets the current minimum to j pylint: disable=line-too-long
                current_minimum_index = j

        array[i], array[current_minimum_index] = (
            array[current_minimum_index],
            array[i],
        )  # This code is where the values actually swap. It relies o nswapping the values AT the current minimum index. pylint: disable=line-too-long


selection_sort(my_array)
print(my_array)
