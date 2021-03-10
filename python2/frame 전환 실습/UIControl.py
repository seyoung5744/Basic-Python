import tkinter as tk
import miniproject.MainUI as mainUI

class UIControl(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(mainUI.MainUI)

    def switch_frame(self, frame_class):
        print("test")
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
