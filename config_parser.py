from data_struct.camera_struc import Camera
import configparser

class LocalConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.camera_list = []
        self.load_config()

    def load_config(self):
        self.config.read("setting.ini")

        for cam_type in ["daylight", "thermal"]:
            cam = Camera(
                ip=self.config.get(cam_type, "ip"),
                user=self.config.get(cam_type, "user"),
                password=self.config.get(cam_type, "password"),
                port=self.config.get(cam_type, "port"),
                rtsp_path=self.config.get(cam_type, "rtsp_path")
            )
            self.camera_list.append(cam)

local_config = LocalConfig()