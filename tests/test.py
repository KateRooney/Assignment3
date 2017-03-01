import sys
import unitest
from nose.tools import *
from main import Tester

def test_file_exists(self):
#this test checks that the filenames parsed are as expected
    a='http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
    b='http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt'
    c='http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt'
    d='http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt'
    e='http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt'
    if main.uri == a or b or c or d or e:
        ok_()

def test_instructions_within_file(self):
#this test checks that the commands on, off and switch are in the file, idea is that 
#we are looking at a good file
    for line in main.uri:
        a ="turn on"
        b="turn off"
        c="switch"
        if  a or b or c in line:
                ok_()

def test_limit_lights_on(self.size, testerLED):
#this test checks that the number of lights counted to be switched on is not greater than the grid size
    if testerLED<=Tester.size:
        ok_()
        
def test_outside_range(self.size,x1,y1,x2,y2):
#this test checks that the coordinates in the file are not bigger outside the sqare grid
    maximum=main.self.size
    if (x1<maximum) and (x2<maximum) and (y1<maximum) and (y2<maximum):
        ok_() 

"""def test_lights_turned_on(self,x1,x2,y1,y2):
    for row in range (y1,y2+1):
        for col in range (x1, x2+1):
            self._size[row][col] =1"""