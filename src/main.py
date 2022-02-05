import tkinter as tk
import tkinter.filedialog
from render.render_manager import RenderManager

class App:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("STL Viewer")
        self.root.geometry("600x600")
        
        self.mesh = None
        self.mode = tk.StringVar(value="dotted")
        self.resolution = tk.IntVar(value=10)
        
        self.render_manager = RenderManager(self.root, None, None, self.mode, self.resolution)
        self._build_ui()
        self.render_manager.ascii_view = self.ascii_view
        self.render_manager.dotted_view = self.dotted_view
        
    def run(self):
        self.root.mainloop()
        
    def _build_ui(self):
        self.root.columnconfigure(0, weight=1)
        for i in range(21):
            self.root.rowconfigure(i, weight=1)

        self.render_frame = tk.Frame(self.root, bg='red')
        self.render_frame.grid(row=0, column=0, rowspan=20, sticky='nswe')
        
        self.dotted_view = tk.Canvas()
        self.ascii_view = tk.Canvas()

        self.nav_frame = tk.Frame(self.root,  bg='green', padx=10)
        self.nav_frame.grid(row=20, column=0, sticky='nswe')
        
        self.nav_frame.rowconfigure(0, weight=1)
        self.nav_frame.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(1, weight=1)
        self.nav_frame.columnconfigure(2, weight=1)
        self.nav_frame.columnconfigure(3, weight=1)
        self.nav_frame.columnconfigure(4, weight=1)
        self.nav_frame.columnconfigure(5, weight=1)

        tk.Button(self.nav_frame, text="Open", command=self.open_file, pady=10).grid(row=0, column=0, sticky='nswe')
        tk.Label(self.nav_frame, text="View mode: ").grid(row=0, column=1, sticky='nswe')
        tk.Radiobutton(self.nav_frame, text='Dotted', value='dotted', variable=self.mode, command=self.render_manager.change_mode).grid(row=0, column=2, sticky='nswe')
        tk.Radiobutton(self.nav_frame, text='ASCII', value='ascii', variable=self.mode, command=self.render_manager.change_mode).grid(row=0, column=3, sticky='nswe')
        tk.Label(self.nav_frame, text="Resolution: ").grid(row=0, column=4, sticky='nswe')
        tk.Scale(self.nav_frame, orient=tk.HORIZONTAL, length=200, from_=1.0, to=100.0, variable=self.resolution, command=self.render_manager.change_resolution).grid(row=0, column=5, sticky='nswe')
        
    def open_file(self):
        path = tk.filedialog.askopenfilename()
        print(path)

if __name__ == '__main__':
    app = App()
    app.run()