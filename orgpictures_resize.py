# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 0012 下午 17:10
# @Author  : fanyalei
# @Email   : 645978480@qq.com
# @File    : orgpictures_resize.py
# @Software: PyCharm
# @description:  参考 https://www.cnblogs.com/xuanxufeng/p/6283101.html

from PIL import Image
import os

def convert(dir,out_dir,width,height):
    file_list = os.listdir(dir)
    for filename in file_list:
        path = ''
        path = dir + filename
        im = Image.open(path)
        im = im.convert('RGB')
        (x, y) = im.size
        x_s = width
        y_s = y * x_s // x
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        out.save(out_dir+filename)
        print("%s has been resized!" % filename)

if __name__ == '__main__':
    dir = 'F:/SSD/from_HiKapok/MY_picture/VOC/'
    out_dir = 'F:/SSD/from_HiKapok/MY_picture/VOC_resize/'
    convert(dir,out_dir,500,500)