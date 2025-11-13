from camera.camera_struc import Camera

camera = [
    # daylight
    {
        "type": "daylight",
        "ip": "192.168.10.231",
        "user": "admin",
        "password": "pw123456",
        "port": "554",
        "rtsp_path": "/Streaming/Channels/101"
    },  
    # thermal
    {
        "type": "thermal",
        "ip": "192.168.10.231",
        "user": "admin",
        "password": "pw123456",
        "port": "554",
        "rtsp_path": "Streaming/Channels/201"
    },
]

camera_list: Camera = []
for camera in camera:
    camera_list.append(
        Camera(
            type=camera["type"],
            ip=camera["ip"],
            user=camera["user"],
            password=camera["password"],
            port=camera["port"],
            rtsp_path=camera["rtsp_path"]
        )
    )