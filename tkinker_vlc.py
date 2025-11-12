import tkinter as tk
import vlc
from screeninfo import get_monitors

rtsp_url = "rtsp://admin:pw123456@192.168.10.231:554/Streaming/Channels/101"

screen = get_monitors()[0]
screen_width = screen.width
screen_height = screen.height
screen_x = screen.x
screen_y = screen.y

class MyFrame(tk.Frame):
    def __init__(self, root):
        super(MyFrame, self).__init__(root)
        self.grid()
        self.frame = tk.Frame(self, width=screen_width, height=screen_height)
        self.frame.configure(bg="black")
        self.frame.pack()

    def play(self):
        instance = vlc.Instance('--no-xlib --quiet')
        self.player = instance.media_player_new()
        media = instance.media_new(rtsp_url)
        self.player.set_media(media)
        xid = self.frame.winfo_id()
        self.player.set_xwindow(xid)
        self.player.play()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Video Frame Tkinter")
    root.overrideredirect(True)
    app = MyFrame(root)
    app.after(1000, app.play())
    root.mainloop()