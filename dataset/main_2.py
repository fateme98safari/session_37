import cv2
import os
import numpy as np

image=cv2.imread("dataset\input\spaces_u9ESMkINnUK9Z0nC4FPH_uploads_fX9Y3TPp9vHLVpN1pe4T_mnist.webp",0)
# print(image.shape)
k=0
count=1
for i in range(0,1000,20):
    for j in range(0,2000,20):
        # image_k=np.zeros((10, 20), dtype="uint8")
        number=image[i:i+20,j:j+20]
        path=f"dataset\output\{k}"
        os.makedirs(path,exist_ok=True)
        cv2.imwrite(f"{path}\{k}_{count}.jpg", number)
        count+=1
        if count>500:
            count=1
            k+=1
cv2.waitKey()
