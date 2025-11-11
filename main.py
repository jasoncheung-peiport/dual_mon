import sys
from rtsp_controller import RTSPController
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from screeninfo import get_monitors

MODE = None  # Global variable to store the selected mode

class CameraApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = Image()
        self.add_widget(self.image)
        self.controller = RTSPController(int(MODE))  # 0 for daylight, 1 for thermal  
        
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # Update the image every 1/30 seconds

    def update(self, dt):
        frame = self.controller.read_frame()  # OpenCV capture object
        
        if frame is None:
            return

        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]))
        image_texture.blit_buffer(frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        if image_texture:
            self.image.texture = image_texture

class MonitorApp(App):
    def build(self):
        return CameraApp()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python main.py <mode>")
        sys.exit(1)

    MODE = sys.argv[1]
    if MODE not in ['0', '1']:
        print("Invalid mode. Please enter '0' for daylight or '1' for thermal.")
        sys.exit(1)

    monitors = get_monitors()
    target_monitor = monitors[int(MODE)]  # Assuming Monitor 0 is the first monitor
    Window.size = (target_monitor.width, target_monitor.height)

    Window.top = target_monitor.y
    Window.left = target_monitor.x
    
    MonitorApp().run()