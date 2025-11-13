import tkinter as tk
from camera.camera_data import camera_list
from monitors import monitors
from media_player_app import MediaPlayerApp

NETWORK_CACHE = 50
root_list = []

if __name__=="__main__":

    for index in range(len(monitors.monitors)):
        root = tk.Tk()
        root.geometry(f"{abs(monitors.monitors[index].width)}x{abs(monitors.monitors[index].height)}+{monitors.monitors[index].x}+{monitors.monitors[index].y}")
        root.overrideredirect(True)
        app = MediaPlayerApp(root, monitor=monitors.monitors[index], camera=camera_list[index])
        root_list.append(root)

    for root in root_list:
        root.mainloop()
