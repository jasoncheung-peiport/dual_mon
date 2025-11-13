class Camera:
    def __init__(self, type, ip, user, password, port, rtsp_path):
        self.type = type
        self.ip = ip
        self.user = user
        self.password = password
        self.port = port
        self.rtsp_path = rtsp_path
        self.rtsp_url = self.get_rtsp_url()

    def get_rtsp_url(self):
        rtsp_url = f"rtsp://{self.user}:{self.password}@{self.ip}:{self.port}/{self.rtsp_path}"
        return rtsp_url
