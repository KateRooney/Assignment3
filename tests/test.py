import sys
import urllib.request
from nose.tools import *
from main import Tester

def test_parse_file():
    #this test checks that the commands and arguments parsed to the functions are as expected
    line='switch 857,894 through 920,932'
    (cmd, x1, y1, x2, y2)=Tester.parse_uri(line)
    eq_(cmd, "switch", "cmd switch passes test")
    eq_(x1,857, "x1 passes test")
    eq_(y1, 894, "y1 passes test")
    eq_(x2, 920, "x2 passes test")
    eq_(y2, 932, "y2 passes test")
    
def test_parse_mistake_with_file_cmd():
    #this test checks that the commands and arguments parsed to the functions are as expected
    line='swptch 857,894 through 920,932'
    (cmd, x1, y1, x2, y2)=Tester.parse_uri(line)
    eq_(cmd, "", "code should ignore this line")
  
def test_parse_negative_number_with_file_cmd():
    #this test checks that the negative number in arguments is parsed to the functions as 0
    tester=Tester(10)
    tester.execute_command('turn on -5,0 through 0,4')
    eq_(tester.count(),5)  
    
def test_parse_outside_range_as_inside_range():
#this test check that co-ordinates greater than the grid's area are limited to the grid area
    line='turn on 226,196 through 5999,390'
    tester=Tester(1000)
    (cmd, x1, y1, x2, y2)=Tester.execute_command(line)
    eq_(x2, 999, "1000-1, 999 should be returned") 

def test_execute_command_illogical_cmd_array_sequence():
#testing that more lights switched off than are on to begin with parses correctly
    tester=Tester(10)
    tester.execute_command('turn on 0,0 through 0,4')
    tester.execute_command('turn off 0,0 through 0,7')
    tester.execute_command('switch 0,0 through 0,4')
    eq_(tester.count(),5)
    