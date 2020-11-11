import tkinter as tk
import python_mini_project.main.UI.MainPage as mp


class SwitchFrame(tk.Tk): # 상속
    def __init__(self):
        print("우와왕")
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(mp.MainPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill = "both", expand = True)


    def finish(self):
        self.quit()
