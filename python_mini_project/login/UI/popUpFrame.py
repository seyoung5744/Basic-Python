import tkinter as tk
import os

class PopUpFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inputJoinID = tk.StringVar()
        self.inputJoinPassword = tk.StringVar()

        self.joinlabel = tk.Label(self, text='')
        self.joinID_label = tk.Label(self, text='ID')
        self.joinPassword_label = tk.Label(self, text='Password')
        print(self.inputJoinID)
        self.joinIdEntry = tk.Entry(self, textvariable=self.inputJoinID)
        self.joinPasswordEntry = tk.Entry(self, textvariable=self.inputJoinPassword)

        self.joinlabel.grid(row=0, column=0)
        self.joinIdEntry.grid(row=1, column=1)
        self.joinPasswordEntry.grid(row=2, column=1)
        self.joinID_label.grid(row=1, column=0)
        self.joinPassword_label.grid(row=2, column=0)

        self.okButton = tk.Button(self, text="가입")
        self.okButton.bind("<Button-1>", self.joinMember)
        self.okButton.grid(row=3, column=1)

        self.title("회원가입")
        self.geometry("250x100+650+400")
        self.mainloop()

    def joinMember(self, Event):
        print("오러ㅏㅣㅁ", self.joinIdEntry.get())
        joinId = self.joinIdEntry.get()
        joinPassWord = self.joinPasswordEntry.get()
        print(joinId, joinPassWord)

        print(os.getcwd())
        os.chdir('../data/login') # 회원정보에 접근하기 위해 파일이동
        print(os.getcwd())
        f = open(joinId + ".txt", "w", encoding='utf-8')
        f.writelines(joinPassWord)
        f.close()
        os.chdir('../') # 가입하고 다시 파일 원 위치로
        os.chdir('../main')
        self.destroy()
        print("파일에 가입자 입력")
