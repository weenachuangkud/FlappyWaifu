class Physic:
    gravity : float = 0.5

class Vector2:
    x = 0
    y = 0

    def __init__(self, x : float =0, y : float = 0):
        self.x = x
        self.y = y

class CollisionObject:

    def __init__(self):
        super().__init__()
        self.CanCollide = True
        self.CanTouch = True

class PhysicObject(Physic):

    def __init__(self):
        super().__init__()
        self.velocity = Vector2()

    def ApplyForce(self, x : float, y : float):
        self.velocity.x += x
        self.velocity.y += y

class CFrame:
    def __init__(self):
        self.Position = Vector2()

    def SetPos(self, x : float, y : float):
        self.Position.x = x
        self.Position.y = y

    @property
    def x(self):
        return self.Position.x

    @x.setter
    def x(self, value):
        self.Position.x = value

    @property
    def y(self):
        return self.Position.y

    @y.setter
    def y(self, value):
        self.Position.y = value

class Object(PhysicObject, CollisionObject, CFrame):

    def __init__(self):
        super().__init__()
        self.Name = ""
        self.Size = Vector2()  # width and height
