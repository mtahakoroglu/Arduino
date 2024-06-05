import cv2
import numpy as np

img1name = "pot.jpg"
img2name = "pot-connections.jpg"
img1 = cv2.imread(img1name)
img2 = cv2.imread(img2name)

h, w = 0, 0
h1, w1, c1 = img1.shape
h2, w2, c2 = img2.shape
if h1 > h2:
    s = h2 / h1
    img1 = cv2.resize(img1, (int(s*img1.shape[1]), int(s*img1.shape[0])), 0)
else:
    s = h1 / h2
    img2 = cv2.resize(img2, (int(s*img2.shape[1]), int(s*img2.shape[0])), 0)

h1, h2, w1, w2 = img1.shape[0], img2.shape[0], img1.shape[1], img2.shape[1]
if img1.shape[0] == img1.shape[0]:
    print("Image heights are now the same.")
    h = h1

img = np.zeros((h, w1+w2, c1), np.uint8)
img[:,0:w1,:] = img1
img[:,w1:w1+w2,:] = img2

# resize image to display on screen
s = 0.5
rimg = cv2.resize(img, (int(s*img.shape[1]), int(s*img.shape[0])), 0)
cv2.imshow("Merged image", rimg)
cv2.waitKey(0)
# save image
cv2.imwrite(f"pot-Arduino-connections.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, 100])