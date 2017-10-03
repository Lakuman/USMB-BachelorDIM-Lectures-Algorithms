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


load_S1_script()

input_list = [1,2,3,4]

def test_average_above_list():
    assert load_S1_script().average_above_zero(input_list)== 2.5 
    
def test_max_value():
    assert load_S1_script().max_value(input_list)== (4, 3) 

def test_reverse_table():
    assert load_S1_script().reverse_table(input_list)== (4, 3, 2, 1)
    
def test_remove_whitespace():
    assert load_S1_script().remove_whitespace(input_list)== "Helloworld"
