import sys
from nose.tools import *
from main import LEDTester


def test_b():
    line='switch 857,894 through 920,932'
    m=LEDTester.parse_fileline(line)
    eq_(m.cmd,"switch", 'cmd is not switch')
     
    """def test_parse_file():
    #this test checks that the commands and arguments parsed to the functions are as expected
    (cmd, x1, y1, x2, y2)=LEDTester.parse_fileline('switch 857,894 through 920,932')
    eq_(cmd,"switch", 'cmd is not switch')

    
def test_parse_mistake_with_file_cmd():
    #this test checks that the commands and arguments parsed to the functions are as expected
    line='swptch 857,894 through 920,932'
    (cmd, x1, y1, x2, y2)=LEDTester.parse_uri(line)
    eq_(cmd,)
  
def test_parse_negative_number_with_file_cmd():
    #this test checks that the negative number in arguments is parsed to the functions as 0
    tester=LEDTester(10)
    tester.execute_command('turn on -5,0 through 0,4')
    eq_(tester.count(),5)  
    
def test_parse_outside_range_as_inside_range():
#this test check that co-ordinates greater than the grid's area are limited to the grid area
    line='turn on 226,196 through 5999,390'
    tester=LEDTester(1000)
    (cmd, x1, y1, x2, y2)=Tester.execute_command(line)
    eq_(x2, 999) 

def test_execute_command_illogical_cmd_array_sequence():
#testing that more lights switched off than are on to begin with parses correctly
    tester=LEDTester(10)
    tester.execute_command('turn on 0,0 through 0,4')
    tester.execute_command('turn off 0,0 through 0,7')
    tester.execute_command('switch 0,0 through 0,4')
    eq_(tester.count(),5)"""
    