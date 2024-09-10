import subprocess
import sys

proc = subprocess.run(["ls"], check=False)


def print_python_version():
    """Function printing python version."""
    print(sys.version)
def random_array(arr):
     
    shuffled_num = None
    for i in enumerate(len(arr)):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
