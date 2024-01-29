import pygame
pygame.init()

class VolumeSlider:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.volume = pygame.mixer.music.get_volume()
        self.font = pygame.font.Font("fonts/Oswald.ttf", 24)
        self.hpfont = pygame.font.Font("fonts/Oswald.ttf", 14)
        self.dragging = False  # Add a flag to track whether the slider is being dragged

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, self.rect.y, self.volume * self.rect.width, self.rect.height))

        volume_text = self.hpfont.render(f'{int(self.volume * 100)}', True, (0, 0, 0)) 
        volume_text_rect = volume_text.get_rect(center=(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)) 
        screen.blit(volume_text, volume_text_rect) 
        
        volume_label = self.font.render('Volume', True, (0, 0, 0))
        volume_label_rect = volume_label.get_rect(center=(self.rect.x + self.rect.width // 2, (self.rect.y - volume_label.get_height()) + 20)) 
        screen.blit(volume_label, volume_label_rect) 
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False 
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.volume = min(max((event.pos[0] - self.rect.x) / self.rect.width, 0), 1)
                pygame.mixer.music.set_volume(self.volume)
