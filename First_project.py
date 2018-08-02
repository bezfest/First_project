from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title("My restaurant")
root.resizable(width=False, height=False)
root.geometry("614x798")

#Photo variables
photo_bg = PhotoImage(file="./Background/Background_current.png")
ph_tra_one = PhotoImage(file="./Traditional_tables/new_tra_icon.png")
ph_tra_two = PhotoImage(file="./Traditional_tables/new_tra_icon2.png")
ph_tra_three = PhotoImage(file="./Traditional_tables/new_tra_icon3.png")
ph_tra_three_des = PhotoImage(file="./Traditional_tables/new_tra_icon3_des.png")
ph_tab_one = PhotoImage(file="./Tables/new_tab_icon.png")
ph_tab_two = PhotoImage(file="./Tables/new_tab_icon2.png")
ph_tab_three = PhotoImage(file="./Tables/new_tab_icon3.png")
ph_tab_four = PhotoImage(file="./Tables/new_tab_icon4.png")
ph_tab_five = PhotoImage(file="./Tables/new_tab_icon5.png")
ph_tab_six = PhotoImage(file="./Tables/new_tab_icon6.png")
ph_tab_seven = PhotoImage(file="./Tables/new_tab_icon7.png")
ph_tra_cb3 = PhotoImage(file="./Checkbuttons/tra_cb3.png")
ph_tra_ty3 = PhotoImage(file="./Checkbuttons/ty_tra_3.png")

#Checkbutton variables
var = IntVar()

#Canvas
canvas = Canvas(width=300, height=200, bg='black')
canvas.pack(expand=YES,fill=BOTH)
canvas.create_image(0, 0,image=photo_bg,anchor=NW)

#Temporary click on table function
def printme(event):
    print("Hello")

#Table traditional 1
table_tra_one = Label(image = ph_tra_one, bd=0)
table_tra_one.place(x=460.5,y=54, anchor="center")
table_tra_one.bind("<Button-1>", printme)
#Table traditional 2
table_tra_two = Label(image = ph_tra_two, bd=0)
table_tra_two.place(x=554.5,y=156, anchor="center")
table_tra_two.bind("<Button-1>", printme)

#At the moment only, yet partially working table+
#3 reservation check
def tra_three(event):
    reservation_tra_three = Label(image=ph_tra_cb3, bd=0)
    reservation_tra_three.place(x=418,y=258, anchor="center")
    cb_tra_three = Checkbutton(reservation_tra_three, bd=0, bg="white", activebackground="white", variable=var, command=tabletra)
    cb_tra_three.place(anchor="center", x=20, y=22)


#Table traditional 3
def tabletra():
    if var.get() == 1:
        table_tra_three_des = Label(root,image = ph_tra_three_des, bd=0)
        table_tra_three_des.place(x=554.5,y=258, anchor="center")
        message = Label(root, image=ph_tra_ty3, bd=0)
        message.place(anchor="center",x=417.5,y=212) #fix Y for 1px (212)
        message.after(2000,message.destroy) #Need to make reservation_tra_three label(from tra_three function) disappear as well - no luck yet
    elif var.get() == 0:
        table_tra_three = Label(root,image = ph_tra_three, bd=0)
        table_tra_three.place(x=554.5,y=258, anchor="center")
        table_tra_three.bind("<Button-1>", tra_three)
    
    

table_tra_three = Label(image = ph_tra_three, bd=0)
table_tra_three.place(x=554.5,y=258, anchor="center")
table_tra_three.bind("<Button-1>", tra_three)

#Table 1
table_one = Label(image = ph_tab_one, bd=0)
table_one.place(x=555.5,y=477.5, anchor="center")
table_one.bind("<Button-1>", printme)

#Table 2
table_two = Label(image = ph_tab_two, bd=0)
table_two.place(x=555.5,y=606.5, anchor="center") #fix button
table_two.bind("<Button-1>", printme)
#Table 3
table_three = Label(image = ph_tab_three, bd=0)
table_three.place(x=555.5,y=735.5, anchor="center") #fix button
table_three.bind("<Button-1>", printme)
#Table 4
table_four = Label(image = ph_tab_four, bd=0)
table_four.place(x=358.5,y=477.5, anchor="center")
table_four.bind("<Button-1>", printme)
#Table 5
table_five = Label(image = ph_tab_five, bd=0)
table_five.place(x=358.5,y=735, anchor="center")
table_five.bind("<Button-1>", printme)
#Table 6
table_six = Label(image = ph_tab_six, bd=0)
table_six.place(x=161.5,y=735.5, anchor="center")
table_six.bind("<Button-1>", printme)
#Table 7
table_seven = Label(image = ph_tab_seven, bd=0)
table_seven.place(x=58.5,y=606.5, anchor="center")
table_seven.bind("<Button-1>", printme)


root.mainloop()
