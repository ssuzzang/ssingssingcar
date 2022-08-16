import cv2
from hj_opencv_lane_detect import HjOpencvLaneDetect
import os 

cv_detector = HjOpencvLaneDetect()
video_file = "data/car_video.avi"
cap = cv2.VideoCapture(video_file)

index = 0
try:
    os.system("rm ./data/*.png")  
except OSError:
    print("No *.png files")

while True:
    ret, img_org = cap.read()
    if ret:
        lanes, img_lane = cv_detector.get_lane(img_org)
        cv2.imshow("img", img_org)
        angle, img_angle = cv_detector.get_steering_angle(img_lane, lanes)
        if img_angle is None:
            print("can't find lane...")
        else:
            cv2.imwrite("%s_%03d_%03d.png" % (video_file, index, angle), img_org)
            index += 1	
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("camera error")
        break

cap.release()
cv2.destroyAllWindows()




