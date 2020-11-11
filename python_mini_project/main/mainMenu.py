import tkinter as tk
import python_mini_project.movie.movieMenu as mm
from PIL import Image, ImageTk
import python_mini_project.movie.movieService as ms
import python_mini_project.movie.UI.StartPage as sp

# import python_mini_project.Switch_Frame as sa
#
# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self._frame = None
#         self.switch_frame(MainPage)
#
#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.pack(fill = "both", expand = True)
#
#
#     def finish(self):
#         self.quit()


#
# class MainPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         load = Image.open('cgv_logo.png')
#         render = ImageTk.PhotoImage(load)
#         img = tk.Label(self, image=render) # width = 250, height = 350
#         img.image = render
#         img.size()
#         img.grid(row = 1, column = 0, padx = 30, pady = 20)
#
#
#         tk.Button(self, text="상영 중인 영화",
#                   command=lambda: master.switch_frame(sp.StartPage)).grid(row=2, column=0)
#         tk.Button(self, text="종료", command=lambda: master.quit()).grid(row=2, column=1)


#
# class PageOne(tk.Frame):
#     def __init__(self, master):
#         self.service = ms.MovieService()
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self) #  bg='blue'
#         tk.Label(self, text = self.service.getMovieInfo("삼진그룹 영어토익반"), font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="뒤로가기",
#                   command=lambda: master.switch_frame(MainPage)).pack()
#         tk.Button(self, text="종료", command = lambda : master.quit()).pack()
#
#
#
# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         self.service = ms.MovieService()
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self)
#         tk.Label(self, text = self.service.getMovieInfo("도굴"), font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="뒤로가기",
#                   command=lambda: master.switch_frame(MainPage)).pack()
#         tk.Button(self, text="종료", command=lambda: master.quit()).pack()
#
# class PageThree(tk.Frame):
#     def __init__(self, master):
#         self.service = ms.MovieService()
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self)
#         tk.Label(self, text = self.service.getMovieInfo("노트북"), font=('Helvetica', 10, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="뒤로가기",
#                   command=lambda: master.switch_frame(MainPage)).pack()
#         tk.Button(self, text="종료", command=lambda: master.quit()).pack()
#
# class MainMenu:
#     app = sa.SwitchFrame()
#     def run(self):
#         print("fdasfafadwe")
#         app = sa.SwitchFrame()
#         app.geometry("1000x600+100+100") # 창의 너비, 창의 높이, 창의 가로 방향 위치, 창의 세로 방향 위치
#         app.mainloop()