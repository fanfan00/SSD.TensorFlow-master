# SSD.TensorFlow-master
Foreign object detection  BY fanyalei
weight:链接：https://pan.baidu.com/s/1QgWLVgJYNUjD65MIlizy8Q 提取码：m1pn 
VOC数据集：链接：https://pan.baidu.com/s/1bzESmd11AmA-Vn15E1dlfQ 
![image](https://github.com/fanfan00/SSD.TensorFlow-master/upload/master/logs)
run:
1 'dataset' build ‘tfrecords’ , then run convert_tfrecords.py

2 Run the following script to start training:

  python train_ssd.py

  Run the following script for evaluation and get mAP:

  python eval_ssd.py
  python voc_eval.py

Note: you need first modify some directory in voc_eval.py

  Run the following script for visualization:

  python simple_ssd_demo.py

![image](https://github.com/fanfan00/SSD.TensorFlow-master/blob/master/logs/120K%E4%BA%A4%E5%8F%89%E7%86%B5%E6%8D%9F%E5%A4%B1.jpg)

![image](https://github.com/fanfan00/SSD.TensorFlow-master/blob/master/logs/120K%E5%AE%9A%E4%BD%8D%E6%8D%9F%E5%A4%B1.jpg)

![image](https://github.com/fanfan00/SSD.TensorFlow-master/blob/master/logs/120K%E6%80%BB%E6%8D%9F%E5%A4%B1.jpg)

![image](https://github.com/fanfan00/SSD.TensorFlow-master/blob/master/logs/test%E4%B8%8A%E7%9A%84%E5%87%86%E7%A1%AE%E7%8E%87.png)

![image](https://github.com/fanfan00/SSD.TensorFlow-master/blob/master/demo/000191.jpg)

![image](https://github.com/fanfan00/SSD.TensorFlow-master/blob/master/demo/000042.jpg)

![image](https://github.com/fanfan00/SSD.TensorFlow-master/blob/master/demo_out/test_out_191.jpg)

![image](https://github.com/fanfan00/SSD.TensorFlow-master/blob/master/demo_out/test_out_42.jpg)
