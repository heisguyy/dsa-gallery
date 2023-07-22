"""module showing the various sorting algoirthms"""
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    An implementation of the bubble sort algoirthm used to arrange 
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


if __name__ == "__main__":
    print(bubble_sort([2,3,1,8,5,6,0]))
