import tkinter as tk
def f1():
    if label.cget('text')=='hello':
        label.config(text='world')#config():레이블 속성 변경 함수
    else:
        label.config(text='hello')

window = tk.Tk()  #Tk 객체 생성. 기본 윈도우 객체
label = tk.Label(window, text = 'hello', width='100', height='5')#뷰 위젯의 하나인 레이블 객체 생성
btn1 = tk.Button(window, text = 'btn1', command=f1, width='100', height='5')
label.pack()#위젯(레이블, 버튼...)을 윈도우에 붙임
btn1.pack()
window.mainloop()#ui 쓰레드 실행하여 화면에 출력
'''
뷰 위젯(레이블, 버튼...)공통 메서드
config(옵션명=값): 위젯의 설정을 변경하는 메서드
cget(옵션명): 위젯의 옵션 값을 반환
버튼의 command속성은 버튼이 클릭될때 호출될 핸들러 등록 속성
'''