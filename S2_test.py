import pytest
import 
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


input_list = [1,2,3,4]

def test_average_above_list():
    assert load_S1_script().average_above_zero(input_list)==2.5 
    
    
