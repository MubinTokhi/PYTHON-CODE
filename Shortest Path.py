

#Shortest Path////////////

import math
def short_path(dir_name):

    y = 0
    x = 0

    for i in range(len(dir_name)):

        if dir_name [i] == "S":

            y-=1
        elif dir_name[i] == "N":

            y +=1
        elif dir_name [i] == " E":

            x+=1
        else:

            x-=1
    
    X2 = x * x 
    Y2 = y * y

    return math.sqrt(X2+Y2)

name = "WNEENESENNN"

print(short_path(name))
