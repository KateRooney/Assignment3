import sys
from nose.tools import *
from main import *

def file_exists():
    #this test checks the file exists and would be read by get_grid function
    file="http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    size=get_grid(file)
    eq_(size,1000)

def test_parse_wrong_command_error():
    #this test checks that an inaccurate command will not parse, main file ignores these using pass statement
    (self.size, cmd, x1, y1, x2, y2)=LEDTester.execute_command(1000,"tyrn on",0,0,0,-4)
    raise CustomError("cmd not recognised")     
    
def test_parse_negative_number():
    #this test checks that the negative number in arguments is parsed to the function as 0
    (self.size, cmd, x1, y1, x2, y2)=LEDTester.execute_command(1000,"turn on",0,0,0,-4)
    eq_(y2,0)  
  
def test_outside_range():
    #this test check that coordinates passed as arguments that are greater than the grid's area 
    #are limited to the grid area
    (self.size, cmd, x1, y1, x2, y2)=LEDTester.execute_command(1000,"turn on",0,0,0,1004)
    eq_(y2,999) 

def test_execute_command_on():
    #this test checks that the command 'turn on' is parsed properly
    (self.size, cmd, x1, y1, x2, y2)=LEDTester.execute_command(1000,"turn on",0,0,0,4)
    eq_(cmd,"turn on")
    
def test_execute_command_switch():   
     #this test checks that the command 'switch' is parsed properly
    (self.size, cmd, x1, y1, x2, y2)=LEDTester.execute_command(1000,"switch",0,0,0,4)
    eq_(cmd,"turn on")
    