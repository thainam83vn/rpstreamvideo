import cv2
from  picamera.array import PiRGBArray
from picamera import PiCamera
import time


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = PiCamera()
        self.video.resolution = (640, 480)
        self.video.framerate = 32
        self.rawCapture = PiRGBArray(camera, size=(640,480))
        time.sleep(0.1)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        #self.video.release()
        self.video = None
    
    def get_frame(self):
        #success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        for frame in self.video.capture_continuous(self.rawCapture, format="jpeg", use_video_port=True):
            image = frame.array
            #ret, jpeg = cv2.imencode('.jpg', image)
            jpeg = image
            return jpeg.tobytes()
        return None