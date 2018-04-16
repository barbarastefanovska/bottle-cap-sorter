import serial
import cv2
import numpy as np
import IDcircle as idc
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import picamera


def main():
    #Open camera to wiev image
    cap = cv2.VideoCapture(0)
    #ser = serial.Serial('/dev/ttyACM0',9600)
    #print(ser.name)
    while (True):
        
        print("Photo capiture: ")
        ret , img_RGB = cap.read()
   
        print("Preparing images:")
        #img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

        img_RGB =  idc.find_track(img_RGB)
        cv2.imshow('Track Found',img_RGB)

        #Oimg_bottletap = idc.find_bottletap(img_RGB)
        #Omask_red, img_bottletap = idc.red_mask(img_bottletap)
        cv2.imshow('Bottletap found', img_RGB)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    ser.close()
    cap.release()
    cv2.destroyAllWindows()
    print("Process ended!")


if __name__ == '__main__':
    print("Running program...")
    main()  