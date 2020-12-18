import tkinter as tk

class Map(tk.Frame):
    def __init__(self, root=None, peo=None):
        super().__init__(root)
        self.root = root  # 기본 윈도우를 멤버변수로 저장
        self.root.geometry(peo)
        self.root.resizable(False, False)
        self.root.configure(bg = "white")
        self.pack()  # 현재 이객체(프레임)을 윈도우에 부착
        self.setMap()

    def setMap(self):
        BigFrame = tk.Frame(self, width = 600, height = 600, bg = "black")
        BigFrame.pack()
        for i in range(0, 8):
            for j in range(0, 9):
                # frame = tk.Frame(BigFrame, width = 67, height = 67,bd = 1,borderwidth = 0, highlightthickness=0) # bd : 테두리 두께
                # frame.grid(row=i, column=j)
                canvas = tk.Canvas(BigFrame, width=65, height=65, bd=1, borderwidth = 0,highlightthickness=0) # highlightthickness : 여백
                canvas.grid(row=i, column=j)
                canvas.create_line(0,0,0,66, fill="blue", width =3) # 왼 #BFFEFF
                canvas.create_line(64, 0, 64, 66, fill="blue", width=3) # right
                canvas.create_line(0, 0, 66, 0, fill="blue", width=3) # top
                canvas.create_line(0, 64, 64, 64, fill="blue", width=3) # botton
                t = canvas.create_oval(10,10,30,30,fill="red")
                if i % 3 == 0:
                    canvas.delete(t)
        # t = self.canvas.create_oval(10, 10, 50, 40, fill="blue")
        # self.canvas.delete(t)

