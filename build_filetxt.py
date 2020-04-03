#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:43:24 2020

@author: osboxes
"""

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

pylab.rcParams['figure.figsize'] = (8.0, 10.0)
dataDir='/home/osboxes/eclipse-workspace'
dataType='val2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)

coco=COCO(annFile)

catIds = coco.getCatIds(catIds=['chair'])
imgIds = coco.getImgIds(catIds=catIds)
percentage_test = 0.9

train = open('/home/osboxes/eclipse-workspace/data/train.txt', 'w')

test = open('/home/osboxes/eclipse-workspace/data/test.txt', 'w')

counter=1

size = len(imgIds)

index_test = round(percentage_test*size)

for i in range(len(imgIds)):
    img=coco.loadImgs(imgIds)[i]
    if counter > index_test:
        test.write('data/obj/'+img['file_name'])
        test.write('\n')
    else:
        train.write('data/obj/'+img['file_name'])
        train.write('\n')
        counter+=1
test.close
train.close
print("end")