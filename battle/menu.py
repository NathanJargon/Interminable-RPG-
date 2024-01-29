import pygame
import time

class Menu:
    KEY_PRESS_DELAY = 0.2
    
    def __init__(self, options):
        self.options = options
        self.state = 0
        self.option_rects = []
        self.last_key_press_time = 0 

    def handle_event(self, event):
        current_time = time.time()
        if event.type == pygame.KEYDOWN:
            if current_time - self.last_key_press_time > self.KEY_PRESS_DELAY:
                if event.key == pygame.K_LEFT:
                    self.state = max(0, self.state - 1)
                elif event.key == pygame.K_RIGHT:
                    self.state = min(len(self.options) - 1, self.state + 1)
                self.last_key_press_time = current_time
        elif event.type == pygame.MOUSEMOTION:
            for i, rect in enumerate(self.option_rects):
                if rect.collidepoint(event.pos):
                    self.state = i
        print(f"Current state: {self.state}, Selected skill: {self.options[self.state]}") 
        return self.options[self.state]

    def draw(self, screen, font):
        total_width = sum(font.size(option)[0] + 100 for option in self.options[:len(self.options)//2]) - 100
        if len(self.options) <= 3:
            x = (screen.get_width() // 2 - total_width // 2) - 150
            y = screen.get_height() - 60
        else:
            x = screen.get_width() // 2 - total_width // 2
            y = screen.get_height() - 120
        self.option_rects = []
        for i, option in enumerate(self.options):
            if i == len(self.options) // 2 and len(self.options) > 3:  
                y += 60  
                x = screen.get_width() // 2 - total_width // 2  
            color = (0, 255, 255) if i == self.state else (0, 0, 0)
            text = font.render(option, True, color)
            rect = screen.blit(text, (x, y))
            self.option_rects.append(rect)
            x += font.size(option)[0] + 100