import cv2
import numpy as np
import math
import tensorflow as tf
from keras.models import load_model

_SHOW_IMAGE = False

class HjDeepLaneDetect(object):

    def __init__(self, model_path):
        self.curr_steering_angle = 90
        if model_path is None:
            print("wrong model path!")
            return 
        else:
            self.model = load_model(model_path)
    
    def follow_lane(self, frame):
        show_image("orig", frame)
        self.curr_steering_angle = self.compute_steering_angle(frame)
        final_frame = display_heading_line(frame, self.curr_steering_angle)
        return self.curr_steering_angle, final_frame 

    def compute_steering_angle(self, frame):
        preprocessed = img_preprocess(frame)
        X = np.asarray([preprocessed])
        steering_angle = self.model(X, training=False)[0]
        return int(steering_angle + 0.5) 

def img_preprocess(image):
    height, _, _ = image.shape
    image = image[int(height/2):,:,:]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)  
    image = cv2.GaussianBlur(image, (3,3), 0)
    image = cv2.resize(image, (200,66))
    image = image / 255 
    return image

def display_heading_line(frame, steering_angle, line_color=(0, 0, 255), line_width=5, ):
    heading_image = np.zeros_like(frame)
    height, width, _ = frame.shape

    try:
        steering_angle_radian = steering_angle / 180.0 * math.pi
        x1 = int(width / 2)
        y1 = height
        x2 = int(x1 - height / 2 / math.tan(steering_angle_radian))
        y2 = int(height / 2)

        cv2.line(heading_image, (x1, y1), (x2, y2), line_color, line_width)
        heading_image = cv2.addWeighted(frame, 0.8, heading_image, 1, 1)
    except:
       pass 

    return heading_image

def show_image(title, frame, show=_SHOW_IMAGE):
    if show:
        cv2.imshow(title, frame)
