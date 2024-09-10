"""
This module provides utility functions to generate random numbers
"""
import secrets
import random

def random_array(arr):
    """
    Replaces each element in the input array with a random number between 1 and 20.

    Parameters:
    -----------
    arr : list
        The list of elements to be replaced with random numbers.

    Returns:
    --------
    list
        The modified list where each element is replaced with a random number from 1 to 20.
    """
    for i in range(len(arr)):
        random.random()
        arr[i] = secrets.randbelow(21)
    return arr
