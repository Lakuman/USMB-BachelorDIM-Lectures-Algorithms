import pytest
def load_S1_script():
    """
        utility function that tris to load the script written along the first lesson
        @throws an ImportError exception if the script file does not exist
        @return the script as a loaded module
    """
    S1_script_filename='assignments/Session1/S1_algotools.py'
    import imp
    s1_algotools=imp.load_source('session_1_script', S1_script_filename)
    return  s1_algotools


def test_average_above_list():
    
    input_list = [1,2,3,4]
    assert load_S1_script().average_above_zero(input_list)== 2.5 
    input_list = [-1,-2,-3,4]
    assert load_S1_script().average_above_zero(input_list)== 4
    input_list = [-1,-2,-3,-4]
    with pytest.raises(ZeroDivisionError):
        load_S1_script().average_above_zero(input_list)   
    
def test_max_value():
    input_list = [1,2,3,4]
    assert load_S1_script().max_value(input_list)== 4

    input_list = [-1,-2,-3,-4]
    assert load_S1_script().max_value(input_list)== -1

def test_reverse_table():
    input_list = [1,2,3,4]
    assert load_S1_script().reverse_table(input_list)== [4, 3, 2, 1]
    
def test_remove_whitespace():
    mystring = "Hello world"
    assert load_S1_script().remove_whitespace(mystring)== "Helloworld"

def test_sort_selective():
    my_list = [10, 15, 7, 1, 3, 3, 9]
    assert load_S1_script().sort_selective(my_list)== [1, 3, 3, 7, 9, 10, 15]

    my_list = [-10, -15, -7, -1, -3, -3, -9]
    assert load_S1_script().sort_selective(my_list)== [-15, -10, -9, -7, -3, -3, -1]

def test_sort_bubble():
    my_list = [10, 15, 7, 1, 3, 3, 9]
    assert load_S1_script().sort_bubble(my_list)== [1, 3, 3, 7, 9, 10, 15]

    my_list = [-10, -15, -7, -1, -3, -3, -9]
    assert load_S1_script().sort_bubble(my_list)== [-15, -10, -9, -7, -3, -3, -1]
