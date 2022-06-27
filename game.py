from constants import *
import pygame
from model import Model


class App:
    
    def __init__(self):
        self.screen_size = self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.display_size = self.display_width, self.display_height = DISPLAY_WIDTH, DISPLAY_HEIGHT
        
        self._screen = None
        self._display_surf = None
        self._running = True
        self.mouse_pos = None
        
        self.model = Model(self.display_size)
    
    def draw_background(self):
        self._screen.fill(BACKGROUND_COLOR)
        self._display_surf.fill(FOREGROUND_COLOR)
        
    def display_gamestate(self):
        self.model.level.draw_to_surface(self._display_surf)
        
        rays = self.model.get_wall_endpoints()
        for wall_endpoints in rays:
            for endpoint in wall_endpoints:
                print(endpoint)
                pygame.draw.aaline(self._display_surf, (255, 211, 0), self.model.pos, endpoint)
                pygame.draw.circle(self._display_surf, (0, 200, 0), endpoint, 5)

        self._screen.blit(self._display_surf, dest=(BUFFER, BUFFER))
        
    def on_init(self):
        pygame.init()
        
        self._screen = pygame.display.set_mode(self.screen_size)
        self._display_surf = pygame.Surface(self.display_size)
        
        self._running = True
        
        self.draw_background()
        pygame.display.update()
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        print(event)
            
    def on_loop(self):
        # mouse_pos is set in mouse-coordinates, we want to find game-coordinates
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        display_pos = display_x, display_y = mouse_x - BUFFER, mouse_y - BUFFER
        display_pos = self.bound_point_to_within(display_pos, 0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        game_pos = game_x, game_y = display_x / self.model.level.w, display_x / self.model.level.h
        game_pos = self.bound_point_to_within(game_pos, 0, 0, self.model.level.level_info["board_size"]["width"],
                                   self.model.level.level_info["board_size"]["height"])
        
        self.model.pos = display_pos
        self.model.game_pos = game_pos
        
    def bound_point_to_within(self, pt, x1, y1, x2, y2):
        x, y = pt
        if x <= x1:
            x = x1
        if x >= x2:
            x = x2
        if y <= y1:
            y = y1
        if y >= y2:
            y = y2
        return x, y
            
    
    def on_render(self):
        self.draw_background()
        self.display_gamestate()
        pygame.display.update()
        
    def on_cleanup(self):
        pygame.quit()
    
    def on_execute(self):
        
        self.on_init()
            
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            
        self.on_cleanup()
    
    
if __name__ == '__main__':
    app = App()
    app.on_execute()
    