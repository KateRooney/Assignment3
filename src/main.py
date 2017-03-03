import argparse
import urllib.request
import re

           
def main():
    
    #this parses from command line the argument - filename
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', help='pass in filename')
    args=parser.parse_args()
    filename=args.input
    tester = LEDTester(filename)
    tester.parse_fileline(filename)
    print (filename, tester.countLED())
   

class LEDTester:
    
    def __init__(self, filename):
    #this is the grid on which the lights are located, or the 2D array
        self.size =self.get_grid(filename)
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
    #this is the third command that can be called on the grid, to switch the lights.
    #this gives the elements of the 2D grid the value '1' for on or '0' for off.
        for row in range (y1,y2+1):
            for col in range (x1, x2+1):
                if self._grid[row][col] ==1:
                    self._grid[row][col] =0
                elif self._grid[row][col]==0:
                    self._grid[row][col]=1
                else:
                    pass

    def countLED(self):
    #this is the final count of lights on on the grid 
        count=0
        for row in range (0, self.size):
            for col in range (0, self.size):
                if self._grid[row][col]==1:
                    count +=1
        return count  
           
    def parse_fileline(self, filename):
        #this parses in the file and extracts the variable the other methods in the class will use, 
        #and executes the next command in the flow
        uri=filename
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
    
    def get_grid(self, filename):
    # this parses the size of the grid. 
        uri=filename
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
        line = buffer.split('\n')
        size = int(line[0])
        return size
                    
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
    