from pygame import draw
from constants import DISPLAY_WIDTH, DISPLAY_HEIGHT
import json


class Level:
    
    def __init__(self, file_path):
        self.level_info = None
        self.w = None
        self.h = None
        self.walls_cpu = None  # pre-compute the pixel positions of the wall vertices
        self.walls = None
        self.load_level(file_path)
        
    def load_level(self, file_path):
        with open(file_path, "r") as f:
            self.level_info = json.load(f)
            
        self.w = DISPLAY_WIDTH / self.level_info["board_size"]["width"]
        self.h = DISPLAY_HEIGHT / self.level_info["board_size"]["height"]
        self.walls = self.level_info["walls"]
        
        self.walls_cpu = self.calculate_walls(self.level_info["walls"])
        
    # def get_wall_
    
    def calculate_walls(self, walls):
        """
        walls:
        [
            {
              "closed":  false,
              "wall_segments":  [
                [2.7, 0],
                [3, 2],
                [2, 4],
                [3, 5]
            ]},
            {
              "closed":  true,
              "wall_segments":  [
                [0, 0],
                [6, 0],
                [6, 6],
                [0, 6]
        
            ]}
        ]
        """
        _out = []
        for wall_seg in walls:
            _out.append({
                "closed": wall_seg["closed"],
                "wall_segments": [[int(x * self.w), int(y * self.h)] for x, y in wall_seg["wall_segments"]]
            })
        return _out
        
    def get_wall_segments_pixel_coords(self):
        return self.walls_cpu
    
    def get_starting_pos(self):
        return self.level_info["starting_pos"]
    
    def draw_to_surface(self, surf):
        # Draw the grid lines
        for c in range(1, self.level_info["board_size"]["width"]):
            start_pos = (c * self.w, 0)
            end_pos = (c * self.w, DISPLAY_HEIGHT)
            draw.line(surf, (255, 255, 255), start_pos, end_pos, width=1)
        for r in range(1, self.level_info["board_size"]["height"]):
            start_pos = (0, r * self.h)
            end_pos = (DISPLAY_WIDTH, r * self.h)
            draw.line(surf, (255, 255, 255), start_pos, end_pos, width=1)
            
        # Draw the walls in
        # The walls is a list of objects like:
        # {"closed": true,
        #  "wall_segments": [
        #      [0, 0],
        #      [4, 0],
        #      [4, 5],
        #      [0, 5]
        #  ]}
            walls = self.get_wall_segments_pixel_coords()
            for wall_seg in walls:
                points = wall_seg["wall_segments"]
                draw.lines(
                    surface=surf,
                    color=(255, 0, 255),
                    closed=wall_seg["closed"],
                    points=points,
                    width=5
                )
        
        
        
            

