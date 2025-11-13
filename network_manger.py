import subprocess
import platform

class NetworkManager:
    def is_window_os(self):
        if platform.system() == "Windows":
            return True
        return False

    def is_device_online(self, ip):
        is_window = self.is_window_os()
        if is_window:
            command = ['ping', '-n', '1', ip]  # Windows
        else:
            command = ['ping', '-c', '1', ip]  # Linux/Mac

        try:
            subprocess.run(command)
            print("Device online")  # Print status message
            return True
        except subprocess.CalledProcessError:
            print("Device offline")  # Print status message
            return False

network_manager = NetworkManager()

if __name__ == "__main__":
    network_manager.is_device_online("192.168.10.231")