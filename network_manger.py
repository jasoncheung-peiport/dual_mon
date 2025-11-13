import subprocess

class NetworkManager:
    def is_device_online(self, ip):
        command = ['ping', "-n", "1", ip]  # Window
        try:
            subprocess.run(command)
            print("device online")# Resume playing if the player was paused
            return True
        except subprocess.CalledProcessError:
            print("device offline")
            return False 

network_manager = NetworkManager()

if __name__=="__main__":
    network_manager.check_device_online("192.168.10.231")