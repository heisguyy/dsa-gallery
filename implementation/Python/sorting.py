"""module showing the implementation of various sorting algoirthms"""
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    An implementation of the bubble sort algoirthm(aka sinking sort) used to arrange 
    a mutable sequence of integers in a particular order.

    Args:
        arr (List[int]): A sequence with unsorted elements.

    Returns:
        List[int]: the sorted version of the sequence inputted.
    """
    for array_end in range(len(arr)-1,0,-1):
        for i in range(array_end):
            if arr[i] > arr[i+1]:
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
    return arr

def selection_sort(arr: List[int]) -> List[int]:
    """
    An implementation of the selection sort algorithm used to arrange mutable sequences into
    in a particular order

    Args:
        arr (List[int]): A sequence with unsorted elements.

    Returns:
        List[int]: the sorted version of the sequence inputted.
    """
    for i, _ in enumerate(arr):
        index_of_minimum_value = i
        for index, value in enumerate(arr[i:],i):
            if value < arr[index_of_minimum_value]:
                index_of_minimum_value = index
        arr[i], arr[index_of_minimum_value] = arr[index_of_minimum_value], arr[i]
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """
    An implementation of the insertion sort algorithm used to arrange mutable sequences into
    in a particular order

    Args:
        arr (List[int]): A sequence with unsorted elements.

    Returns:
        List[int]: the sorted version of the sequence inputted.
    """

    for i,_ in enumerate(arr):
        if i == 0:
            continue
        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

if __name__ == "__main__":
    print(bubble_sort([2,3,1,8,5,6,0]))
    print(selection_sort([2,3,1,8,5,6,0]))
    print(insertion_sort([2,3,1,8,5,6,0]))
