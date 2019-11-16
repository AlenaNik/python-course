import os
import sys
import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
import PyPDF2

root = tk.Tk()
apps = []

def addApp():

    filename = filedialog.askopenfile(initialdir="/", title="Select File",
                                      filetypes=(("executables", "*.studio"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="white")
        label.pack()

def readApps():
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call(app)

canvas = tk.Canvas(root, height=400, width=400, bg="#0c1013")
canvas.pack()
frame = tk.Frame(root, bg="#181f2d")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File",
                     padx=10,
                     pady=5,
                     fg="black",
                     bg="#0c1013", command=addApp)
openFile.pack()
readApps = tk.Button(root, text="Run",
                     padx=10,
                     pady=5,
                     fg="#ff7d6d",
                     bg="#0c1013",
                     command=readApps
                     )
readApps.pack()

root.mainloop()