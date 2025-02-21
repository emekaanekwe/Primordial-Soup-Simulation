

class Agent:
    def __init__(self, id, start_point):
        self.id = id
        self.start_point = start_point
        
                
    def stating_position(self):
        print("sets starting position")
        
    def move(self, direction):
        pos_x, pos_y = direction
        self.start_point[0] = pos_x + self.start_point[0] #should possibly be 2D array 
        self.start_point[0] = pos_y + self.start_point[0]
        
