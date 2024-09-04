import os
import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 打开文件选择对话框
    file_path = filedialog.askopenfilename(
        title='选择文件',
        filetypes=[('所有文件', '*.*'), ('文本文件', '*.txt'), ('Python文件', '*.py')]
    )

    if file_path:
        print(f"选择的文件路径是: {file_path}")
    else:
        print("没有选择文件")

if __name__ == "__main__":
    select_file()