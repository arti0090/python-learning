from djitellopy import Tello
import cv2
import KeyPressModule as kp
from time import sleep

kp.init()
tello = Tello()
tello.connect()
tello.get_battery()

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

    return [lr, fb, up, yv]


while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.1)
    img = frame_read.frame
    cv2.imshow('tello', img)

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)