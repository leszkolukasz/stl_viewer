from render.render_ascii import RenderAscii
from render.render_dotted import RenderDotted

class RenderManager():
    def __init__(self, root, mesh, dotted_view, ascii_view, mode, resolution):
        self.root = root
        self.mesh = mesh
        self.dotted_view = dotted_view
        self.ascii_view = ascii_view
        self.mode = mode
        self.resolution = resolution
        self.renderers = dict(dotted=RenderDotted(self.dotted_view, self.mesh), ascii=RenderAscii(self.ascii_view, self.mesh))
        self.current_renderer = self.renderers['dotted']
        
    def change_mode(self):
        print(self.mode.get())
        
        if self.mode.get() == 'dotted':
            self.ascii_view.grid_forget()
            self.dotted_view.grid(row=0, column=0, sticky='nswe')
            
        if self.mode.get() == 'ascii':
            self.dotted_view.grid_forget()
            self.ascii_view.grid(row=0, column=0, sticky='nswe')
            
        self.current_renderer = self.renderers[self.mode.get()]
        self.render()
        
    def change_resolution(self, val):
        print(self.resolution.get())
        
    def render(self):
        print('Rendering...')
        self.current_renderer.render()