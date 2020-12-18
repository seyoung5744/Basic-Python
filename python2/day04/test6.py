import tkinter as tk

def f1():
    msg = '당신의 선택은 '+str(val.get())
    label.config(text=msg)

root = tk.Tk()
root.title('라디오버튼')
root.geometry('300x200+100+100')
label = tk.Label(root, text='라디오 테스트')
label.pack()
val = tk.IntVar()
r1 = tk.Radiobutton(root, text='사과', variable=val, value=1, command=f1)
r1.pack()
r2 = tk.Radiobutton(root, text='오렌지', variable=val, value=2, command=f1)
r2.pack()
r3 = tk.Radiobutton(root, text='자몽', variable=val, value=3, command=f1)
r3.pack()
root.mainloop()