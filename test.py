# -*- coding:utf-8 -*-
# @author :adolf
import numpy as np
import cv2
import matplotlib.pyplot as plt
from utils import resize_image
import traceback

resize = True
max_size = 768


def plot(img):
    plt.imshow(img)
    plt.show()
    return


img = cv2.imread('./data_test/5.jpg')
print(f'ori size: {img.shape}', end='\t')
if resize:
    w, h = resize_image(img, max_size)
    img = cv2.resize(img, dsize=(w, h))
    print(f'resize size: {img.shape}')
# plot(img)

with open('./text_file/5.txt', 'r') as f:
    for line in f.readlines():
        list_on = line.split(',')
        # cv2.polylines(img,)
        # print(line)
        cv2.rectangle(img, (int(list_on[0]), int(list_on[1])),
                      (int(list_on[4]), int(list_on[5])), (255, 0, 0), 2)

    plot(img)

traceback.print_exc()
