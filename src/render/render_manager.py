class RenderManager():
    def __init__(self, root, dotted_view, ascii_view, mode, resolution):
        self.root = root
        self.dotted_view = dotted_view
        self.ascii_view = ascii_view
        self.mode = mode
        self.resolution = resolution
        
    def change_mode(self):
        print(self.mode.get())
        
    def change_resolution(self, val):
        print(self.resolution.get())