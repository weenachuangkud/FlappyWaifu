from enum import Enum

class InputAction(Enum):
    JUMP = "jump"
    RESTART = "restart"
    QUIT = "quit"
    
class Sounds(Enum):
    JumpSound = "Assets\\Sounds\\JumpSound.mp3"