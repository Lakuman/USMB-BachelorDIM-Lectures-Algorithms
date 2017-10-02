import pytest
import asssignments.Session1.S1_algotools as algo

input_list = [1,2,3,4]

def test_average_above_list():
    assert algo.average_above_zero(input_list)==2.5 
    
    
