import cv2
from adafruit_servokit import ServoKit
from hj_deep_lane_detect import HjDeepLaneDetect
from hj_car_motor_l9110 import HjCarMotorL9110
import time

deep_detector = HjDeepLaneDetect("./models/LIW2_cv_lane_navigation_final.h5")
motor = HjCarMotorL9110()
servo = ServoKit(channels=16)

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

servo_offset = 5
servo.servo[0].angle = 90 + servo_offset

for i in range(30):
    ret, img_org = cap.read()
    if ret:
        angle_deep, img_angle = deep_detector.follow_lane(img_org)
        if img_angle is None:
            print("can't find lane...")
        else:
            print(angle_deep)
            if angle_deep > 40 and angle_deep < 140:
                servo.servo[0].angle = angle_deep + servo_offset	
            		
            cv2.imshow("img_angle", img_angle)
            cv2.waitKey(1)
    else:
        print("cap error")

motor.motor_move_forward(20)

while cap.isOpened():
    ret, img_org = cap.read()
    angle_deep, img_angle = deep_detector.follow_lane(img_org)
    if img_angle is None:
        print("can't find lane...")
    else:
        print(angle_deep)
        if angle_deep > 30 and angle_deep < 160:
            servo.servo[0].angle = angle_deep + servo_offset
        cv2.imshow("img_angle", img_angle)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
motor.motor_stop()
cap.release()
cv2.destroyAllWindows()



        

