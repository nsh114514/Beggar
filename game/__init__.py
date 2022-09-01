"""
这是为了一个东东
"""
import tkinter
win = tkinter.Tk()
def start(winname,heigh,wheigh):
    import tkinter
    win = tkinter.Tk()
    win.resizable(1,1)
    win.title(winname)
    win.geometry(str(heigh)+"x"+str(wheigh)+"+1+1")
def quit():
    win.quit()
def Label(auer,x,y):
    son = tkinter.Label(win,auther=auer,relx=x,rely=y)
