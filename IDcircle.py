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
    kernel_circle = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    # dilation with a circle kernel
    dilation = cv2.dilate(mask, kernel=kernel_circle, iterations=2)
    # set mask: zero everywhere exept hot zones
    output_img_red = img.copy()
    output_img_red[np.where(dilation == 0)] = 0
    return mask , output_img_red #returns a mask with all the red pixels?


def blue_mask(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([120, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
    # set mask: zero everywhere exept target zones
    output_img_blue = img.copy()
    output_img_blue[np.where(mask == 0)] = 0
    return mask ,output_img_blue


def green_mask(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_green = np.array([20, 50, 50])
    upper_green = np.array([100, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img_hsv, lower_green, upper_green)
    output_img_green = img.copy()
    output_img_green[np.where(mask == 0)] = 0
    return mask ,output_img_green


def yellow_mask(img): #POPRAVI JA! Ovaj ne raboti!!!
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    lower_yellow = np.array([80, 100, 200])
    upper_yellow = np.array([100, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img_rgb, lower_yellow, upper_yellow)
    output_img_yellow = img.copy()
    output_img_yellow[np.where(mask == 0)] = 0
    return mask ,output_img_yellow


def find_bottletap(image_rgb,x,y,r):
    #turn image_rgb into image_gray : a grayscale image
    image_gray = cv2.cvtColor(image_rgb , cv2.COLOR_RGB2GRAY)
    # detect circles in the image
    circles = cv2.HoughCircles(image_gray, cv2.HOUGH_GRADIENT, 1, 1000, param1=40, param2=30,
                               minRadius=50, maxRadius=70)
    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        # loop over the (x, y) coordinates and radius of the circles
        circles = np.uint16(np.around(circles))
        for i in circles[0,:,]:
            # draw the outer circle
            # print(i)
            cv2.circle(image_rgb, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(image_rgb, (i[0], i[1]), i[2], (0, 0, 0), 3)
    else:
        print("No bottletap on track!")
        x=0
        y=0
        r=0
        
    x=i[0]
    y=i[1]
    r=i[2]
    return x, y ,r, image_rgb

def bottletap(image,x,y,r): # Paints everything outside the circle black!
   for i in np.arange(0, image.shape[0]):
       for j in np.arange(0, image.shape[1]):
            if ((((j-x)**2) + (((i-y)**2))>r**2)):
                image[i, j, 0] = 0
                image[i, j, 1] = 0
                image[i, j, 2] = 0
   return image


def find_track(img):
    img[0:300, :] = 0
    img[520:800, :] = 0
    return img

def getColor(img):
    
    bw_red, color_red = red_mask(img)
    bw_green,color_green = green_mask(img)
    bw_blue,color_blue = blue_mask(img)

    counter_R= np.sum(bw_red == True)
    print(counter_R)
    counter_B= np.sum(bw_blue == True)
    print(counter_B)
    counter_G=np.sum(bw_green == True)
    print(counter_G)

    message=0

    if(counter_R > counter_B) and (counter_R > counter_G):
        message=111

    elif(counter_B > counter_R) and (counter_B > counter_G):
        message=101

    elif (counter_G > counter_R) and (counter_G >> counter_B):
        message=100

    return message


