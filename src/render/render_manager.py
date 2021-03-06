from render.render_ascii import RenderAscii
from render.render_dotted import RenderDotted
import tkinter as tk

class RenderManager():
    """
    Variables
    ---------
    renderers: Dict[Render]
        dictionary of all available renderers
    delta: Dict[str]
        various variables needed to deal with too frequent events
    
    """
    def __init__(self, root, mesh, render_frame, dotted_view, ascii_view, config):
        self.root = root
        self.mesh = mesh
        self.render_frame = render_frame
        self.dotted_view = dotted_view
        self.ascii_view = ascii_view
        
        self.config = config
        self.delta = dict(
            zoom=0,
            resolution=0,
            from_move=[0, 0],
            to_move=[0, 0],
            from_rotation=[0, 0],
            to_rotation=[0, 0]
        )
        
        self.renderers = dict(
            dotted=RenderDotted(
                self.dotted_view,
                self.mesh, 
                self.config
            ), 
            ascii=RenderAscii(
                self.ascii_view,
                self.mesh,
                self.render_frame,
                self.config
            )
        )
        self.current_renderer = self.renderers['dotted']
        
    def change_mode(self):        
        if self.config['mode'].get() == 'dotted':
            self.ascii_view.grid_forget()
            self.dotted_view.grid(row=0, column=0, sticky='nswe')
            self.dotted_view.create_rectangle(
                0, 0, self.dotted_view.winfo_width(), self.dotted_view.winfo_height(), fill='black'
            )

        if self.config['mode'].get() == 'ascii':
            self.dotted_view.grid_forget()
            self.ascii_view.grid(row=0, column=0, sticky='nswe')
            self.root.update()
            self.ascii_view.create_rectangle(
                0, 0, self.ascii_view.winfo_width(), self.ascii_view.winfo_height(), fill='black'
            )
   
        self.current_renderer = self.renderers[self.config['mode'].get()]
        self.render()
        
    def rotate(self, val):
        if self.delta['from_rotation'] == [0, 0]:
            self.delta['from_rotation'] = [val.x, val.y]
            self.root.after(50, self._rotate)
        else:
            self.delta['to_rotation'] = [val.x, val.y]
        
    def _rotate(self):
        if self.delta['from_rotation'] != [0, 0]:
            self.config['rotation_offset'][0] += self.delta['to_rotation'][0] - self.delta['from_rotation'][0]
            self.config['rotation_offset'][1] += self.delta['to_rotation'][1] - self.delta['from_rotation'][1]
            self.render()
        self.delta['from_rotation'] = [0, 0]
        
    def move(self, val, scale=1):
        if self.delta['from_move'] == [0, 0]:
            self.delta['from_move']  = [val.x, val.y]
            self.root.after(50, lambda: self._move(scale))
        else:
            self.delta['to_move']  = [val.x, val.y]
        
    def _move(self, scale):
        if self.delta['from_move'] != [0, 0]:
            self.config['move_offset'][0] += int((self.delta['to_move'][0] - self.delta['from_move'][0])*scale)
            self.config['move_offset'][1] += int((self.delta['to_move'][1] - self.delta['from_move'][1])*scale)
            self.render()
        self.delta['from_move'] = [0, 0]
        
    def change_resolution(self, val):
        self.delta['resolution'] = val
        self.root.after(100, self._change_resolution)
        
    def _change_resolution(self):
        if self.delta['resolution'] != 0:
            self.render()
        self.delta['resolution'] = 0
        
    def zoom(self, val, change):
        self.delta['zoom'] += change
        self.root.after(100, self._zoom)
        
    def _zoom(self):
        if self.delta['zoom'] != 0:
            self.config['zoom'] += self.delta['zoom']
            self.render()
        self.delta['zoom'] = 0
        
    def render(self):
        if(self.mesh.is_loaded()):
            self.current_renderer.render()
        else:
            print("No file selected")