import tkinter as tk
from tkinter import messagebox

class AppWindow(tk.Frame):#프레임 하나 만듬.
    def __init__(self, root=None, geo=None, file=None):
        super().__init__(root)#부모 생성자에 기본 윈도우 전달
        self.root = root #기본 윈도우를 멤버변수로 저장
        self.root.geometry(geo)#윈도우의 크기 및 위치 설정
        self.root.resizable(True, True)#윈도우의 가로, 세로 크기 재조정 가능으로 설정
        self.pack()#현재 이객체(프레임)을 윈도우에 부착

        self.file = file
        self.flist = None #파일 목록 담을 리스트
        self.raVal = tk.IntVar()#라디오버튼 선택한 것의 value
        self.subfr = None#라디오버튼이 부착될 판으로 사용할 프레임
        self.create_widgets()


    def create_widgets(self):#원하는 구성요소 부착
        self.title = tk.Label(self, text='파일읽기<파일목록>')
        self.title.pack()
        self.subfr = tk.Frame(self)  # 하위 프레임 생성
        self.subfr.pack()
        self.mkFList()
        self.readBtn = tk.Button(self, text='read', command=self.readFile)
        self.readBtn.pack()
        self.content = tk.Label(self, text='')
        self.content.pack()
        self.title = tk.Label(self, text='파일쓰기')
        self.title.pack()
        self.aa = tk.Label(self, text='생성할 파일명')
        self.aa.pack()
        self.ent1 = tk.Entry(self, width=50)
        self.ent1.pack()
        self.bb = tk.Label(self, text='파일 내용을 입력하시오')
        self.bb.pack()
        self.ent2 = tk.Entry(self, width=50)
        self.ent2.pack()
        self.writeBtn = tk.Button(self, text='write', command=self.writeFile)
        self.writeBtn.pack()

    def mkFList(self):
        ff = self.subfr.grid_slaves()#위젯의 부모에서 grid로 배치된 위젯만 검색
        for i in ff:
            i.destroy()#destroy(): 위젯 삭제

        j=0
        self.flist = self.file.listDir()
        for idx, i in enumerate(self.flist):
            r = tk.Radiobutton(self.subfr, text=i, variable=self.raVal, value=idx)
            if idx!=1 and idx%3==1:
                j+=1
            r.grid(row=j, column=(idx-1)%3)

    def readFile(self):
        msg = self.file.read(self.flist[self.raVal.get()])
        self.content.config(text=msg)

    def writeFile(self):
        fname = self.ent1.get()#파일명 읽음
        if fname=='' or fname==None:
            tk.messagebox.showinfo(title='오류', message='파일명 누락')
            return

        content = self.ent2.get()
        self.file.write(fname, content)
        self.ent1.delete(0, tk.END)
        self.ent2.delete(0, tk.END)
        self.mkFList()

