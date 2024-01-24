from djitellopy import Tello
import cv2
import KeyPressModule as kp
from time import sleep
import os
from datetime import datetime

global img

def getKeyboardInput():
    # left-right, front-back, up-down, yaw-controll
    lr, fb, up, yv = 0, 0, 0, 0
    speed = 30

    if kp.getKey("RIGHT"): lr = speed
    elif kp.getKey("LEFT"): lr = -speed

    elif kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    elif kp.getKey("w"): up = speed
    elif kp.getKey("s"): up = -speed

    elif kp.getKey("d"): yv = speed
    elif kp.getKey("a"): yv = -speed

    elif kp.getKey("o"): tello.takeoff()
    elif kp.getKey("l"): tello.land()

    elif kp.getKey("z"):
        print(img)
        cv2.imwrite(os.path.join(os.getcwd(), f"Resources\\Images\\Tello_{datetime.now().strftime('%Y%m%d-%H%M%S')}.jpg"), img)

    elif kp.getKey("q"):
        frame_read.stop()
        tello.streamoff()

    return [lr, fb, up, yv]

kp.init()
tello = Tello()
tello.connect()
tello.get_battery()
tello.streamoff()
tello.streamon()
frame_read = tello.get_frame_read()
sleep(1)

try:
    while True:
        vals = getKeyboardInput()
        tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
        tello.get_battery()
        img = tello.get_frame_read().frame
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.resize(img, (1280, 720))
        if img is not None:
            cv2.imshow("Video Streaming", img)
        sleep(0.05)

except KeyboardInterrupt:
    print("Program stopped by user keyboard interrupt, landing")
finally:
    tello.land()