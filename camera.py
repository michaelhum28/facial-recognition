# camera.py

import cv2
from threading import Thread

class Camera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                self.frame = frame

    def get_frame(self):
        return self.frame
