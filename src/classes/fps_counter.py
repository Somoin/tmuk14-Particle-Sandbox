class fps_counter:
    def __init__(self, window, font, clock, color, pos):
        self.window = window
        self.font = font
        self.clock = clock
        self.color = color
        self.pos = pos

        self.fps_text = self.font.render("FPS: 0", False, self.color)
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1]))   

    def render(self):
        self.window.blit(self.fps_text, self.fps_text_rect) # Render the fps_counter
    
    def update(self):
        self.fps_text = self.font.render(f"FPS: {self.clock.get_fps():2.0f}", False,  self.color) # Update the fps text
        self.fps_text_rect = self.fps_text.get_rect(center=(self.pos[0], self.pos[1])) # Update the pos of text rect
        