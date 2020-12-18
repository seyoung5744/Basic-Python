import tkinter as tk
from PIL import Image
from PIL import ImageTk

'''
    pillow : 이미지 처리 라이브러리
'''
root = tk.Tk()
img = Image.open("a.jpg") # 이미지 파일 오픈
img = img.resize((300,200))
src = ImageTk.PhotoImage(image=img) # label에 출력할 수 있는 형태로 변환
img_label = tk.Label(root, image=src)
img_label.pack()
root.mainloop()