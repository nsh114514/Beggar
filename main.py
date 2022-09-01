import tkinter
import time
win = tkinter.Tk()
win.resizable(0,0)
win.title("丐")
win.geometry("800x600+1+1")
photo = tkinter.PhotoImage(file="../res/background.png")
bgd = tkinter.Label(image=photo)
bgd.place(relx=0.5,rely=0.5,anchor="center")
son_label = tkinter.Label(win,text="Beggar",font=("Sans Serif",40))
son_label.place(anchor="center",relx=0.5,rely=0.3,height=60,width=120)
def singleplayer():
    import time
    time = time.time()
    print("time:"+str(time),"nope")
def quitgame():
    import time
    time = time.time()
    print("time:"+str(time),"quiting...")
    win.quit()
son_button1 = tkinter.Button(win,text="单机游戏",command=singleplayer)
son_button1.place(anchor="center",relx=0.5,rely=0.4,height=20,width=120)
son_button2 = tkinter.Button(win,text="退出",command=quitgame)
son_button2.place(anchor="center",relx=0.55,rely=0.6,height=20,width=55)
time = time.time()
print("time:"+str(time),"running...")
win.mainloop()