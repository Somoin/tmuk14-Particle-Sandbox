class Particle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update(self):
        raise NotImplementedError("update method not implemented")

