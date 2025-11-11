import cv2
from config import rtsp_url

class RTSPController:
    def __init__(self, mode_index):
        self.cap = cv2.VideoCapture(rtsp_url[mode_index])

    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Could not read frame from RTSP stream.")
            return None
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return cv2.flip(rgb_frame, 0)
