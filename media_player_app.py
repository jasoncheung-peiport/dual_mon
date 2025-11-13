import vlc
from screeninfo import Monitor

import tkinter as tk

from camera.camera_struc import Camera
from network_manger import network_manager

NETWORK_CACHE = 100
PING_INTERVAL = 5000 # milliseconds

class MediaPlayerApp:
    def __init__(self, master: tk.Tk, monitor: Monitor, camera: Camera):
        self.master = master
        self.monitor = monitor
        self.camera = camera
        master.title("Peiport Player")
        self.set_player()
        
        self.master.after(1000, self.check_device_online)

    def set_player(self):
        self.instance = vlc.Instance(f"--network-caching={NETWORK_CACHE}")
        self.player = self.instance.media_player_new()
        self.video_frame = tk.Frame(self.master, bg="black", width=self.monitor.width, height=self.monitor.height)
        if self.master.winfo_exists():
            self.player.set_hwnd(self.video_frame.winfo_id())
        self.video_frame.pack()
        self.media = self.instance.media_new(self.camera.rtsp_url)
        self.player.set_media(self.media)
        self.master.after(1000, self.play_video)

    def play_video(self):
        self.player.play()

    def check_device_online(self):
        # Check if the player is actively playing content
        is_playing = self.player.get_state() == vlc.State.Playing
        
        if is_playing:
            self.master.after(PING_INTERVAL, self.check_device_online)
            return
        
        # Check if the device is online
        is_online = network_manager.is_device_online(self.camera.ip)

        if is_online:
            # Reset the media and play the video
            self.media = self.instance.media_new(self.camera.rtsp_url)
            self.player.set_media(self.media)
            self.play_video()

        self.master.after(PING_INTERVAL, self.check_device_online)
