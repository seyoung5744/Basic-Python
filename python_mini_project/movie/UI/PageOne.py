import tkinter as tk
import python_mini_project.movie.movieService as ms
import python_mini_project.movie.UI.StartPage as sp

class PageOne(tk.Frame):
    def __init__(self, master):
        self.service = ms.MovieService()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self) #  bg='blue'
        tk.Label(self, text = self.service.getMovieInfo("삼진그룹 영어토익반"), font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="뒤로가기",
                  command=lambda: master.switch_frame(sp.StartPage)).pack()
        tk.Button(self, text="종료", command = lambda : master.quit()).pack()