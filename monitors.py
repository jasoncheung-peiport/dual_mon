from screeninfo import get_monitors

class Monitors():
    def __init__(self):
        self.update_monitor_info()

    def update_monitor_info(self):
        self.monitors = get_monitors()

monitors = Monitors()
