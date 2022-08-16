import cv2
import os 
from adafruit_servokit import ServoKit
from hj_opencv_lane_detect import HjOpencvLaneDetect
from hj_car_motor_l9110 import HjCarMotorL9110

servo = ServoKit(channels=16)
cv_detector = HjOpencvLaneDetect()
motor = HjCarMotorL9110()


cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

try:
    if not os.path.exists('./data'):
        os.makedirs('./data')
except OSError:
    print("failed to make ./data folder")
    
fourcc =  cv2.VideoWriter_fourcc(*'XVID')
video_orig = cv2.VideoWriter('./data/car_video.avi', fourcc, 20.0, (320, 240))

servo_offset = 1
servo.servo[0].angle = 90 + servo_offset

for i in range(30):
    ret, img_org = cap.read()
    if ret:
        lanes, img_lane = cv_detector.get_lane(img_org)
        angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
        if img_angle is None:
            print("can't find lane...")
            pass
        else:
            print(angle)
            servo.servo[0].angle = angle + servo_offset			
    else:
        print("camera error")
motor.motor_move_forward(30)

while True:
    ret, img_org = cap.read()
    if ret:
        video_orig.write(img_org)
        lanes, img_lane = cv_detector.get_lane(img_org)
        angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
        if img_angle is None:
            print("can't find lane...")
            pass
        else:
            cv2.imshow('lane', img_angle)
            print(angle)
            servo.servo[0].angle = angle + servo_offset
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("cap error")
motor.motor_stop()
cap.release()
video_orig.release()
cv2.destroyAllWindows()


