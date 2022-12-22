import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img1 = np.array(Image.open("four.png"))
img2 = np.array(Image.open("six.png"))
img3 = np.array(Image.open("three.png"))


#Cinco lados 
img_and = img1 & img3

plt.figure(figsize=(16, 16))
plt.subplot(2, 1, 2)
plt.imshow(img_and)

#Dois lados
img_xor = img1 | img3

plt.figure(figsize=(16, 16))
plt.subplot(2, 1, 2)
plt.imshow(img_xor)

#Apenas um lado

img_xor = img1 ^ img3
img_and = img_xor & img1

img_and_not = np.invert(img_and)
plt.figure(figsize=(16, 16))
plt.subplot(2, 1, 2)
plt.imshow(img_and_not)


plt.show()