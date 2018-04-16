import cv2
import IDcircle as idc
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
# Load and prepare image:
print("Load and prepare image: ")
img_BGR = cv2.imread("image019.jpg")
img = idc.find_track(img_BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img, cmap= None)
plt.show()
# WARNING: Image has to be in grayscale!

print("Finding circle...")
x=100
y=100
r=100
x, y, r, img_circle = idc.find_bottletap(img,x,y,r)
plt.imshow(img_circle,cmap='Blues')
plt.show()
print(x,y,r)
plt.imshow(img_circle[y-r:y+r,x-r:x+r],cmap='Blues')
plt.show()
img_new = idc.bottletap(img_circle[x-r:x+r,y-r:y+r], x, y, r)
print("Circle found: ")
bw, color = idc.blue_mask(img_new)
plt.imshow(color, cmap= 'gray')
plt.show()
message=idc.getColor(img_new)
print(message)
plt.imshow(img_new,cmap='Blues')
plt.show()
print("End program.")


# img_circle[y-r:y+r,x-r:x+r] <-- Vaka ja prakjam slikata za da oderi boja!