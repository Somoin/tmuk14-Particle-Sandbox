class Particle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update(self):
        raise NotImplementedError("update method not implemented")

class SandParticle(Particle):
    def __init__(self):
        super().__init__("sand", (194, 178, 128))
    
    def update(self):
        pass