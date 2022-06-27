from level import Level

class Model:
    """
    Keeps track of the game state.
    
    """
    
    def __init__(self, display_size):
        
        self.level = Level("level1.json")
        self.pos = None
        self.game_pos = self.level.get_starting_pos()
        self.display_size = self.display_width, self.display_height = display_size


    def get_wall_endpoints(self):
        """
        Create a ray from the pos to each of the wall segments to separate out areas
        This will create triangles portraying the visual areas
        :return:
        """
        _endpoints = []
        
        for wall_segment in self.level.get_wall_segments_pixel_coords():
            _endpoints.append(wall_segment["wall_segments"])
            
        return _endpoints
    
    # def compute_intersections(self):
    #     """
    #     Checks if any ray intersects with a wall.
    #     :return:
    #     # """
    #     # [
    #     #     {
    #     #         "closed": false,
    #     #         "wall_segments": [
    #     #             [2.7, 0],
    #     #             [3, 2],
    #     #             [2, 4],
    #     #             [3, 5]
    #     #         ]},
    #     #     {
    #     #         "closed": true,
    #     #         "wall_segments": [
    #     #             [0, 0],
    #     #             [6, 0],
    #     #             [6, 6],
    #     #             [0, 6]
    #     #
    #     #         ]}
    #     # ]
    #     wall_segments = self.level.get_walls()
    #
    #     ray_segments = [(self.pos, endpoint) for endpoint in self.get_wall_endpoints()]  # integer coordinates
    #
    #
    #     doLinesIntersect(LineSegment
    #     a, LineSegment
    #     b) {
    #         Point[]
    #     box1 = a.getBoundingBox();
    #     Point[]
    #     box2 = b.getBoundingBox();
    #     return doBoundingBoxesIntersect(box1, box2)
    #     & & lineSegmentTouchesOrCrossesLine(a, b)
    #     & & lineSegmentTouchesOrCrossesLine(b, a);
    #
    # }
    
    
    
    