import tkinter as tk
import miniproject.FactoryUI as fUI
import miniproject.UIControl as uiControl

class MainUI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        factoryButton = tk.Button(self, text="공장", width=10, command=lambda: master.switch_frame(fUI.FactoryUI))
        factoryButton.pack()
        storeButton = tk.Button(self, text="가게", width=10)
        storeButton.pack()


