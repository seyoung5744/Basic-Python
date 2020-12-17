import tkinter as tk

root = tk.Tk()
root.title('제목줄')
root.geometry('300x200+100+100')#윈도우 창의 크기(300, 200)와 위치(100,100) 지정
root.resizable(False, False)#가로, 세로 길이 조정 불가
b1 = tk.Button(root, width=10, text='1')
b1.grid(row=0, column=0)
b2 = tk.Button(root, width=10, text='2')
b2.grid(row=0, column=1)
b3 = tk.Button(root, width=10, text='3')
b3.grid(row=0, column=2)
b4 = tk.Button(root, width=10, text='4')
b4.grid(row=1, column=0)
b5 = tk.Button(root, width=10, text='5')
b5.grid(row=1, column=1)
b6 = tk.Button(root, width=10, text='6')
b6.grid(row=1, column=2)

b7 = tk.Button(root, width=10, text='7')
b7.place(x=145, y=120)

root.mainloop()
