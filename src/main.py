import tkinter as tk

root = tk.Tk()
root.title("STL Viewer")

root.geometry("600x600")

root.columnconfigure(0, weight=1)
for i in range(21):
    root.rowconfigure(i, weight=1)

render_frame = tk.Frame(root, bg='red')
render_frame.grid(row=0, column=0, rowspan=20, sticky='nswe')

nav_frame = tk.Frame(root,  bg='green', padx=10)
nav_frame.grid(row=20, column=0, sticky='nswe')

tk.Button(nav_frame, text="Open", pady=10).grid(row=0, column=0, sticky='nswe')
tk.Label(nav_frame, text="View mode: ").grid(row=0, column=1, sticky='nswe')
tk.Radiobutton(nav_frame, text='Dotted').grid(row=0, column=2, sticky='nswe')
tk.Radiobutton(nav_frame, text='ASCII').grid(row=0, column=3, sticky='nswe')
tk.Label(nav_frame, text="Resolution: ").grid(row=0, column=4, sticky='nswe')
tk.Scale(nav_frame, orient=tk.HORIZONTAL, length=200, from_=1.0, to=100.0).grid(row=0, column=5, sticky='nswe')

nav_frame.rowconfigure(0, weight=1)
nav_frame.columnconfigure(0, weight=1)
nav_frame.columnconfigure(1, weight=1)
nav_frame.columnconfigure(2, weight=1)
nav_frame.columnconfigure(3, weight=1)
nav_frame.columnconfigure(4, weight=1)
nav_frame.columnconfigure(5, weight=1)


root.mainloop()