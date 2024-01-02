import math
import random
import numpy as np

# def changetext(a,b):
# orientation = np.arange(0,180,10)

with open('polycrystal.txt','r') as f:
    lines=[]
    for line in f.readlines():
        if line!='\n':
            lines.append(line)
    f.close()
    print (lines)
a = np.array([0.800,0.704,0.455,0.173,0.645,0.372])
with open('polycrystal.txt','w') as f:
    n = 0
    for line in lines:
        if n != 0:
            print (line)
            # b = str(360 * random.random())
            b = str(360 * a[random.randrange(0,6)])
            new_line = line.replace('\n', ' '+b+'\n')
            print (new_line)
            f.write('%s' %new_line)
        else:
            f.write('%s' %line)
        n = n + 1
    f.close()