from  picamera.array import PiRGBArray
from picamera import PiCamera
import time
import threading


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = PiCamera()
        self.video.resolution = (640, 480)
        self.video.framerate = 32
        self.rawCapture = PiRGBArray(self.video, size=(640,480))
        self.threads = []
        time.sleep(0.1)
        t = threading.Thread(target=self.doCamera)
        self.threads.append(t)
        t.start()
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def doCamera(self):
        for frame in self.video.capture_continuous(self.rawCapture, format='jpeg', use_video_port=True):
            image = frame.array
            self.image = image
            self.rawCapture.truncate(0)
            #print("update image")

    def __del__(self):
        #self.video.release()
        self.video.close()
    
    def get_frame(self):
        #success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        #return cv2.imencode('.jpg', self.image)
        return self.image

        #for frame in self.video.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
        #    image = frame.array
        #    ret, jpeg = cv2.imencode('.jpg', image)
        #    return jpeg.tobytes()
        #return None