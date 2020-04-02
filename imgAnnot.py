# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 05:35:10 2020

@author: Toshiba
"""


from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir='..'
dataType='val2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)

coco=COCO(annFile)

catIds = coco.getCatIds(catNms=['toaster'])
imgIds = coco.getImgIds(catIds = catI)

for i in range(len(imgIds)):
    
    img = coco.loadImg(imgIds)[i]
    data_img = requests.get(img['coco_url']).content
    with open('obj'+img['file_name'], 'wb') as handler:
        handler.write(data_img)
    
    filename_jpg = img["file_name"]
    filename = filename_jpg.split(".jpg")
    filename_txt = filename[0]+".txt"
    
    with open('obj'+filename_txt,'w'):
        annIds = coco.getAnnIds(imgIds = img['id'], catIds=catIds, iscrowd=None)
        for j in range(len(annIds)):
            anns = coco.loadAnns(annIds[j])
            x=anns[0]['bbox'][0]
            y=anns[0]['bbox'][1]
            w=anns[0]['bbox'][2]
            h=anns[0]['bbox'][3]
            W=img['width']
            H=img['Height']
            annotations = str(catIds[0]-1) + "" +str((x+w/2)/W) + "" +str((y+h/2)/H) + "" +str(w/W) + "" +str(h/H)
            handler.write(annotations)
            handler.write('\n')
        