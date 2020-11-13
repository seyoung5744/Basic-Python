import tkinter as tk
import python_mini_project.staticString as ss
import python_mini_project.movie.UI.MovieListPage as mlp
import python_mini_project.login.UI.LoginPage as lp
import os

seznamTextu = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
buttons = [] # 버튼을 고유 값 저장
pushButton = []
bookingNum = [1, 10] # 예약된 좌석 ( 이때 파일에서 불러옴 )
selectSeat = []

class bookingPage(tk.Frame):
    # global bookingSeat
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # os.chdir("booking")
        print("값 없냐?",ss.screen) # 영화 설명에서 받아오는 영화 제목
        print("지금 어디?", os.getcwd())
        self.seatTable()
        self.master = master
        # tk.Frame.configure(self)  # bg='blue'

        self.isLoginFlag = False
        self.popUpClicked = False

        self.listbox = tk.Listbox(self, font=(20), selectmode="extended")

        self.movieTimeListBox()
        tk.Label(self, text="예매하기", font=('Helvetica', 15, "bold")).place(x=460,y=40)

        self.backButton()
        self.bookingButton()

        print(self.listbox.curselection())
    def bookingButton(self):
        selectbtn = tk.Button(self, text="예매하기")
        selectbtn.bind("<Button-1>", self.bookingEvent)
        selectbtn.place(x=680, y=480)

    def movieTimeListBox(self):
        self.listbox.insert(0,"13:35 188석")
        self.listbox.insert(1, "10:30 236석")
        self.listbox.insert(2, "17:10 237석")
        self.listbox.insert(3, "20:10 237석")
        self.listbox.select_set(0)
        print("현재 선택한 거",self.listbox.curselection())
        self.listbox.place(x=660,y=200)
        self.listbox.bind("<<ListboxSelect>>", self.listSelect)

    def listSelect(self,Event = None):
        print(self.listbox.curselection())
        index = self.listbox.curselection()[0] # 선택된 날짜
        '''
        선택한거 불러오면 됨
        '''
        # if index != ():

    def bookingEvent(self, event):
        if ss.isLogin:
            print("로그인 필요")
            self.createLoginSuccessPopUp()

        else:
            print("로그인 이미 함")
            index = self.listbox.curselection()[0]
            print(index)
            # index = self.listbox.bbox(index)
            bookingDate = self.listbox.get(index,)
            print(self.listbox.get(index,))
            print("예매 " ,ss.screen, bookingDate, selectSeat)

    def seatTable(self):
        l_frame = tk.Frame(self, width = 600, height = 1000, bd = 50, bg = "black")
        l_frame.place(x =100, y = 200)
        print(l_frame)

        num = 1
        for i in range(4):  # Rows
            for j in range(4):  # Columns
                b = tk.Button(l_frame, text=seznamTextu[i][j], width = 5, height = 2)
                print(b) # .!bookingpage2.!frame.!button
                # print(b.getint())
                # num = str(b).split("!")[3][6]
                buttons.append(b)
                b.config(command=lambda t=seznamTextu[i][j], b = b: self.selectSeat(t, b))
                # b.bind("<Button-1>", self.buttonClicked)
                b.grid(row=i, column=j, padx = 5, pady = 5)
                num+=1
        self.bookedSeat()
        # for bt in buttons: # 예약된거 색칠
        #     if bt.cget("text") in bookingNum:
        #         bt.configure(state=tk.DISABLED)
        #         bt.configure(background='red', foreground="white")

    def bookedSeat(self):
        for bt in buttons:  # 예약된거 색칠
            if bt.cget("text") in bookingNum:
                bt.configure(state=tk.DISABLED)
                bt.configure(background='red', foreground="white")

        # os.chdir('../')
        # os.chdir('../')
        # os.chdir('../main')

    def selectSeat(self, text, btn):
        global bookingSeat
        print(btn, text)

        if text in selectSeat: # 선택 전
            btn.configure( background='white', foreground = "black")

            # pushButton.remove(btn)

            selectSeat.pop()
            print(selectSeat)
        else: # 좌석 선택하면
            btn.configure(background='green', foreground="white")

            # pushButton.append(btn)

            bookingSeat = btn.cget("text")
            selectSeat.append(bookingSeat)
            print(selectSeat)

    def createLoginSuccessPopUp(self):
        self.popUpClicked = True

        self.popUpFrame = tk.Tk()
        okLabel = tk.Label(self.popUpFrame, text="로그인이 필요합니다.", font=(25))
        okLabel.pack()
        okButton = tk.Button(self.popUpFrame, text="로그인")
        okButton.bind("<Button-1>", self.goLogin)
        okButton.pack(side="bottom")

        self.popUpFrame.title("로그인")
        self.popUpFrame.geometry("+650+400")
        self.popUpFrame.mainloop()

    def goLogin(self,Event):
        if self.popUpClicked:
            self.popUpFrame.destroy()
        self.master.switch_frame(lp.LoginPage)

    def backButton(self):
        b1 = tk.Button(self, text="뒤로가기")
        b1.bind("<Button-1>", self.backButtonClicked)
        b1.place(x=800, y=30)
        buttons.clear()


    def backButtonClicked(self, event):
        # os.chdir("../")  # movie 파일로 이동
        # print("PageOne : ", os.getcwd())
        # print("눌렀음")
        selectSeat.clear()
        self.master.switch_frame(mlp.StartPage)

