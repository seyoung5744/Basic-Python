import tkinter as tk

class ClientUI:
    def __init__(self, root):
        self.root = root
        self.uiInit()

    def uiInit(self):
        self.root.title("클라이언트")
        frame1 = tk.Frame(self.root, relief="solid", bd=2)
        frame1.pack(side="top",  fill="both")

        frame2 = tk.Frame(self.root, relief="solid", bd=2, height=200)
        frame2.pack(side="bottom", fill="both")

        chatLabel = tk.Label()
        button1 = tk.Button(frame1, text="프레임1")
        button1.pack(side="right")

        button2 = tk.Button(frame2, text="프레임2")
        button2.pack(side="left")

def main():
    root = tk.Tk()
    root.geometry("300x400+100+100") # 너비x높이+x좌표+y좌표
    root.resizable(False, False) # 윈도우이름.resizeable(상하, 좌우)을 이용하여 윈도우 창의 창 크기 조절 가능 여부를 설정할 수 있습니다. True로 설정할 경우 윈도우 창의 크기를 조절할 수 있습니다.
    ClientUI(root)
    root.mainloop()

main()
