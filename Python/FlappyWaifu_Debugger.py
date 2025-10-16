#wtf
# i use this for Debugging my game :P
#
from pygame.time import Clock
from pygame.font import SysFont
from typing import Callable
import time
from functools import wraps


def Logger(message: str = "LOG MESSAGE", show_args=False, show_timing=False, show_return_Value=False):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if show_args:
                print(f"{func.__name__} ARGS : ")
                for i, arg in enumerate(args):
                    print(f"    arg[{i}] : {arg}")
                for key, value in kwargs.items():
                    print(f"    {key} : {value}")
            print(message)
            start_time = time.time() if show_timing else None
            result = func(*args, **kwargs)
            if show_timing and start_time:
                duration = time.time() - start_time
                print(f"{func.__name__} took : {duration*1000:.2f} ms")
            if show_return_Value:
                print(f"{func.__name__} returned : {repr(result)}")
            return result
        return wrapper
    return decorator

class DebuggerStatus:
    def __init__(self):
        self.Visible = False
        self.Clock = Clock()
        self.font = SysFont("Consolas", 16)
        self.font_color = (255, 255, 255)
        
        self.fps = int(self.Clock.get_fps())
        self.fps_text = self.font.render("FPS: XX", True, self.font_color)
    
    def UpdateStatus(self):
        self.fps = int(self.Clock.get_fps())
        self.fps_text = self.font.render(f"FPS: {self.fps}", True, self.font_color)