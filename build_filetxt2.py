#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 06:44:05 2020

@author: osboxes
"""

# creation of files txt for test and train
train = open('/home/osboxes/eclipse-workspace/YOLO-DATA/data/train.txt', 'w')
test = open('/home/osboxes/eclipse-workspace/YOLO-DATA/data/test.txt', 'w')

#************************* get total lines in file source *******************
def getsizefile():
    
    size=0 # total lines in file
    with open('/home/osboxes/eclipse-workspace/YOLO-DATA/file.txt', 'r') as file:
    
        for line in file:
            size+=1
    return size        
#****************************************************************************        
percentage_test = 0.9
index_test = round(percentage_test*getsizefile())

index_current=0
#open file content path from images ex: data/obj/*.jpg
with open('/home/osboxes/eclipse-workspace/YOLO-DATA/file.txt', 'r') as handler:
      
#lecture line per ligne from file

    for line in handler:
        index_current+=1
        if index_current<=index_test:
            train.write(line) # writing 90% lines from file.txt to train.txt
        else:   
            
            test.write(line) # writing 10% lines from file.txt to test.txt
 
print('end')

