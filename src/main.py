import tkinter as tk
from render.render_manager import RenderManager

class App:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("STL Viewer")
        self.root.geometry("600x600")
        self._build_ui()
        
        self.render_manager = RenderManager()
        
    def run(self):
        self.root.mainloop()
        
    def _build_ui(self):
        self.root.columnconfigure(0, weight=1)
        for i in range(21):
            self.root.rowconfigure(i, weight=1)

        self.render_frame = tk.Frame(self.root, bg='red')
        self.render_frame.grid(row=0, column=0, rowspan=20, sticky='nswe')

        self.nav_frame = tk.Frame(self.root,  bg='green', padx=10)
        self.nav_frame.grid(row=20, column=0, sticky='nswe')
        
        self.nav_frame.rowconfigure(0, weight=1)
        self.nav_frame.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(1, weight=1)
        self.nav_frame.columnconfigure(2, weight=1)
        self.nav_frame.columnconfigure(3, weight=1)
        self.nav_frame.columnconfigure(4, weight=1)
        self.nav_frame.columnconfigure(5, weight=1)

        tk.Button(self.nav_frame, text="Open", pady=10).grid(row=0, column=0, sticky='nswe')
        tk.Label(self.nav_frame, text="View mode: ").grid(row=0, column=1, sticky='nswe')
        tk.Radiobutton(self.nav_frame, text='Dotted').grid(row=0, column=2, sticky='nswe')
        tk.Radiobutton(self.nav_frame, text='ASCII').grid(row=0, column=3, sticky='nswe')
        tk.Label(self.nav_frame, text="Resolution: ").grid(row=0, column=4, sticky='nswe')
        tk.Scale(self.nav_frame, orient=tk.HORIZONTAL, length=200, from_=1.0, to=100.0).grid(row=0, column=5, sticky='nswe')


if __name__ == '__main__':
    app = App()
    app.run()