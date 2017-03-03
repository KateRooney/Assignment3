import urllib.request
import re
filename = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"
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
    print(cmd, x1, y1,x2, y2)