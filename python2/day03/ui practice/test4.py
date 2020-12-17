import tkinter as tk

def f1():
    s = entry.get()#엔트리의 입력값 반환
    label.config(text=s)
    entry.delete(0, tk.END)#엔트리의 모든 값 삭제

root = tk.Tk()
root.title('제목줄')
root.geometry('300x200+300+300')#윈도우 창의 크기(300, 200)와 위치(100,100) 지정
root.resizable(False, False)#가로, 세로 길이 조정 불가
label = tk.Label(root, width=10)
entry = tk.Entry(root, width=10)#입력받스
b1 = tk.Button(root, text='write')
b1.bind('<Button-1>', f1)
label.grid(row=0, column=0)
entry.grid(row=1, column=0)
b1.grid(row=1, column=1)
root.mainloop()