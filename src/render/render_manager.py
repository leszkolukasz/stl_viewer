from render.render_ascii import RenderAscii
from render.render_dotted import RenderDotted
import tkinter as tk

class RenderManager():
    def __init__(self, root, mesh, dotted_view, ascii_view, config):
        self.root = root
        self.mesh = mesh
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
                self.config
            )
        )
        self.current_renderer = self.renderers['dotted']
        
    def change_mode(self):        
        if self.mode.get() == 'dotted':
            self.ascii_view.grid_forget()
            self.dotted_view.grid(row=0, column=0, sticky='nswe')
            self.dotted_view.create_rectangle(
                0, 0, self.dotted_view.winfo_width(), self.dotted_view.winfo_height(), fill='black'
            )

        if self.mode.get() == 'ascii':
            self.dotted_view.grid_forget()
            self.ascii_view.grid(row=0, column=0, sticky='nswe')
            self.ascii_view.create_rectangle(
                0, 0, self.ascii_view.winfo_width(), self.ascii_view.winfo_height(), fill='white'
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
        
    def move(self, val):
        if self.delta['from_move'] == [0, 0]:
            self.delta['from_move']  = [val.x, val.y]
            self.root.after(50, self._move)
        else:
            self.delta['to_move']  = [val.x, val.y]
        
    def _move(self):
        if self.delta['from_move'] != [0, 0]:
            self.config['move_offset'][0] += self.delta['to_move'][0] - self.delta['from_move'][0]
            self.config['move_offset'][1] += self.delta['to_move'][1] - self.delta['from_move'][1]
            self.render()
        self.delta['from_move'] = [0, 0]
        
    def change_resolution(self, val):
        self.delta['resolution'] = val
        self.root.after(50, self._change_resolution)
        
    def _change_resolution(self):
        if self.delta['resolution'] != 0:
            self.render()
        self.delta['resolution'] = 0
        
    def zoom(self, val, change):
        self.delta['zoom'] += change
        self.root.after(50, self._zoom)
        
    def _zoom(self):
        if self.delta['zoom'] != 0:
            self.config['zoom'] += self.delta['zoom']
            self.render()
        self.delta['zoom'] = 0
        
    def render(self):
        self.current_renderer.render()