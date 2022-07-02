"""Implements Main application class"""

import tkinter as tk
import tkinter.filedialog

from render.render_manager import RenderManager
from mesh import Mesh

class App:
    """
    Main application class. Manages all Tkinter widgets
    
    Variables
    ----------
    root:
        main application Tkinter class
    mesh: Mesh
        object that contains vectors from stl file and applies transformations to it
    config: Dict[str]
        various configuration parameters
    render_manager: RenderManager
        object that manages rendering
    render_frame:
        frame where rendering occurs
    nav_frame:
        frame with navigation buttons
    dotted_view:
        canvas where dotted view is displayed
    ascii_view:
        canvas where ASCII view is displayed
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("STL Viewer")
        self.root.geometry("600x600")
        
        self.mesh = Mesh()
        self.config = dict(
            mode=tk.StringVar(value="dotted"),
            resolution=tk.IntVar(value=10),
            zoom=100,
            fov=250,
            distance=300,
            move_offset=[0, 0],
            rotation_offset=[0,0],
            window_width = 600,
            window_height = 600
        )
        
        self._build_ui_frames()
        self.render_manager = RenderManager(
            self.root,
            self.mesh,
            self.render_frame,
            self.dotted_view,
            self.ascii_view,
            self.config
        )
        self._build_ui_widgets()
        
        self.root.bind('<Configure> ', lambda e: self.resize(e))
        
    def run(self):
        self.root.mainloop()
        
    def _build_ui_frames(self):
        self.root.columnconfigure(0, weight=1)
        for i in range(21):
            self.root.rowconfigure(i, weight=1)

        self.render_frame = tk.Frame(self.root, bg='black', padx=10, pady=10)
        self.render_frame.grid(row=0, column=0, rowspan=20, sticky='nswe')
        
        self.render_frame.rowconfigure(0, weight=1)
        self.render_frame.columnconfigure(0, weight=1)
        
        self.dotted_view = tk.Canvas(self.render_frame, background='black')
        self.dotted_view.grid(row=0, column=0, sticky='nswe')
        self.ascii_view = tk.Canvas(self.render_frame, background='black')
        
        self.nav_frame = tk.Frame(self.root,  bg='black', padx=10)
        self.nav_frame.grid(row=20, column=0, sticky='nswe')
        
        self.nav_frame.rowconfigure(0, weight=1)
        self.nav_frame.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(1, weight=1)
        self.nav_frame.columnconfigure(2, weight=1)
        self.nav_frame.columnconfigure(3, weight=1)
        self.nav_frame.columnconfigure(4, weight=1)
        self.nav_frame.columnconfigure(5, weight=1)

    def _build_ui_widgets(self):
        tk.Button(
            self.nav_frame, text="Open", command=self.open_file, pady=10
        ).grid(row=0, column=0, sticky='nswe')
        tk.Label(
            self.nav_frame, text="View mode: "
        ).grid(row=0, column=1, sticky='nswe')
        tk.Radiobutton(
            self.nav_frame,
            text='Dotted',
            value='dotted',
            variable=self.config['mode'],
            command=self.render_manager.change_mode
        ).grid(row=0, column=2, sticky='nswe')
        tk.Radiobutton(
            self.nav_frame,
            text='ASCII',
            value='ascii',
            variable=self.config['mode'],
            command=self.render_manager.change_mode
        ).grid(row=0, column=3, sticky='nswe')
        tk.Label(
            self.nav_frame, text="Resolution: "
        ).grid(row=0, column=4, sticky='nswe')
        tk.Scale(
            self.nav_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=1.0,
            to=30.0,
            variable=self.config['resolution'],
            command=self.render_manager.change_resolution
        ).grid(row=0, column=5, sticky='nswe')
        
        self.dotted_view.bind('<Button-4> ', lambda val: self.render_manager.zoom(val, -1))
        self.dotted_view.bind('<Button-5> ', lambda val: self.render_manager.zoom(val, 1))
        self.dotted_view.bind('<B1-Motion> ', self.render_manager.move)
        self.dotted_view.bind('<Shift-B1-Motion> ', self.render_manager.rotate)
        
        self.ascii_view.bind('<Button-4> ', lambda val: self.render_manager.zoom(val, -1))
        self.ascii_view.bind('<Button-5> ', lambda val: self.render_manager.zoom(val, 1))
        self.ascii_view.bind('<B1-Motion> ', lambda val: self.render_manager.move(val, 0.1))
        self.ascii_view.bind('<Shift-B1-Motion> ', self.render_manager.rotate)
        
    def open_file(self):
        path = tk.filedialog.askopenfilename()
        #path = './sphere.stl'
        if len(path):
            self.mesh.load_file(path)
            self.render_manager.render()
            
    def resize(self, event):
        if event.widget == self.root:
            if (self.config['window_width'] != event.width) and (self.config['window_height'] != event.height):
                self.config['window_width'], self.config['window_height'] = event.width, event.height
                self.render_manager.render()

if __name__ == '__main__':
    app = App()
    app.run()
