import picamera

import time
import cv2
camera = picamera.PiCamera()
camera.start_preview(fullscreen=False, window = (10, 10, 640, 480))

for filename in camera.capture_continuous('image{counter:03d}.jpg'):
    print('Photo name: %s' % filename)
    #time.sleep(0.5) #wait 2 seconds
    exit_code = str(input())
    if exit_code == 'q':
        camera.stop_preview()
        camera.close()
        break

#cv2.waitkey(0)
