from dataclasses import dataclass

VERSION: float = 0.01

@dataclass
class ScreenConfig:
    SCREEN_WIDTH: int = 288
    SCREEN_HEIGHT: int = 512
    MAX_SCORE_LABEL_SIZE: int = 24
    MAX_SCORE_LABEL_COLOR: tuple[int, int, int] = (255, 255, 255)
    GAME_TITLE: str = "Flappy Waifu (Pygame)"

@dataclass
class DebuggerConfig:
    VISIBLE: bool = True
    FPS_TEXT_SIZE: int = 16
    FPS_TEXT_COLOR: tuple[int, int, int] = (255, 255, 255)

@dataclass
class PhysicConfig:
    GRAVITY: float = 0.5

@dataclass
class PlayerConfig:
    SIZE_X: int = 20
    SIZE_Y: int = 20
    START_POS_X: float = 50
    START_POS_Y: float = 100
    JUMP_STRENGTH: int = 10
