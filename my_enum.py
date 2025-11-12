from enum import Enum
from config import rtsp_url

class CaptureMode(Enum):
    DAYLIGHT = rtsp_url[0]
    THERMAL = rtsp_url[1]

    @classmethod
    def index(cls, index):
        return list(cls)[index]
    
# Example usage
if __name__ == "__main__":
    index = 0
    mode = CaptureMode.index(index)
    print(
        f"""
        index: {index}
        name: {mode.name}
        value: {mode.value}
        """
    )