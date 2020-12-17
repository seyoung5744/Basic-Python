import tkinter as tk

def f1(num):
    print(num)
    txt = label.cget('text')
    txt+=num
    label.config(text=txt)

root = tk.Tk()
root.title('계산기')
label = tk.Label(root, width=25, text='')
label.grid(row=0, column=0)
op = ['+', '-', '*','C','=','/']
cnt=0
for i in range(0, 4):
    for j in range(0, 4):
        if 0<=i<=2 and j<3:
            txt = str(3*i+1+j)
            b = tk.Button(root, text=txt, width=25, command=lambda:f1(txt))
        elif i==3 and j==0:
            txt = '0'
            b = tk.Button(root, text=txt, width=25, command=lambda:f1(txt))
        else:
            txt = op[cnt]
            b = tk.Button(root, text=txt, width=25)
            if cnt<len(op)-1:
                cnt+=1

        #b = tk.Button(root, text=txt, width=25)
        b.grid(row=i+1, column=j)
root.mainloop()
