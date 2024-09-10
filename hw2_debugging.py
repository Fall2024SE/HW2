"""Module to generate random array"""
import rand

def merge_sort(nums):
    """
    Sorts an array using the merge sort algorithm.

    Parameters:
    -----------
    nums : list
        The list of elements (numbers or comparable objects) to be sorted.

    Returns:
    --------
    list
        A new list containing the elements of `nums`, sorted in ascending order.

    """
    if len(nums) == 1:
        return nums

    half = len(nums) // 2

    return recombine(merge_sort(nums[:half]), merge_sort(nums[half:]))


def recombine(left_arr, right_arr):
    """
    Merges two sorted arrays into a single sorted array.

    This function takes two sorted arrays, `left_arr` and `right_arr`, and merges them into a single
    sorted array by comparing elements from each and inserting them into their correct position.

    Parameters:
    -----------
    left_arr : list
        The first sorted list of elements to be merged.
    right_arr : list
        The second sorted list of elements to be merged.

    Returns:
    --------
    list
        A new list containing all elements from `left_arr` and `right_arr`, 
        sorted in ascending order.

    """
    left_index = 0
    right_index = 0
    merged_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merged_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merged_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merged_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merged_arr[left_index + right_index] = left_arr[i]

    return merged_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
