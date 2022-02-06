from render.render_ascii import RenderAscii
from render.render_dotted import RenderDotted
import tkinter as tk

class RenderManager():
    def __init__(self, root, mesh, dotted_view, ascii_view, mode, resolution, zoom):
        self.root = root
        self.mesh = mesh
        self.dotted_view = dotted_view
        self.ascii_view = ascii_view
        self.mode = mode
        self.resolution = resolution
        self.zoom = zoom
        self.move_x = tk.IntVar(value=0)
        self.move_y = tk.IntVar(value=0)
        self.rot_x = tk.IntVar(value=0)
        self.rot_y = tk.IntVar(value=0)
        self.renderers = dict(dotted=RenderDotted(self.dotted_view, self.mesh, self.resolution, self.zoom, self.move_x, self.move_y, self.rot_x, self.rot_y), ascii=RenderAscii(self.ascii_view, self.mesh, self.resolution, self.zoom, self.move_x, self.move_y, self.rot_x, self.rot_y))
        self.current_renderer = self.renderers['dotted']
        self.cnt = 0
        self.cnt_res = 0
        self.from_drag = [0, 0]
        self.to_drag = [0, 0]
        self.from_rot = [0, 0]
        self.to_rot = [0, 0]
        
    def change_mode(self):
        print(self.mode.get())
        
        if self.mode.get() == 'dotted':
            self.ascii_view.grid_forget()
            self.dotted_view.grid(row=0, column=0, sticky='nswe')
            self.dotted_view.create_rectangle(0, 0, self.dotted_view.winfo_width(), self.dotted_view.winfo_height(), fill='black')

            
        if self.mode.get() == 'ascii':
            self.dotted_view.grid_forget()
            self.ascii_view.grid(row=0, column=0, sticky='nswe')
            self.ascii_view.create_rectangle(0, 0, self.ascii_view.winfo_width(), self.ascii_view.winfo_height(), fill='white')

            
        self.current_renderer = self.renderers[self.mode.get()]
        self.render()
        
    def rotation_drag(self, val):
        if self.from_rot == [0, 0]:
            self.from_rot = [val.x, val.y]
            self.root.after(300, self.rotation_drag2)
        else:
            self.to_rot = [val.x, val.y]
        
    def rotation_drag2(self):
        if self.from_rot != [0, 0]:
            self.rot_x.set(self.rot_x.get() + self.to_rot[0] - self.from_rot[0])
            self.rot_y.set(self.rot_y.get() + self.to_rot[1] - self.from_rot[1])
            self.render()
        self.from_rot = [0, 0]
        
    def drag_mouse(self, val):
        if self.from_drag == [0, 0]:
            self.from_drag = [val.x, val.y]
            self.root.after(300, self.drag_mouse2)
        else:
            self.to_drag = [val.x, val.y]
        
    def drag_mouse2(self):
        if self.from_drag != [0, 0]:
            self.move_x.set(self.move_x.get() + self.to_drag[0] - self.from_drag[0])
            self.move_y.set(self.move_y.get() + self.to_drag[1] - self.from_drag[1])
            self.render()
        self.from_drag = [0, 0]
        
    def change_resolution(self, val):
        self.cnt_res = val
        self.root.after(300, self.change_resolution2)
        
    def change_resolution2(self):
        if self.cnt_res != 0:
            self.render()
        self.cnt_res = 0
        
    def zoom_in(self, val):
        self.cnt += 1
        self.root.after(100, self.zoom_in2)

        
    def zoom_in2(self):
        if self.cnt != 0:
            self.zoom.set(self.zoom.get()+self.cnt)
            self.render()
        self.cnt = 0
        
    def zoom_out(self, val):
        self.cnt -= 1
        self.root.after(100, self.zoom_out2)

    def zoom_out2(self):
        if self.cnt != 0:
            self.zoom.set(self.zoom.get()+self.cnt)
            self.render()
        self.cnt = 0
        
    def render(self):
        print('Rendering...')
        self.current_renderer.render()