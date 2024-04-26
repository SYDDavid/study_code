import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # 隐藏主窗口

file_path = filedialog.askopenfilename()