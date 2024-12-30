from tkinter import * #automatic abbreviation of Tk() can be used

#creating a window
window_name=Tk()      #root is standard (not mandatory) variable for window creation
# main or window is also used instead of root 

#to change window size
window_name.geometry("500x500")

#addition of title to the window
window_name.title("THIS IS THE MAIN TKINTER WINDOW")

#addition of icon alongside window icon[it needs to be in ".ico" format
'''  window_name.iconbitmap("<icon address here>")   '''  #packed to prevent error as no fileaddress is added

#-->Adding text

label_1=Label(window_name,text="Put your Text Here")   #developed the window but not showcased
label_1.pack()     #for showcasing/displaying the label

label_2=Label(window_name,text="You can put multiple labels",bg="green")
label_n=Label(window_name,text="Some text just to fill",bg="blue")

#fill is used to pad the label to full X alignment
label_2.pack(fill=X)
label_n.pack(fill=X)
            

#Frame() are used to separate group and organise widgets.
#define frame then use frame instead of window in labels/buttons/entries.
frame_0=Frame(window_name)
frame_0.pack()
#use of Button()

button_1=Button(frame_0,text="Enter click me text",padx=10,pady=10,fg="blue",bg="yellow")
#padx and pady are used for padding in x and y alignment
#fg and bg are foreground i.e. text and background color
#padding and colors can be used in Label() as well.

button_1.pack(side=TOP)
#side attribute in pack() is used for alignment
#use [LEFT,RIGHT,TOP,BOTTOM] with uppercase only


frame1=Frame(window_name)
frame2=Frame(window_name)
#command and config functions
def button_func():
    print("Button is clicked and this text is displayed in idle.") #displays text when button is clicked
    button_2.config(text="New text") #modifies the button text after clicked


button_2=Button(frame1,text="Old text",command=button_func)  #don't add () of function created
button_2.pack()
frame1.pack()
def emailbutton_func():
    print("email is:",e1.get())  #get attribute fetches data from Entry  tab to the script for use.
    return


label_3=Label(frame2,text="Enter email below")
e1=Entry(frame2,text="Enter mailid in username@domain.extension")
button_3=Button(frame2,text="Submit",command=emailbutton_func)

label_3.pack(side=TOP)
e1.pack()
button_3.pack()
frame2.pack()    #Always pack the frame()
'''
#adding image
frame3=Frame(window_name)

photo_add=PhotoImage(file="address.ext")
img_lbl=Label(frame3,image=photo_add)
img_lbl.pack()
frame3.pack()
'''
#new subwindow creation using function
def subwindow():
    subwindow=Tk()
    subwindow.geometry("500x500")

    #creating menus
    def menu_function():                        #using one function throughout but you can use multiple functions
        print("Menu function is executed")
    main_menu=Menu(subwindow)                   #creation of menu bar
    subwindow.config(menu=main_menu)            #initialising
    
    file_menu=Menu(main_menu)
    main_menu.add_cascade(label="File",menu=file_menu)   #add Cascade
    file_menu.add_command(label="Section1",command=menu_function)   #add submenus
    file_menu.add_separator()                                   #separator between submenus
    file_menu.add_command(label="Section2",command=menu_function)
    
    menu_bar2=Menu(main_menu)
    main_menu.add_cascade(label="New bar",menu=menu_bar2)
    menu_bar2.add_command(label="Section1",command=menu_function)
    
    

    
    #here we will use grid() for alignment
    label_name=Label(subwindow,text="Name:")
    entry_name=Entry(subwindow)
    label_pswd=Label(subwindow,text="Password:")
    entry_pswd=Entry(subwindow)

    #grid() is a better method than pack() as it is more sorted and easy for alignment.
    label_name.grid(row=0,column=0,sticky=W)
    #sticky contains 4 parameters N,E,W,S-->North,East,West,South for aligning text inside its confinement region
    entry_name.grid(row=0,column=1,ipadx=100,ipady=10)
    #ipadx or ipady is width or size of box area
    label_pswd.grid(row=1,column=0,padx=10,pady=10)
    #padx or pady is for spacing label distance from boundary 
    entry_pswd.grid(row=1,column=1,rowspan=2,columnspan=2)
    #rowspan and columnspan are used for covering row and column that is 1 variable will cover area of 2 rows or 2columns(here).

    #check or tickbox button
    check=Checkbutton(subwindow)
    label_chk=Label(subwindow,text="CLICK ON CHECK BUTTON")
    check.grid(row=2,column=0)
    label_chk.grid(row=2,column=1)
    
    
    #scroll bar
    #options are preferred to be strings
    mylist=["option1","option2","option3","option4","others"]                #for options to be displayed
    scrollbar_default=StringVar(subwindow)     #StringVar is used to set default value which will be modified later
    scrollbar_default.set("<default value here>")       #setting of default value
    scrollbar=OptionMenu(subwindow,scrollbar_default,*mylist)  #creation of scrollbar
    scrollbar.grid(row=3,column=0)     #for alignment

    #--> way2 for scrollbar is using Scrollbar feature
    
    #using bind function instead of command
    #benefit of bind function is that we can use specific keyboard keys to perform operations
    def button_click(event):
        print("Bind function is applied here")
    new_button=Button(subwindow,text="Click new button")
    new_button.bind("<Button-1>",button_click)      #instead of button-1 you can also use any other key
    new_button.grid(row=4,column=0)

    #creating a scale
    scale=Scale(subwindow,from_=0,to=100,orient=HORIZONTAL)      #VERTICAL for orientation along y-axis
    scale.grid(row=5,column=0)

    #destroying window with .destroy()
    #---> use inside a button using function --> "subwindow.destroy()"
    def destroy():
        subwindow.destroy()
    subwindow_close=Button(subwindow,text="Close Sub window",command=destroy)
    subwindow_close.grid(row=6,column=0)
    
    subwindow.mainloop()
    


#button for opening subwindow
button_subwindow=Button(window_name,text="Open SubWindow",command=subwindow)
button_subwindow.pack()

def canvaswindow():
    canvas_window=Tk()
    canvas_window.geometry("1000x1000")
    #Drawing using canvas in Tkinter
    canvas=Canvas(canvas_window,width=500,height=200)
    canvas.pack()

    #creating a line
    canvas.create_line(250,100,500,200,fill="blue")    #always in the form x1,y1,x2,y2

    #creating a rectangle
    canvas.create_rectangle(0,0,250,100,fill="red",outline="blue")

    #creating an oval
    canvas.create_oval(0,100,100,200,fill="red",outline="blue")

    #create a polygon for triangle
    canvas.create_polygon(60,60,60,300,300,300,outline="blue",width=10)   #here first 3 are angles summing up to 180 and next 3 are side length/ points
        #outline for boundary color ; fill for internal color ; width for boundary size ;
    def destroy():
        canvas_window.destroy()
    canvas_button_close=Button(canvas_window,text="Close Canvas window",command=destroy)
    canvas_button_close.pack()

#button to showcase canvas
#the canvas window might be a bit messed up as all sort of available structures were comprised within a single window
canvas_button=Button(window_name,text="Open Canvas window",command=canvaswindow)
canvas_button.pack()

#running window on continuous loop
window_name.mainloop() # if not used window will close as soon as created
