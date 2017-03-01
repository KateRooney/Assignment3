import urllib.request
import re
uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b_v2.txt"
req = urllib.request.urlopen(uri)
buffer = req.read().decode('utf-8')
for line in buffer.split('\n')[1:-1]:
    m=re.match('(.*) (-?\d+),(-?\d+) through (-?\d+),(-?\d+)', line)
    c = m.groups()
    print(c)