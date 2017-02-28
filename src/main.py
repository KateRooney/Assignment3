import argparse
import sys
import urllib.request

class Tester:
#this is the grid
    def __init__(self):
        
        self.size = int(self.get_size())
        self._size= [[0]*self.size for _ in range(self.size)]
    
      
    def testerLED(self):
    #this is the count of lights on on the grid 
        count=0
        for row in range (0, self.size):
            for col in range (0, self.size):
                if self._size[row][col]==1:
                    count +=1
        print (count)
      
    def execute_command(self, cmd, x1, y1, x2, y2):
    #this is a switch statement that is a conditional command to 
    #call one of 3 operations on the grid
    
        if x1>self.size:
            x1=self.size
        if y1>self.size:
            y1=self.size
        if x2>self.size:
            x2=self.size
        if y2>self.size:
            y2=self.size
        if cmd =="on":
            self.turn_on(x1,x2,y1,y2)     
        elif cmd == "off":
            self.turn_off(x1,x2,y1,y2)     
        elif cmd == "switch":
            self.switch(x1,x2,y1,y2)      
        else:
            print("error, command unknown")
#         return execute_command
      
    def turn_on(self,x1,x2,y1,y2):
    #this is the first command that can be called on the grid, turn lights on
    #this gives the elements of the 2D grid the value '1'
        for row in range (y1,y2+1):
            for col in range (x1, x2+1):
                self._size[row][col] =1
#                 return turn_on
    
    def turn_off(self,x1,x2,y1,y2):
    #this is the second command that can be called on the grid, turn lights off
    #this gives the elements of the 2D grid the value '0'
        for row in range (y1,y2+1):
            for col in range (x1, x2+1):
                self._size[row][col] =0
#                 return self.turn_off()
      
    def switch(self,x1,x2,y1,y2):
    #this is the second command that can be called on the grid, to switch the lights.
    #this gives the elements of the 2D grid the value '1' for on or '0' for off.
        for row in range (y1,y2+1):
            for col in range (x1, x2+1):
                if self._size[row][col] ==1:
                    self._size[row][col] =0
                if self._size[row][col]==0:
                    self._size[row][col]=1
#                     return self.switch()
    
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
        import urllib.request          
        uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
        for line in buffer.split('\n'):
            val=line.strip().split()
            for word in val[:]:
                if word == 'turn':
                    val.remove(word)
                    for word in val[:]:
                        if word=='through':
                            val.remove(word)
                            new_val=[]
                            for i in val:
                                new_val.extend(i.split(','))
                            cmd=new_val[0]
                            x1=int(new_val[1])
                            y1=int(new_val[2])
                            x2=int(new_val[3])
                            y2=int(new_val[4])
                            self.execute_command(cmd, x1, y1, x2, y2)
                            
    
    def get_size(self):
    # this parses the size of the grid. I should have included in the above but 
    #don't have the coding skills to return this as part of that function without creating bugs 
        lines=[]         
        uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
        for line in buffer.split('\n'):
            lines.append(line)
        size = (lines[0])
        return size
                        
    
    def parse_filename(self,filename):
    #this is called if the file does not start with 'http' - file is parsed to give values for 
    #command (cmd) and the co-ordinates of the lights, x1,y1 is the first light in the array
    #to be affected and x2, y2 is the last light in the array to be affected       
        with open(filename) as f:      
            for line in f.split('\n'):
                val=line.strip().split()
                for word in val[:]:
                    if word == 'turn':
                        val.remove(word)
                        for word in val[:]:
                            if word=='through':
                                val.remove(word)
                                new_val=[]
                                for i in val:
                                    new_val.extend(i.split(','))
                                cmd=new_val[0]
                                x1=int(new_val[1])
                                y1=int(new_val[2])
                                x2=int(new_val[3])
                                y2=int(new_val[4])
                                self.execute_command(cmd, x1, y1, x2, y2)
    
# def get_arg(Tester):
#     # this parses from command line the argument - filename
#         parser=argparse.ArgumentParser()
#         parser.add_argument(Tester, help='Tester help')
#         args=parser.parse_args()
#         filename=args.input
#         return filename


grid = Tester()
grid.testerLED()
grid.parse_uri()
grid.testerLED()