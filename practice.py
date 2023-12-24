from pathlib import Path
import pydicom
import cv2
import numpy as np
data_path = sorted(Path('C:/Users/multi/OneDrive/デスクトップ/CT画像解析プログラム/00000001').glob('*.dcm'))

#スライス画像格納用
ct_vol=[]
#print(ct_vol)
#スライスを順次格納
for path  in data_path:
    dcm=pydicom.dcmread(path)
    img=dcm.pixel_array
    ct_vol.append(img)
    
ct_vol=np.array(ct_vol)

#3次元の形状確認
print(ct_vol.shape)

cv2.imshow('Slice 23', ct_vol[23])
cv2.waitKey(0)
cv2.destroyAllWindows()

print(ct_vol[23].min(),ct_vol[23].max())
 
 