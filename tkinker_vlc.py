import tkinter as tk
import vlc

rtsp_url = "rtsp://admin:pw123456@192.168.10.231:554/Streaming/Channels/101"

class myframe(tk.Frame):
    def __init__(self, root, width=500, height=400, bd=5):
        super(myframe, self).__init__(root)
        self.grid()
        self.frame = tk.Frame(self, width=450, height=350, bd=5)
        self.frame.configure(bg="black")
        self.frame.grid(row=0, column=0, columnspan=2, padx=8)
        self.play_button = tk.Button(self, text = 'Play', command = self.play)
        self.play_button.grid(row=1, column=0, columnspan=1, padx=8)
        self.stop_button = tk.Button(self, text = 'Pause', command = self.pause)
        self.stop_button.grid(row=1, column=1, columnspan=1, padx=8)

    def play(self):
        instance = vlc.Instance('--no-xlib --quiet')
        self.player = instance.media_player_new()
        media = instance.media_new(rtsp_url)
        self.player.set_media(media)
        xid = self.frame.winfo_id()
        self.player.set_xwindow(xid)
        self.player.play()

    def pause(self):
        try:
            self.player.pause()
        except:
            pass

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Video Frame Tkinter")
    app = myframe(root)
    root.mainloop()