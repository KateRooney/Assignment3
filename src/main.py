import argparse
import urllib.request
import re

class Tester:
#this is the grid
    def __init__(self):
        
        self.size =self.get_grid()
        self._grid= [[0]*self.size for _ in range(self.size)]
     
    def turn_on(self,x1,x2,y1,y2):
    #this is the first command that can be called on the grid, turn lights on
    #this gives the elements of the 2D grid the value '1'
        for row in range (y1,y2+1):
            for col in range (x1, x2+1):
                if self._grid[row][col] ==0:
                    self._grid[row][col] =1
                else:
                    pass
    
    def turn_off(self,x1,x2,y1,y2):
    #this is the second command that can be called on the grid, turn lights off
    #this gives the elements of the 2D grid the value '0'
        for row in range (y1,y2+1):
            for col in range (x1, x2+1):
                if self._grid[row][col] ==1:
                    self._grid[row][col] =0
                else:
                    pass
      
    def switch(self,x1,x2,y1,y2):
    #this is the second command that can be called on the grid, to switch the lights.
    #this gives the elements of the 2D grid the value '1' for on or '0' for off.
        for row in range (y1,y2+1):
            for col in range (x1, x2+1):
                if self._grid[row][col] ==1:
                    self._grid[row][col] =0
                elif self._grid[row][col]==0:
                    self._grid[row][col]=1
                else:
                    pass

    def testerLED(self):
    #this is the count of lights on on the grid 
        count=0
        for row in range (0, self.size):
            for col in range (0, self.size):
                if self._grid[row][col]==1:
                    count +=1
        print (count)    
        
    def how_to_read_file(self,fname):
    #this tells the program which method to read the file depending on the filename
    #one of two other commands will be called depending on filename
        if fname.startswith('http'):
            return self.parse_uri()
        else:
            return self.parse_filename()
            
    def parse_uri(self):
        #this is called if the file starts with 'http' - file is parsed to give values for 
        #command (cmd) and the co-ordinates of the lights, x1,y1 is the first light in the array
        #to be affected and x2, y2 is the last light in the array to be affected  
        uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b_v2.txt"
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
        for line in buffer.split('\n')[1:-1]:
            m=re.match('(.*) (-?\d+),(-?\d+) through (-?\d+),(-?\d+)', line)
            cmd = m.group(1)
            x1 = int(m.group(2))
            y1 = int(m.group(3))
            x2 = int(m.group(4))
            y2 = int(m.group(5))
            self.execute_command(cmd, x1, y1, x2, y2)
            
    #REFERENCE: http://stackoverflow.com/questions/11739386/regex-that-matches-any-positive-
    #or-negative-numeric-value-but-no-characters-or-m   
                            
    def get_grid(self):
    # this parses the size of the grid. I should have included in the above but 
    #don't have the coding skills to return this as part of that function without creating bugs         
        uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b_v2.txt"
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
        for line in buffer.split('\n')[0:1]:
            size = int(line)
        return size
                    
    def parse_filename(self,filename):
    #this is called if the file does not start with 'http' - file is parsed to give values for 
    #command (cmd) and the co-ordinates of the lights, x1,y1 is the first light in the array
    #to be affected and x2, y2 is the last light in the array to be affected       
        with open(filename) as f:      
            for line in f.split('\n')[1:-1]:
                m=re.match('(.*) (\d+),(\d+) through (\d+),(\d+)', line)
                cmd = int(m.group(1))
                x1 = int(m.group(2))
                y1 = int(m.group(3))
                x2 = int(m.group(4))
                y2 = int(m.group(5))
                self.execute_command(cmd, x1, y1, x2, y2)
      
    def execute_command(self, cmd, x1, y1, x2, y2):
    #this is a switch statement that is a conditional command to 
    #call one of 3 operations on the grid
        if x1>self.size:
            x1=self.size-1
        if x1<0:
            x1=0
        if y1>self.size:
            y1=self.size-1
        if y1<0:
            y1=0
        if x2>self.size:
            x2=self.size-1
        if x2<0:
            x2=0
        if y2>self.size:
            y2=self.size-1
        if y2<0:
            y2=0
        if cmd =="turn on":
            self.turn_on(x1,x2,y1,y2)     
        elif cmd == "turn off":
            self.turn_off(x1,x2,y1,y2)  
        elif cmd == "switch":
            self.switch(x1,x2,y1,y2)         
        else:
            pass
   
        """def get_arg():
        #this parses from command line the argument - filename
        parser=argparse.ArgumentParser()
        parser.add_argument('--input', help='Tester help')
        args=parser.parse_args()
        filename=args.input
        return filename"""


grid = Tester()
grid.parse_uri()
grid.testerLED()