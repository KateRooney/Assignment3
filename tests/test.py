import sys
from nose.tools import *
from main import *


def test_file_exists_and_size_returns():
    #this test checks the file exists and would be read by get_grid function
    tester = LEDTester("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    size=tester.get_grid("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    eq_(size,1000) 
 
def test_parse_negative_number_as_zero(event=None):
    #this test checks that the negative number in arguments is parsed to the function as 0
    tester = LEDTester("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    y2=tester.execute_command("turn on",0,0,3,-4)
    eq_(y2,0)  
  
def test_parse_outside_range_as_inside_grid():
    #this test check that coordinates passed as arguments that are greater than the grid's area 
    #are limited to the grid area
    tester = LEDTester("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
    y2=tester.execute_command("turn on",0,0,0,1004)
    eq_(y2,999)
    


