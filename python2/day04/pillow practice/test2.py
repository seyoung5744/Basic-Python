import tkinter as tk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
cnt=0
imgs = ['a.jpg', 'b.jpg', 'c.jpg']
src = None

def f1():
    global cnt
    if cnt==0:
        tk.messagebox.showinfo(title='오류', message='맨 앞입니다')
    else:
        cnt-=1
        viewImg()

def f2():
    global cnt
    if cnt == 2:
        tk.messagebox.showinfo(title='오류', message='맨 끝입니다')
    else:
        cnt += 1
        viewImg()

def viewImg(): # 이미지를 읽어서 레이블에 출력
    global src
    print(imgs[cnt])
    img = Image.open(imgs[cnt])
    img = img.resize((300, 200))
    src = ImageTk.PhotoImage(image=img)
    img_label['image'] = src

root = tk.Tk()
img = Image.open(imgs[cnt])
img = img.resize((300, 200))
src = ImageTk.PhotoImage(image=img)

img_label = tk.Label(root, image=src)
img_label.pack()

prev = tk.Button(root, text='prev', command=f1)
prev.pack()
next = tk.Button(root, text='next', command=f2)
next.pack()

root.mainloop()
