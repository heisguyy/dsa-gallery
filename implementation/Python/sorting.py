"""module showing the implementation of various sorting algoirthms"""
from typing import List
import math

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

def merge(first_array: List[int], second_array: List[int]) -> List[int]:
    """
    Helper function for the merge sort function implemented below

    Args:
        first_array (List[int]): sorted array to be merged. 
        second_array (List[int]): sorted array to be merged.

    Returns:
        List[int]: Sorted array containing all the elements of the two input arrays.
    """
    first_arr_counter = 0
    second_arr_counter = 0
    new_arr = [0]*(len(first_array)+len(second_array))
    new_arr_counter = 0
    while first_arr_counter < len(first_array) and second_arr_counter < len(second_array):
        if first_array[first_arr_counter] <= second_array[second_arr_counter]:
            new_arr[new_arr_counter] = first_array[first_arr_counter]
            first_arr_counter+=1
        else:
            new_arr[new_arr_counter] = second_array[second_arr_counter]
            second_arr_counter+=1
        new_arr_counter+=1

    while first_arr_counter < len(first_array):
        new_arr[new_arr_counter] = first_array[first_arr_counter]
        first_arr_counter+=1
        new_arr_counter+=1

    while second_arr_counter < len(second_array):
        new_arr[new_arr_counter] = second_array[second_arr_counter]
        second_arr_counter+=1
        new_arr_counter+=1

    return new_arr

def merge_sort(arr: List[int]) -> List[int]:
    """
    An implementation of the merge sort algorithm used to arrange a sequence in a 
    particular order.

    Args:
        arr (List[int]): Unsorted sequence

    Returns:
        List[int]: Sorted sequence
    """
    if len(arr) == 1:
        return arr
    else:
        middle = len(arr)//2
        sorted_arr = merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))
    return sorted_arr

def bucket_sort(arr: List[int]) -> int:
    """
    Implementation of the bucket sort algorithm used to arrange a sequence in a particular order.

    Args:
        arr (List[int]): Unsorted sequence

    Returns:
        int: Sorted sequence.
    """
    number_of_buckets = round(math.sqrt(len(arr)))
    maximum_value = max(arr)
    buckets = []

    for _ in range(number_of_buckets):
        buckets.append([])
    for element in arr:
        if element == 0:
            bucket_index = 0
        else:
            bucket_index = math.ceil((element * number_of_buckets) / maximum_value) - 1
        buckets[bucket_index].append(element)
    for bucket_index, bucket in enumerate(buckets):
        buckets[bucket_index] = merge_sort(bucket)
    arr_index = 0
    for bucket in buckets:
        for element in bucket:
            arr[arr_index] = element
            arr_index+=1
    return arr

if __name__ == "__main__":
    # print(bubble_sort([2,3,1,8,5,6,0]))
    # print(selection_sort([2,3,1,8,5,6,0]))
    # print(insertion_sort([2,3,1,8,5,6,0]))
    # print(merge_sort([29,10,14,37,14]))
    print(bucket_sort([2,3,1,8,5,6,0]))
