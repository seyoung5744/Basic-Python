import tkinter as tk

root = tk.Tk()
root.title('제목줄')
root.geometry('300x200+100+100')#윈도우 창의 크기(300, 200)와 위치(100,100) 지정
root.resizable(False, False)#가로, 세로 길이 조정 불가
b1 = tk.Button(root, width=10, text='left')
b1.pack(side='left')#위치 왼쪽 지정
b2 = tk.Button(root, width=10, text='right')
b2.pack(side='right')
b3 = tk.Button(root, width=10, text='top')
b3.pack(side='top')
b4 = tk.Button(root, width=10, text='bottom')
b4.pack(side='bottom')

root.mainloop()
