import tkinter as tk
import python_mini_project.main.UI.MainPage as mp
import os
import python_mini_project.staticString as ss
import python_mini_project.login.loginService as loginService
import python_mini_project.login.UI.popUpFrame as puf


class LoginPage(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)

        self.loginService = loginService.LoginService()

        self.isLoginFlag = False
        self.popUpClicked = False
        self.popUpFrame = None

        self.inputID = tk.StringVar()
        self.inputPassword = tk.StringVar()
        # self.inputJoinID = tk.StringVar()
        # self.inputJoinPassword = tk.StringVar()
        # print(self.inputID, self.inputPassword, self.inputJoinID, self.inputJoinPassword)

        self.joinlabel = None
        self.joinID_label = None
        self.joinPassword_label = None
        self.joinIdEntry = None
        self.joinPasswordEntry = None

        self.label = None
        self.login_frame = None
        self.ID_label = None
        self.Password_label = None
        self.IdEntry = None
        self.PasswordEntry = None

        self.login_button = None
        self.member_registration = None

        self.createWidget(master)
        self.positionWidget()
        self.backButton()



    def createWidget(self, master):
        tk.Label(self, text="로그인", font=('Helvetica', 20, "bold")).place(x=440, y=40)
        tk.Button(self, text="종료", command=lambda: master.quit()).place(x=870, y=30)
        self.login_frame = tk.Frame(self, width=300, height=300)
        self.label = tk.Label(self.login_frame, text='회원로그인')
        self.ID_label = tk.Label(self.login_frame, text='ID')
        self.Password_label = tk.Label(self.login_frame, text='Password')
        self.IdEntry = tk.Entry(self.login_frame, textvariable=self.inputID)
        self.PasswordEntry = tk.Entry(self.login_frame, textvariable=self.inputPassword)
        self.login_button = tk.Button(self, text='login')
        self.member_registration =  tk.Button(self, text="회원가입")

    def positionWidget(self):
        self.login_frame.place(x=360, y=250)
        self.label.grid(row=0, column=0)
        self.IdEntry.grid(row=1, column=1)
        self.PasswordEntry.grid(row=2, column=1)
        self.ID_label.grid(row=1, column=0)
        self.Password_label.grid(row=2, column=0)
        self.login_button.place(x=600, y=400)
        self.member_registration.place(x = 640, y = 400)
        self.login_button.bind("<Button-1>", self.loginButton)
        self.member_registration.bind("<Button-1>", self.createMemberJoinPopUp)

    def loginButton(self, event):
        self.isLoginFlag = True
        id = self.inputID.get()
        passWord = self.inputPassword.get()

        memberlist = self.loginService.getMemberList()
        print(os.getcwd())
        if id + ".txt" in memberlist:
            print("이미 가입되어 있다.")
            user = self.loginService.getMember(id)
            print(user)
            readPW= user.split(" ")
            if passWord == readPW[0]:
                print("로그인 성공!!")
                ss.loginID = id
                ss.loginPW = passWord
                ss.isLogin = False
                self.createLoginSuccessPopUp()
            else :
                os.chdir('../')
                os.chdir('../main')
                print("패스워드가 다릅니다.")
        else :
            os.chdir('../')
            os.chdir('../main')
            # self.wantJoinPopUp()
            print("가입해야함")

    def backButton(self):
        b1 = tk.Button(self, text="뒤로가기" )
        b1.bind("<Button-1>",self.backButtonClicked)
        b1.place(x = 800, y = 30)

    def backButtonClicked(self, event):
        if self.isLoginFlag:  # 로그인 버튼을 클릭했엇으면
            os.chdir('../')
            os.chdir('../main')
        os.chdir("../main")  # movie 파일로 이동
        print("PageOne : ", os.getcwd())
        print("눌렀음")
        if self.popUpClicked:
            self.popUpFrame.destroy()
        self.master.switch_frame(mp.MainPage)


    def createLoginSuccessPopUp(self):
        self.popUpClicked = True

        self.popUpFrame = tk.Tk()
        okLabel = tk.Label(self.popUpFrame, text="로그인 성공!!", font = (25))
        okLabel.pack()
        okButton = tk.Button(self.popUpFrame, text="확인")
        okButton.bind("<Button-1>",self.backButtonClicked)
        okButton.pack(side = "bottom")

        self.popUpFrame.title("로그인 팝업")
        self.popUpFrame.geometry("+650+400")
        self.popUpFrame.mainloop()

    def wantJoinPopUp(self):
        self.popUpClicked = True

        self.popUpFrame = tk.Tk()
        okLabel = tk.Label(self.popUpFrame, text="회원가입이 필요합니다.", font = (25))
        okLabel.pack()
        okButton = tk.Button(self.popUpFrame, text="확인")
        # okButton.bind("<Button-1>",self.backButtonClicked)
        okButton.pack(side = "bottom")

        self.popUpFrame.title("회원가입 요구")
        self.popUpFrame.geometry("+650+400")
        self.popUpFrame.mainloop()

    def createMemberJoinPopUp(self,Event):
        self.popUpClicked = True

        pop = puf.PopUpFrame()
        # pop.joinMember()

        # self.joinlabel = tk.Label(self.popUpFrame, text='')
        # self.joinID_label = tk.Label(self.popUpFrame, text='ID')
        # self.joinPassword_label = tk.Label(self.popUpFrame, text='Password')
        # print(self.inputJoinID)
        # self.joinIdEntry = tk.Entry(self.popUpFrame, textvariable=self.inputJoinID)
        # self.joinPasswordEntry = tk.Entry(self.popUpFrame, textvariable=self.inputJoinPassword)
        #
        # self.joinlabel.grid(row=0, column=0)
        # self.joinIdEntry.grid(row=1, column=1)
        # self.joinPasswordEntry.grid(row=2, column=1)
        # self.joinID_label.grid(row=1, column=0)
        # self.joinPassword_label.grid(row=2, column=0)
        #
        # okButton = tk.Button(self.popUpFrame, text="가입")
        # okButton.bind("<Button-1>", self.joinMember)
        # okButton.grid(row = 3, column = 1)
        #
        # self.popUpFrame.title("회원가입")
        # self.popUpFrame.geometry("250x100+650+400")
        # self.popUpFrame.mainloop()

    # def joinMember(self, Event):
    #     print(self.popUpFrame.inputJoinID.get())
    #     joinId = self.popUpFrame.inputJoinID.get()
    #     joinPassWord = self.popUpFrame.inputJoinPassword.get()
    #     print(joinId, joinPassWord)
    #     print("파일에 가입자 입력")



