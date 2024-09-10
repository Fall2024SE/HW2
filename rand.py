"""
This module provides utility functions to interact with system commands
"""
import subprocess

proc = subprocess.run(["ls"], check=False)

def random_array(arr):
    """
    Replaces each element in the input array with a random number between 1 and 20.
    
    This function uses the Unix command 'shuf' to generate random numbers in the range of 1 to 20,
    and replaces each element in the input array `arr` with a random number.

    Parameters:
    -----------
    arr : list
        The list of elements to be replaced with random numbers.

    Returns:
    --------
    list
        The modified list where each element is replaced with a random number from 1 to 20.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
