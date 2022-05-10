from tkinter import *
from tkinter import ttk
from tkinter import messagebox



FirstWindow=Tk()
FirstWindow.title("LIBRARY MANAGEMENT SYSTEM BY ADITYA")
FirstWindow.geometry("1900x1065+0+0")
bg=PhotoImage(file="C:/Users/Aaditya/Desktop/LIBRARY MANAGEMENT SYSTEM/FirstPage.png")
label_image=Label(FirstWindow,image=bg)
label_image.place(x=0,y=0,height=1000,width=1900)
entry_username=Entry(FirstWindow,font=("Bahnschrift SemiBold",20))
entry_username.place(x=1350,y=760,width=400)

entry_password=Entry(FirstWindow,show="°",font=("Bahnschrift SemiBold",20))
entry_password.place(x=1350,y=850,width=400)
#def button_login(event=None):
#    command=SecondWindow
def SecondWindow():

    if entry_username.get()=="Librarian" and entry_password.get()=="librarian123":
        SecondWindow=Tk()
        SecondWindow.title("LIBRARIAN LOGIN")
        SecondWindow.geometry("1900x1065+0+0")

        SecondWindow.mainloop()
#def ThirdWindow():
    if entry_username.get()=="" and entry_password.get()=="":
        FirstWindow.destroy()
        ThirdWindow=Tk()
        ThirdWindow.title("STUDENT LOGIN")
        ThirdWindow.geometry("1900x1065+0+0")
        bg=PhotoImage(file="C:/Users/Aaditya/Desktop/LIBRARY MANAGEMENT SYSTEM/Screenshot (21).png")

        
        label_image=Label(ThirdWindow,image=bg)
        label_image.place(x=0,y=0,height=1000,width=1900)

        view_button_image=PhotoImage(file="./view_button.png")
        button_booklist=Button(label_image,image=view_button_image,borderwidth=0)
        button_booklist.place(x=465,y=435,width=1250,height=135)

        view_button_image1=PhotoImage(file="./view_button2.png")
        button_search=Button(label_image,image=view_button_image1,borderwidth=0)
        button_search.place(x=465,y=649.5,width=1250,height=135)
        ThirdWindow.mainloop()
    else:
        messagebox.showerror("ERROR404","Username and Password are incorrect.\nEnter the correct username and password.")
    
































button_login=Button(FirstWindow,font=("Bookman Old Style",20),text="Login",command=SecondWindow,bg="#BD4FEC",fg="white")
button_login.place(x=1400,y=900,width=100,height=40)
FirstWindow.mainloop()
