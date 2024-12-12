

class Agent:
    def __init__(self, id, start_point):
        self.id = id
        self.start_point = start_point
        
                
    def stating_position(self):
        print("sets starting position")
        
    def move(self, direction):
        x, y = direction
        self.start_point[0] = x + self.start_point[0] = y