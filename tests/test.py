import sys
import urllib.request
from nose.tools import *
from main import Tester


def test_parse_file():
    #this test checks that the filenames parsed are as expected
    line='switch 857,894 through 920,932'
    (cmd, x1, y1, x2, y2)=Tester.parse_uri(line)
    eq_(cmd, "switch")
    eq_(x1,857)
    eq_(y1, 894)
    eq_(x2, 920)
    eq_(y2, 932)
    
"""Tester=

def test_limit_lights_on(self.size, testerLED):
#this test checks that the number of lights counted to be switched on is not greater than the grid size
    if testerLED<=Tester.size:
        ok_()
        
def test_outside_range(self.size,x1,y1,x2,y2):
#this test checks that the coordinates in the file are not bigger outside the sqare grid
    maximum=main.self.size
    if (x1<maximum) and (x2<maximum) and (y1<maximum) and (y2<maximum):
        ok_() 

def test_lights_turned_on(self,x1,x2,y1,y2):
    for row in range (y1,y2+1):
        for col in range (x1, x2+1):
            self._size[row][col] =1"""