import cv2
import numpy as np
from random import randint

height=1000
width=1000
blank_image = np.zeros((height,width,3), np.uint8)
all_points= [[500,0],[1000,1000],[0,1000]]
base_points= [[500,0],[1000,1000],[0,1000]]

def leng_2_points(x1,y1,x2,y2):
    xdiff=abs(x1-x2)
    ydiff=abs(y1-y2)
    return xdiff,ydiff

def get_random_point_between_2(x1,y1,x2,y2):
    xdiff,ydiff=leng_2_points(x1,y1,x2,y2)
    
    value = int(xdiff/2)
    if(x1<x2):
        new_X=x1+value
    else:
        new_X=x2+value

    value_y=int((value*ydiff)/xdiff)
    if(y1<y2):
        if(x2<x1):
            new_Y=y2-value_y
        else:
            new_Y=y1+value_y

    else:
        if(x1<x2):
            new_Y=y1-value_y
        else:
            new_Y=y2+value_y


    
    return int(new_X),int(new_Y)


for i in range(1,60000):
    x_1,y_1=all_points[randint(0, len(all_points)-1)]
    x_2,y_2=base_points[randint(0, len(base_points)-1)]
    if(x_1==x_2 or y_1==y_2):
        continue
    x,y= get_random_point_between_2(x_1,y_1,x_2,y_2)
    image2 = cv2.circle(blank_image, (x,y), radius=0, color=(0, 0, 255), thickness=-1)
    all_points.append([x,y])

cv2.imshow("window_name", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
