#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:52:35 2020

@author: osboxes
"""

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import requests
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir='/home/osboxes/eclipse-workspace'
dataType='val2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)

coco=COCO(annFile)
catIdsIntersec = coco.getCatIds(catNms=['chair','person'])
imgIdsIntersec = coco.getImgIds(catIds=catIdsIntersec )
#intersection img is 367 total = 734

catIdsObject = coco.getCatIds(catNms=['person'])

imgIdsObject = coco.getImgIds(catIds=catIdsObject ) #chair img = 580  total = 1160
                                                    #person img 2693


onlyObject=[]
print(len(imgIdsObject))
for i in imgIdsObject:
    
    if i not in imgIdsIntersec:
            
            onlyObject.append(i) # 213 = chair - intersection or
                                 # person - intersection = 2326 and total 4652
 
print(len(onlyObject))
#person = 2693
for i in range(len(onlyObject)):
    
    img = coco.loadImgs(onlyObject)[i]
    data_img = requests.get(img['coco_url']).content
    with open('/home/osboxes/eclipse-workspace/obj-person/'+img['file_name'], 'wb') as handler:
        handler.write(data_img)
    
    filename_jpg = img["file_name"]
    filename = filename_jpg.split(".jpg")
    filename_txt = filename[0]+".txt"
    
    with open('/home/osboxes/eclipse-workspace/obj-person/'+filename_txt,'w') as handler:
        annIds = coco.getAnnIds(imgIds = img['id'], catIds=catIdsObject, iscrowd=None)
        for j in range(len(annIds)):
            anns = coco.loadAnns(annIds[j])
            x=anns[0]['bbox'][0] # anns[0] is un object segmentation and bbox is into object
            y=anns[0]['bbox'][1]
            w=anns[0]['bbox'][2]
            h=anns[0]['bbox'][3]
            W=img['width']
            H=img['height']
            annotations = str(anns[0]['category_id']-1)+ " " +str(round((x+w/2)/W,6))+ " " +str(round((y+h/2)/H,6))+ " " +str(round(w/W,6))+ " " +str(round(h/H,6))
            handler.write(annotations)
            handler.write('\n')
          
print('end')   