from rtsp_stream import RTSPStream
from my_enum import CaptureMode
import sys

if len(sys.argv) != 2:
    print("Usage: python main.py <monitor_index>")
    sys.exit(1)

try:
    monitor_index = int(sys.argv[1])
except ValueError:
    print("Monitor index must be an integer.")
    sys.exit(1)

stream = RTSPStream(CaptureMode.index(monitor_index).value, monitor_index=monitor_index)
stream.start_stream()
