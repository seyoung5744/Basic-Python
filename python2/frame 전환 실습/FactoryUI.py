import tkinter as tk
import miniproject.MainUI as mainUI
class FactoryUI(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='blue')


        backButton = tk.Button(self, text="뒤로가기", width=10, command=lambda: master.switch_frame(mainUI.MainUI))
        backButton.pack()






