import tkinter as tk
import python_mini_project.movie.movieMenu as mm
from PIL import Image, ImageTk
import python_mini_project.movie.movieService as ms
import python_mini_project.movie.UI.StartPage as movie
import python_mini_project.Switch_Frame as sf
# from python_mini_project.main.main import app



class MainPage(tk.Frame):
    def __init__(self, master):
        # sd = sf.SwitchFrame()
        tk.Frame.__init__(self, master)
        load = Image.open('cgv_logo.png')
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render) # width = 250, height = 350
        img.image = render
        img.size()
        img.grid(row = 1, column = 0, padx = 30, pady = 20)

        tk.Button(self, text="상영 중인 영화",
                  command=lambda: master.switch_frame(movie.StartPage)).grid(row=2, column=0)
        tk.Button(self, text="종료", command=lambda: master.quit()).grid(row=2, column=1)