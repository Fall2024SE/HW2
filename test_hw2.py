import hw2_debugging

def test_pass1():
    assert hw2_debugging.mergeSort([]) 

def test_pass2():
    assert hw2_debugging.mergeSort([1,2,3,4,5]) 

def test_pass3():
    assert hw2_debugging.mergeSort([4,4,4,1,3]) 
