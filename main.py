import tkinter as tk
from screeninfo import get_monitors
import vlc

rtsp_url = [
    "rtsp://admin:pw123456@192.168.10.231:554/Streaming/Channels/101",  # daylight
    "rtsp://admin:pw123456@192.168.10.231:554/Streaming/Channels/201"   # thermal
]

def play(frame, index):
    instance = vlc.Instance('--no-xlib --quiet')
    player = instance.media_player_new()
    media = instance.media_new(rtsp_url[index])
    player.set_media(media)
    xid = frame.winfo_id()
    player.set_xwindow(xid)
    player.play()
    while True:
        pass

tk_app = []
monitors = get_monitors()
for index in range(len(monitors)):
    screen = monitors[index]
    screen_width = screen.width
    screen_height = screen.height
    screen_x = screen.x
    screen_y = screen.y


    root = tk.Tk()
    root.title(f"Window {index + 1}")
    monitor = monitors[index]
    root.geometry(f"{abs(monitor.width)}x{abs(monitor.height)}+{monitor.x}+{monitor.y}")
    root.overrideredirect(True)
    frame = tk.Frame(width=screen_width, height=screen_height)
    frame.configure(bg="black")
    frame.pack()
    frame.after(5000, play(frame, index))
    # label = tk.Label(root, text=f"Monitor {index + 1}", font=("Helvetica", 30))
    # label.place(relx=0.5, rely=0.5, anchor="center")
    tk_app.append(root)

for app in tk_app:
    app.mainloop()