import hw2_debugging 

def test_merge_1():
    assert hw2_debugging.merge_sort([]) == []

def test_merge_2():
    assert hw2_debugging.merge_sort([1,2,3,4,5]) == [1,2,3,4,5]

def test_merge_3():
    assert hw2_debugging.merge_sort([4,4,4,1,3]) == [1,3,4,4,4]
