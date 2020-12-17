import tkinter as tk
def f1(e):#첫 번째 파라메터는 발생한 이벤트 객체
    print('왼쪽 버튼 클릭')
    print(e.x, e.y)
def f2(e):
    print('오른쪽 버튼 클릭')
    print(e.x, e.y)
def f3(e):
    print('엔트리에 엔터 이벤트 발생')

def f4(e):
    print(e)

root = tk.Tk()
b = tk.Button(root, text='btn', width=30)
e = tk.Entry(root, width=30)

b.pack()
e.pack()
b.bind('<Button-1>', f1)#<Button-1>:왼쪽, <Button-2>:가운데, <Button-3>:오른쪽 버튼클릭
b.bind('<Button-3>', f2)
e.bind('<Enter>', f3)
e.bind('<Return>', f4)#엔트리에서 엔터키 누르면 이벤트 발생

root.mainloop()