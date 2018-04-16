import cv2
import numpy as np

def red_mask(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # lower mask (0-10)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
    # upper mask (170-180)
    lower_red = np.array([170, 100, 100])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
    # join my masks
    mask = mask0 + mask1
    # creating a circle kernel
    #kernel_circle = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    # dilation with a circle kernel
    #dilation = cv2.dilate(mask, kernel=kernel_circle, iterations=2)
    # set mask: zero everywhere exept hot zones
    output_img_red = img.copy()
    #output_img_red[np.where(dilation == 0)] = 0
    return mask, output_img_red #returns a mask with all the red pixels?

def find_bottletap(image_rgb):
    #turn image_rgb into image_gray : a grayscale image
    image_gray = cv2.cvtColor(image_rgb , cv2.COLOR_RGB2GRAY)
    # detect circles in the image
    circles = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT, 1, 500, param1=40, param2=30,
                               minRadius=20, maxRadius=100)
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        # loop over the (x, y) coordinates and radius of the circles
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            # print(i)
            cv2.circle(image_rgb, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(image_rgb, (i[0], i[1]), 2, (0, 0, 0), 3)
    else:
        print("No bottletap on track!")

    return image_rgb

def find_track(img):
    img[0:195,:] = 0
    img[300:600,:] = 0

    return img

def bottletap(img, x, y,r):
    for i in np.arrange(0, image.shape[0]):
        for j in np.arrange(0, image.shape[1]):
            if((((j-x)**2) + (((i-y)**2)))>r**2):
                img[i,j,0] = 0
                img[i,j,1] = 0
                img[i,j,2] = 0
    return img

