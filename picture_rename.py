# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 0002 下午 21:47
# @Author  : fanyalei
# @Email   : 645978480@qq.com
# @File    : picture_rename.py
# @Software: PyCharm
# @description: 1 对图片的名称进行重命名，为了便于后期标注成和VOC数据集一样的 .xml。
#               2 转换其他格式的图片为 .jpg
# 目前异物图片汇总在 F:\SSD\my_obj_V1\my_obj_label 其中包含了网络图片和自行收集的图片123张

# Time:20181008 22:23
# 将png图像转换为jpg
# form：https://blog.csdn.net/bevison/article/details/79126410?utm_source=copy

import os
import cv2
import sys
import numpy as np


def png2jpg(path):
    for filename in os.listdir(path):
        if os.path.splitext(filename)[1] == '.png':
            # print(filename)
            img = cv2.imread(path + filename)
            print(filename.replace(".png", ".jpg"))
            newfilename = filename.replace(".png", ".jpg")
            # cv2.imshow("Image",img)
            #  cv2.waitKey(0)
            cv2.imwrite(path + newfilename, img)


class BatchRename():
    """
    批量重命名文件夹中的图片文件
    """
    def __init__(self,path):
        self.path = path

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            Suffix_name = ['.png', '.jpg', '.jpeg', '.tif']
            if item.endswith(tuple(Suffix_name)):
                n = 6 - len(str(i))
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(0) * n + str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print('converting %s--to-->%s' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i-1))

if __name__ == '__main__':
    #path = "F:/fan_pictures/没有异物缠绕的/"       # 图片文件夹路径
    path = "F:/SSD/from_HiKapok/MY_picture/网络图片和收集图片汇总"
    demo = BatchRename(path).rename()

