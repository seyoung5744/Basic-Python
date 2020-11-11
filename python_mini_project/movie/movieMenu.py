import tkinter as tk
from PIL import Image, ImageTk
import python_mini_project.movie.movieService as ms

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill = "both", expand = True)


    def finish(self):
        self.quit()



class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="상영 중인 영화", width = 10, font=('Helvetica', 18, "bold")).\
            grid(row=0, column=1, pady = 30)

        load = Image.open('movie_info/image/im.png')
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render) # width = 250, height = 350
        img.image = render
        img.size()
        img.grid(row = 1, column = 0, padx = 30, pady = 20)

        load2 = Image.open('movie_info/image/im2.png')
        render2 = ImageTk.PhotoImage(load2)
        img2 = tk.Label(self, image=render2)
        img2.image = render2
        img2.size()
        img2.grid(row=1, column=1, padx = 30, pady = 20)

        load3 = Image.open('movie_info/image/im3.png')
        render3 = ImageTk.PhotoImage(load3)
        img3 = tk.Label(self, image=render3)
        img3.image = render3
        img3.size()
        img3.grid(row=1, column=2, padx = 30, pady = 20)


        tk.Button(self, text="삼진그룹 영어토익반",
                  command=lambda: master.switch_frame(PageOne)).grid(row=2, column=0)

        tk.Button(self, text="도굴",
                  command=lambda: master.switch_frame(PageTwo)).grid(row=2, column=1)
        tk.Button(self, text="노트북",
                  command=lambda: master.switch_frame(PageThree)).grid(row=2, column=2)


class PageOne(tk.Frame):
    def __init__(self, master):
        self.service = ms.MovieService()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self) #  bg='blue'
        tk.Label(self, text = self.service.getMovieInfo("삼진그룹 영어토익반"), font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="뒤로가기",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="종료", command = lambda : master.quit()).pack()



class PageTwo(tk.Frame):
    def __init__(self, master):
        self.service = ms.MovieService()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text = self.service.getMovieInfo("도굴"), font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="뒤로가기",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="종료", command=lambda: master.quit()).pack()

class PageThree(tk.Frame):
    def __init__(self, master):
        self.service = ms.MovieService()
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text = self.service.getMovieInfo("노트북"), font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="뒤로가기",
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="종료", command=lambda: master.quit()).pack()


class MovieMenu:
    def run(self):
        app = SampleApp()
        app.geometry("1000x600+100+100") # 창의 너비, 창의 높이, 창의 가로 방향 위치, 창의 세로 방향 위치
        app.mainloop()