import pygame
import sys
from typing import List, Callable

from FlappyWaifu_Enums import *
from FlappyWaifu_Object import Object
from FlappyWaifu_Debugger import Logger
from FlappyWaifu_Debugger import DebuggerStatus

# im such a fat ass boy
class Game:
    version : float = 0.01

    SCREEN_WIDTH : int = 288
    SCREEN_HEIGHT : int = 512

    title : str = "Flappy Waifu (Pygame) v" + str(version)

    def __init__(self):
        pygame.init()
        self.Screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.title)
        print(f"Starting Game.. \n Version : {self.version}")
        self.Player : Player = Player()

        self.InputHandler : InputHandler = InputHandler()
        self.InputHandler.bind_action(InputAction.JUMP, self.Player.jump)
        self.InputHandler.bind_action(InputAction.RESTART, self.restart)
        self.InputHandler.bind_action(InputAction.QUIT, self.quit_game)

        self.pipes = []
        self.highestScore : int = 0
        self.game_over = False
        
        self.DebuggerStatus = DebuggerStatus()
        self.DebuggerStatus.Visible = True

        self.IsRunning : bool = True

    def Start(self):
        while self.IsRunning:
            self.update()
            self.draw()
            self.DebuggerStatus.Clock.tick(60)

    def update(self):
        if not self.game_over:
            self.Player.update()
            # Update pipes
            for pipe in self.pipes:
                pipe.update()
            # Check collisions
            if self.check_collisions():
                self.game_over = True
        self.InputHandler.handle_events()
        self.DebuggerStatus.UpdateStatus()

    def draw(self):
        self.Screen.fill((135, 206, 235))  # Sky blue background
        self.Player.draw(self.Screen)
        for pipe in self.pipes:
            pipe.draw(self.Screen)
        if self.DebuggerStatus.Visible:
            self.Screen.blit(self.DebuggerStatus.fps_text, (self.SCREEN_WIDTH - self.DebuggerStatus.fps_text.get_width(), self.SCREEN_HEIGHT - self.DebuggerStatus.fps_text.get_height()))
        pygame.display.flip()

    @Logger("Collision Check", show_timing=True)
    def check_collisions(self):
        # Simple collision with ground
        if self.Player.y + self.Player.Size.y >= self.SCREEN_HEIGHT:
            return True
        # Collision with pipes (to be implemented)
        # For future pipes, if pipe.CanTouch and collision, trigger jump
        for pipe in self.pipes:
            if pipe.CanTouch and self.player_collides_with(pipe):
                self.Player.jump()
        return False

    def player_collides_with(self, obj):
        # Simple AABB collision detection
        return (self.Player.x < obj.x + obj.Size.x and
                self.Player.x + self.Player.Size.x > obj.x and
                self.Player.y < obj.y + obj.Size.y and
                self.Player.y + self.Player.Size.y > obj.y)

    def restart(self):
        self.Player = Player()
        self.pipes = []
        self.score = 0
        self.game_over = False

    def quit_game(self):
        self.IsRunning = False

    def SpawnPipe(self):
        # Spawn Pipe
        pass

class Player(Object):
    def __init__(self):
        super().__init__()
        # This is so fucking obv lmao
        self.jump_strength = -10
        self.x = 50
        self.y = 100
        # Load character image
        self.image = pygame.image.load("Python\\Assets\\Characters\\Character1.jpg").convert_alpha()
        # Set desired Size for the player
        self.Size.x = 20
        self.Size.y = 20
        # Scale image to match the Size
        self.image = pygame.transform.scale(self.image, (self.Size.x, self.Size.y))
        # Load jump sound
        self.jump_sound = pygame.mixer.Sound("Python\\Assets\\Sounds\\JumpSound.mp3")

    def update(self):
        self.velocity.y += self.gravity
        self.y += self.velocity.y

    def jump(self):
        self.velocity.y = self.jump_strength
        self.jump_sound.play()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Pipe(Object):
    pass

    
class InputHandler:
    def __init__(self):
        self.key_bindings = {
            pygame.K_SPACE : InputAction.JUMP,
            pygame.K_r : InputAction.RESTART,
            pygame.K_ESCAPE : InputAction.QUIT
        }
        
        self.callbacks : dict[InputAction, List[Callable]] = {
            action : [] for action in InputAction
        }
    
    def bind_action(self, action: InputAction, callback: Callable):
        """Bind a callback to an input action"""
        self.callbacks[action].append(callback)
        
    def unbind_action(self, action : InputAction):
        """Unbind Specific InputAction"""
        if len(self.callbacks[action]) == 0:
            print("Action is not Binded")
            return
        self.callbacks[action]
        
    def trigger_action(self, action : InputAction):
        """Execute all callbacks for given action"""
        for callback in self.callbacks[action]:
            callback()
        
    def handle_events(self) -> bool:
        """Process all pygame events and trigger callbacks"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.trigger_action(InputAction.QUIT)
                return False

            if event.type == pygame.KEYDOWN:
                if event.key in self.key_bindings:
                    action = self.key_bindings[event.key]
                    self.trigger_action(action)
        return True
class Render:
    pass