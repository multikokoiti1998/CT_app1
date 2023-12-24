x=512
y=512
bytesize=1
histogramX=256
histogramY=256

import struct
import math
from pathlib import Path
import pydicom
import cv2
import numpy as np

rf1=open(r'F:\DD_CT\100-200.dcm','rb')
rf2=open(r'F:\DD_CT\100-800.dcm','rb')
wf=open('20histogram.raw','wb')

data1=rf1.read(bytesize*x*y)
data2=rf2.read(bytesize*x*y)

histmap=[[0 for j in range(histogramX)] for i in range(histogramY)]
outbinary=[[0 for j in range(histogramX)] for i in range(histogramY)]
p_ab=[[0 for j in range(histogramX)] for i in range(histogramY)]
p_a=[0 for j in range(histogramX)]
p_b=[0 for j in range(histogramY)]
t=[[0 for j in range(histogramX)] for i in range(histogramY)]

histsum=0
mutual=0

#2次元ヒストグラム作成
for k in range(len(data1)):
    
    num1=data1[k]
    num2=data2[k]
    histmap[num1][num2] +=1
for m in range(histogramX):
    for n in range(histogramY):
     histsum += histmap[m][n]
     outbinary[m][n] = struct.pack('I',histmap[m][n])
     wf.write(outbinary[m][n])
     
#相互情報計算
#p(a,b)
for m in range(histogramX):
    for n in range(histogramY):
        p_ab[m][n] = histmap[m][n]/(histsum)
        
#p(a),p(b)
for m in range(histogramX):
    for n in range(histogramY):
        p_a[m]+= p_ab[m][n]
        p_b[n]+= p_ab[m][n]
for m in range(histogramX):
    for n in range(histogramY):
        if p_a[m]*p_b[n] !=0:
            t[m][n]=p_ab[m][n]/(p_a[m]*p_b[n])
            if t[m][n] !=0:
                mutual += p_ab[m][n]*math.log(t[m][n], 2)
                
print (mutual)

rf1.close()
rf2.close()
wf.close()