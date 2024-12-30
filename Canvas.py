from tkinter import *

mainwindow=Tk()
label1=Label(mainwindow,text="bgcolor:")
e1=Entry(mainwindow)
label1.grid(row=0,column=0)
e1.grid(row=0,column=1,columnspan=2)

def verify_open():
    def subwindow():
        subwindow=Tk()
        subwindow.geometry("1000x500")
        p=1
        def paint_function(event):
            p=1
            canvas.create_oval(event.x,event.y,event.x+p,event.y+p,fill=color,outline=color)

        header=Label(subwindow,text="This is a simple paint program to enjoy",fg="black",bg="light blue",font=100)
        header.pack(fill=X)

        canvas=Canvas(subwindow,width=1000,height=400)
        canvas.bind("<B1-Motion>",paint_function)      #holds done on mouse and moves cursor 
        canvas.pack()
        
        footer=Label(subwindow,text="Krish D. Shah",fg="black",bg="light blue",font=100)
        footer.pack(fill=X)
        
        def destroy():
            subwindow.destroy()
            
        button=Button(subwindow,text="Close Paint Window",fg="white",bg="red",command=destroy)
        button.pack()
        subwindow.mainloop()
    if e1.get()=='':
        color="black"
    else:
        color=e1.get()
    subwindow()

button1=Button(mainwindow,text="Open New Window",command=verify_open)
button1.grid(row=1,column=1,padx=10)
