import tkinter as tk
import tkinter.filedialog

from render.render_manager import RenderManager
from mesh import Mesh

class App:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("STL Viewer")
        self.root.geometry("600x600")
        self.window_width = 600
        self.window_height = 600
        
        self.mesh = Mesh()
        self.mode = tk.StringVar(value="dotted")
        self.resolution = tk.IntVar(value=10)
        
        self.zoom = tk.IntVar(value=10000)
        
        self._build_ui_frames()
        self.render_manager = RenderManager(self.root, self.mesh, self.dotted_view, self.dotted_view, self.mode, self.resolution, self.zoom)
        self._build_ui_widgets()
        
        self.root.bind('<Configure> ', lambda e: self.resize(e))
        
    def run(self):
        self.root.mainloop()
        
    def _build_ui_frames(self):
        self.root.columnconfigure(0, weight=1)
        for i in range(21):
            self.root.rowconfigure(i, weight=1)

        self.render_frame = tk.Frame(self.root, bg='red', padx=10, pady=10)
        self.render_frame.grid(row=0, column=0, rowspan=20, sticky='nswe')
        
        self.render_frame.rowconfigure(0, weight=1)
        self.render_frame.columnconfigure(0, weight=1)
        
        self.dotted_view = tk.Canvas(self.render_frame, background='black')
        self.dotted_view.grid(row=0, column=0, sticky='nswe')
        self.ascii_view = tk.Canvas(self.render_frame, background='white')

        self.nav_frame = tk.Frame(self.root,  bg='green', padx=10)
        self.nav_frame.grid(row=20, column=0, sticky='nswe')
        
        self.nav_frame.rowconfigure(0, weight=1)
        self.nav_frame.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(1, weight=1)
        self.nav_frame.columnconfigure(2, weight=1)
        self.nav_frame.columnconfigure(3, weight=1)
        self.nav_frame.columnconfigure(4, weight=1)
        self.nav_frame.columnconfigure(5, weight=1)

    def _build_ui_widgets(self):
        tk.Button(self.nav_frame, text="Open", command=self.open_file, pady=10).grid(row=0, column=0, sticky='nswe')
        tk.Label(self.nav_frame, text="View mode: ").grid(row=0, column=1, sticky='nswe')
        tk.Radiobutton(self.nav_frame, text='Dotted', value='dotted', variable=self.mode, command=self.render_manager.change_mode).grid(row=0, column=2, sticky='nswe')
        tk.Radiobutton(self.nav_frame, text='ASCII', value='ascii', variable=self.mode, command=self.render_manager.change_mode).grid(row=0, column=3, sticky='nswe')
        tk.Label(self.nav_frame, text="Resolution: ").grid(row=0, column=4, sticky='nswe')
        tk.Scale(self.nav_frame, orient=tk.HORIZONTAL, length=200, from_=1.0, to=50.0, variable=self.resolution, command=self.render_manager.change_resolution).grid(row=0, column=5, sticky='nswe')
        
        self.dotted_view.bind('<Button-4> ', self.render_manager.zoom_out)
        self.dotted_view.bind('<Button-5> ', self.render_manager.zoom_in)
        self.dotted_view.bind('<B1-Motion> ', self.render_manager.drag_mouse)
        self.dotted_view.bind('<Shift-B1-Motion> ', self.render_manager.rotation_drag)
        
    def open_file(self):
        #path = tk.filedialog.askopenfilename()
        path = './sphere.stl'
        print(self.dotted_view.winfo_width())
        if len(path):
            self.mesh.load_file(path)
            self.render_manager.render()
            
    def resize(self, event):
        if event.widget == self.root:
            if (self.window_width != event.width) and (self.window_height != event.height):
                self.window_width, self.window_height = event.width, event.height
                self.render_manager.render()

if __name__ == '__main__':
    app = App()
    app.run()