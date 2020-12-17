import socket, threading
import tkinter as tk

client_socket = None
label = None
Msg = None
root = None

def send(e): # 이벤트 핸들러 함수. 엔트리 엔터 입력 시 호출
    global client_socket
    
    msg = Msg.get()#입력박스에 입력한 텍스트 읽어옴
    client_socket.sendall(msg.encode())
    Msg.delete(0, tk.END) # 보낸 메시지는 지움

def th_read():
    global client_socket
    while True:
        data = client_socket.recv(1024)
        msg = data.decode()
        #print(msg)
        
        label.configure(text=label.cget('text')+'\n'+msg)
        if msg=='/stop':
            break
        
    print('서버 메시지 출력 쓰레드 종료')
    
def ui_init():
    global label
    global Msg
    global root

    root = tk.Tk() #윈도우 창

    root.title('chatting room')#윈도우 제목창 타이틀 출력
    root.geometry("400x400")#윈도우 가로 세로 길이
    frm = tk.Frame(root)    #윈도우에 프레임을 생성. 화면 분할

    #레이블 생성
    label = tk.Label(root, text = '', relief = 'groove', borderwidth = 1, padx = 400, pady = 150)
    #입력박스 생성
    Msg = tk.Entry(root,width = 100)
    Msg.bind('<Return>', send)
    #버튼 생성
    #btn = tk.Button(root, text="send", command = send)

    #위젯들을 프레임에 부착
    Msg.pack()
    frm.pack()
    label.pack()   
    #btn.pack()
    
    

def main():
    global root
    global client_socket
    
    HOST = 'localhost'
    PORT = 9999

    #통신할 소켓 오픈 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #서버에 연결요청. server ip, port
    client_socket.connect((HOST, PORT))

    ui_init()
    
    t2 = threading.Thread(target=th_read, args=())
    t2.start()

    root.mainloop()
    #client_socket.close()

main()
