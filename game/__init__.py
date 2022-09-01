import tkinter
win = tkinter.Tk()
win.resizable(1,1)
win.title("丐")
win.geometry("800x600+1+1")
win.mainloop
def quit():
    win.quit()
def Label(anor,x,y,string):
    son_label = tkinter.Label(win,text=string)
    son_label.place(anchor=anor,relx=x,rely=y)
def Button(x,y,string,anor,cm):
    son_button = tkinter.Button(win,text=string,command=cm)
    son_button.place(anchor=anor,relx=x,rely=y)
