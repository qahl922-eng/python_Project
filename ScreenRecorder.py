import numpy as np
import pyautogui
import cv2
import time


# resolution = (1920, 1080)
# codec = cv2.VideoWriter_fourcc(*"XVID")
# Fps = 11.55

# video = cv2.VideoWriter("Recording.avi", codec, Fps, resolution)
# cv2.namedWindow('Live', cv2.WINDOW_NORMAL)           #    Note if the window name 'Live' in this case is different inside and outside the
# cv2.resizeWindow('Live', (1280, 720))                #    loop than everytime a loop runs, a new window will be created.

# while True:
#     time1 = time.time() 

#     img = pyautogui.screenshot()
#     frame = np.array(img)
#     frame1 = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#     video.write(frame1)

#     cv2.imshow('Live', frame1)                        #    Keep the window name exactly same, b/c its case sensitive.

#     time2 = time.time() - time1
#     sleeptime = 0.08656 - time2
#     if sleeptime > 0:
#         time.sleep(sleeptime)


#     if cv2.waitKey(1) == ord('q'):                    #    The full form of the ord function in Python stands for "ordinal".
#         break

# video.release()
# cv2.destroyAllWindows()

   


'''Screen Recorder + Webcam Overlay(on my own)'''

# resolution1 = (1920, 1080)
# fps1 = 11.55
# codec = cv2.VideoWriter_fourcc(*'XVID')

# screen = cv2.VideoWriter('WEBCAM_REC.avi', codec, fps1, resolution1)
# cv2.namedWindow('Live', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Live', (1280, 720))

# cam = cv2.VideoCapture(2)                 # Default webcam is at 2.

# while True:

#     time0 = time.time()

#     img =  pyautogui.screenshot()
#     frame0 = np.array(img)
#     frame12 = cv2.cvtColor(frame0, cv2.COLOR_RGB2BGR)

#     ret, webcam_frame = cam.read()
#     small_cam = cv2.resize(webcam_frame, (640, 360))
#     frame12[0:360, 0:640] = small_cam
#     screen.write(frame12)
    

#     cv2.imshow('Live', frame12)

#     time12 = time.time() - time0
#     sleeptime = 1/fps1 - time12 
#     if sleeptime > 0:
#         time.sleep(sleeptime)

#     if cv2.waitKey(1) == ord("q"):
#         break


# cam.release()
# screen.release()
# cv2.destroyAllWindows()




resolution = (1920, 1080)
fPs = 11.50
codec = cv2.VideoWriter.fourcc(*"XVID")
filename  = 'Myrecord.avi'

vid = cv2.VideoWriter(filename,  codec, fPs, resolution)

cv2.namedWindow('Live', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Live', 1280, 720)

while True:

    time1 = time.time()


    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    vid.write(frame)

    cv2.imshow('Live', frame)

    time2 = time.time() - time1
    sleeptime = 1/11.55 - time2
    if sleeptime > 0:
        time.sleep(sleeptime)

    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

    