import cv2
from screeninfo import get_monitors

from my_enum import CaptureMode

class RTSPStream:
    def __init__(self, rtsp_url: str, monitor_index: int):
        self.rtsp_url = rtsp_url
        self.monitor_index = monitor_index
        self.set_resolution()
        self.init_camera()

    def init_camera(self):
        if hasattr(self, 'cap') and self.cap:
            self.cap.release()
        self.cap = cv2.VideoCapture(self.rtsp_url)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.monitor_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.monitor_height)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'XVID')) 
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    def set_resolution(self):
        monitor = get_monitors()[self.monitor_index]
        self.monitor_width = monitor.width
        self.monitor_height = monitor.height
        self.monitor_x = monitor.x
        self.monitor_y = monitor.y
        cv2.namedWindow(f'Screen {self.monitor_index}', cv2.WINDOW_NORMAL)
        cv2.moveWindow(f'Screen {self.monitor_index}', monitor.x, monitor.y)
        cv2.setWindowProperty(f'Screen {self.monitor_index}', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def start_stream(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to read frame")
                self.init_camera()
                continue

            cv2.imshow(f'Screen {self.monitor_index}', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Example
if __name__ == "__main__":
    stream = RTSPStream(CaptureMode.DAYLIGHT, monitor_index=0)
    stream.start_stream()
