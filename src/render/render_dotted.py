from render.render import Render

class RenderDotted(Render):
    def __init__(self, window, mesh):
        self.window = window
        self.mesh = mesh
    
    def render(self):
        z = 200
        Z = 205
        scale = 700
        points = self.mesh.get_points()
        normals = self.mesh.get_normals()
        self.window.create_rectangle(0, 0, self.window.winfo_width(), self.window.winfo_height(), fill='black')
        
        for i in range(len(points)):
            projection = [0, 0]
            projection[0] = points[i,0]*z/(points[i, 2] + Z)
            projection[1] = points[i,1]*z/(points[i, 2] + Z)
            projection[0] = int(scale*projection[0])
            projection[1] = int(scale*projection[1])
            
            print(projection)
            
            if projection[0] >= 0 and projection[1] >= 0 and projection[0] <= self.window.winfo_width() and projection[1] <= self.window.winfo_height():
                self.window.create_oval(projection[0]-2, projection[1]-2, projection[0]+2, projection[1]+2, fill='white')
            
            
        