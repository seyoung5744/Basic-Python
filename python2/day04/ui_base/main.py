import day04.ui_base.fileRW as f
import day04.ui_base.main_ui as ui
import tkinter as tk

def main():
    root = tk.Tk()
    file = f.FileRW('../ui_base')
    app = ui.AppWindow(root, '650x500+100+100', file)
    app.mainloop()

main()