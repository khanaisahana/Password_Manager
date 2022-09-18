from tkinter import *
import mysql.connector
from PIL import ImageTk, Image

# ----------------------------------------Login form------------------------------------------------------------

loginWin = Tk()
loginWin.geometry('800x700')
loginWin.title("Password Management System")
loginWin.state('zoomed')


def login():
    if user_name.get() == "" or passwd.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=loginWin)
    else:
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="",
                                          database="password_management_system")
            cur = con.cursor()

            cur.execute("select * from user_info where user_name = %s and password = %s",
                        (user_name.get(), passwd.get()))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=loginWin)

            else:
                messagebox.showinfo("Success", "Successfully Login", parent=loginWin)
                close()
                passMain()
                # close()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=loginWin)


def clear():
    uEntry.delete(0, END)
    pEntry.delete(0, END)


def close():
    loginWin.destroy()


bg_frame = Image.open('image/padlock.png')
photo = ImageTk.PhotoImage(bg_frame)
bg_panel = Label(loginWin, image=photo)
bg_panel_image = photo
bg_panel.place(x=100, y=150)

Label(loginWin, text="Password Manager ", width=20, fg='royal blue', font='Verdana 30 bold').place(x=70, y=40)

heading = Label(loginWin, text="Sign In", width=20, fg='royal blue', font='Verdana 30 bold')
heading.place(x=800, y=150)

# Entry Box
user_name = StringVar()
passwd = StringVar()

uname = Label(loginWin, text="User Name", bg='sky blue', fg='black', font='Verdana 12', width=15)
uname.place(x=800, y=300)

uEntry = Entry(loginWin, textvariable=user_name, width=25, background='white', font='Verdana 15')
uEntry.focus()
uEntry.place(x=1000, y=300)

passWD = Label(loginWin, text="Password", bg='sky blue', fg='black', font='Verdana 12', width=15)
passWD.place(x=800, y=400)

pEntry = Entry(loginWin, show='*', textvariable=passwd, width=25, background='white', font='Verdana 15')
pEntry.place(x=1000, y=400)

Button(loginWin, text='Login', width=13, bg='dodger blue', fg='black', font='Verdana 12 bold', activeforeground='white',
       activebackground='blue', command=login).place(x=880,
                                                     y=550)

Button(loginWin, text='Clear', width=13, bg='dodger blue', fg='black', font='Verdana 12 bold', activeforeground='white',
       activebackground='blue', command=clear).place(x=1130, y=550)


# ----------------------------------------Registration form------------------------------------------------------------


def signup():
    def action():
        if email_id.get() == "" or username.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=regWin)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=regWin)
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="",
                                              database="password_management_system")
                cur = con.cursor()
                sql = "INSERT INTO user_info (email_id, user_name, password) VALUES (%s,%s,%s)"
                val = (email_id.get(),
                       username.get(),
                       password.get())

                cur.execute(sql, val)
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registration Successfull", parent=regWin)
                clear()
                switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=regWin)

    def switch():
        regWin.destroy()

    def clearform():
        email_id.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)
        very_pass.delete(0, END)

    regWin = Tk()
    regWin.geometry('600x600')
    regWin.title("Password Management System")
    regWin.state('zoomed')

    # heading label
    Label(regWin, text='', width=70, fg='white', bg='light sky blue', font='Verdana 25 bold').place(x=0, y=0)
    Label(regWin, text="Password Manager ", width=20, fg='black', bg='light sky blue', font='Verdana 30 bold').place(
        x=0, y=45)
    Label(regWin, text='Password Manager ', width=70, fg='light sky blue', bg='light sky blue',
          font='Verdana 30 bold').place(x=540, y=45)
    Label(regWin, text='', width=70, fg='white', bg='light sky blue', font='Verdana 25 bold').place(x=0, y=97)

    heading = Label(regWin, text="Sign Up", width=20, fg='royal blue', font='Verdana 30 bold')
    heading.place(x=500, y=150)

    emailid = Label(regWin, text="Email ID", bg='sky blue', fg='black', font='Verdana 12', width=15)
    emailid.place(x=500, y=250)

    email_id = StringVar()
    email_id = Entry(regWin, width=25, background='white', font='Verdana 15', textvariable=email_id)
    email_id.place(x=700, y=250)

    username = Label(regWin, text="User Name", bg='sky blue', fg='black', font='Verdana 12', width=15)
    username.place(x=500, y=320)

    username = Entry(regWin, width=25, background='white', font='Verdana 15')
    username.place(x=700, y=320)

    password = Label(regWin, text="Password", bg='sky blue', fg='black', font='Verdana 12', width=15)
    password.place(x=500, y=390)

    password = Entry(regWin, width=25, background='white', font='Verdana 15', show="*")
    password.place(x=700, y=390)

    very_pass = Label(regWin, text="Verify Password", bg='sky blue', fg='black', font='Verdana 12', width=15)
    very_pass.place(x=500, y=460)

    very_pass = Entry(regWin, width=25, background='white', font='Verdana 15', show="*")
    very_pass.place(x=700, y=460)

    # button login and clear
    btn_signup = Button(regWin, text="Signup", width=13, bg='dodger blue', fg='black', font='Verdana 12 bold',
                        activeforeground='white',
                        activebackground='blue', command=action)
    btn_signup.place(x=570, y=560)

    btn_login = Button(regWin, text="Clear", width=13, bg='dodger blue', fg='black', font='Verdana 12 bold',
                       activeforeground='white',
                       activebackground='blue', command=clearform)
    btn_login.place(x=800, y=560)

    Label(regWin, text='Already on Password Manager?', width=30, font='Verdana 12', fg='blue').place(x=550, y=660)
    sign_in_btn = Button(regWin, text="Sign In Now", bg='dodger blue', fg='black', font='Verdana 10 bold',
                         activebackground='blue', activeforeground='white', width=15, command=switch)
    sign_in_btn.place(x=850, y=660)

    regWin.mainloop()


# -------------------------------password manager main page coding-----------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk, messagebox
from db_operations import Db_operation


def passMain():
    def saveRecord():
        for item in record_tree.get_children():
            record_tree.delete(item)
        data = {'website': website.get(), 'user_name': user_name.get(), 'password': password.get()}
        db = Db_operation()
        db.create_record(data)
        print(data)
        showRecord()
        messagebox.showinfo("Save", "Successfully Saved Record ", parent=root)

    def updateRecord():
        for item in record_tree.get_children():
            record_tree.delete(item)
        data = {'website': website.get(), 'user_name': user_name.get(), 'password': password.get()}
        db = Db_operation()
        db.update_record(data)
        showRecord()
        messagebox.showinfo("Update", "Successfully Updated Record ", parent=root)

    def delete_record():
        for item in record_tree.get_children():
            record_tree.delete(item)
        data = {'user_name': user_name.get()}
        db = Db_operation()
        db.delete_record(data)
        showRecord()
        messagebox.showinfo("Delete", "Successfully Deleted Record ", parent=root)

    def showRecord():
        for item in record_tree.get_children():
            record_tree.delete(item)
        db = Db_operation()
        record_list = db.show_record()
        for record in record_list:
            record_tree.insert('', END, values=(record[2], record[3], record[4]))

    def copy_password():
        root.clipboard_clear()
        root.clipboard_append(password.get())
        message = 'Password Copied'
        title = 'Copy'
        if password.get() == '':
            message = 'Box is Empty'
            title = 'Copy'
        messagebox.showinfo(title, message, parent=root)

    # create a function to display the selected row from treeview
    def displaySelectedItem(a):
        # clear entries
        website.delete(0, END)
        user_name.delete(0, END)
        password.delete(0, END)

        selectedItem = record_tree.selection()[0]
        website.insert(0, record_tree.item(selectedItem)['values'][0])
        user_name.insert(0, record_tree.item(selectedItem)['values'][1])
        password.insert(0, record_tree.item(selectedItem)['values'][2])

    def searchRecord():
        for item in record_tree.get_children():
            record_tree.delete(item)
        data = {'website': search.get()}
        db = Db_operation()
        record_list = db.search_record(data)
        print(record_list)
        for record in record_list:
            record_tree.insert('', END, values=(record[2], record[3], record[4]))

    root = Tk()
    root.title('PASSWORD MANAGEMENT SYSTEM')
    root.geometry('800x1000')
    root.state('zoomed')

    record_tree = ttk.Treeview(root, selectmode='browse')
    record_tree.place(x=250, y=550)

    vsb = ttk.Scrollbar(root, orient="vertical", command=record_tree.yview)
    vsb.place(x=250 + 350 + 350 + 350, y=550, height=200 + 30)

    record_tree.configure(yscrollcommand=vsb.set)

    a = ['Website', 'Username', 'Password']
    record_tree["columns"] = ("1", "2", "3")
    record_tree['show'] = 'headings'
    record_tree.column("1", width=350, anchor='c')
    record_tree.column("2", width=350, anchor='c')
    record_tree.column("3", width=350, anchor='c')
    record_tree.heading("1", text=a[0])
    record_tree.heading("2", text=a[1])
    record_tree.heading("3", text=a[2])

    Label(root, text='', width=70, fg='light sky blue', bg='light sky blue', font='Verdana 25 bold').place(x=0, y=0)
    Label(root, text='Password Management System', width=68, fg='black', bg='light sky blue',
          font='Verdana 25 bold').place(x=0,
                                        y=45)
    Label(root, text='', width=70, fg='black', bg='sky blue', font='Verdana 25 bold').place(x=0, y=90)

    Label(root, text="website", bg='sky blue', fg='black', font='Verdana 12', width=15).place(x=500, y=200)
    Label(root, text="user name", bg='sky blue', fg='black', font='Verdana 12', width=15).place(x=500, y=250)
    Label(root, text="password", bg='sky blue', fg='black', font='Verdana 12', width=15).place(x=500, y=300)

    website = Entry(root, width=25, background='white', font='Verdana 15')
    website.place(x=750, y=200)
    website.focus()
    user_name = Entry(root, width=25, background='white', font='Verdana 15')
    user_name.place(x=750, y=250)
    password = Entry(root, width=25, background='white', font='Verdana 15', show='*')
    password.place(x=750, y=300)
    search = Entry(root, width=40, font='Verdana 15')
    search.place(x=620, y=500)

    Button(root, text='SAVE', bg='pale green3', fg='black', font='Verdana 10 bold',
           activebackground='blue', activeforeground='white', width=15, command=saveRecord).place(x=250, y=400)
    Button(root, text='UPDATE', bg='gold2', fg='black', font='Verdana 10 bold',
           activebackground='blue', activeforeground='white', width=15, command=updateRecord).place(x=550, y=400)
    Button(root, text='DELETE', bg='indian red2', fg='black', font='Verdana 10 bold',
           activebackground='blue', activeforeground='white', width=15, command=delete_record).place(x=850, y=400)
    Button(root, text='COPY PASSWORD', bg='light pink2', fg='black', font='Verdana 10 bold',
           activebackground='blue', activeforeground='white', width=15, command=copy_password).place(x=1150, y=400)

    Button(root, text='Show All Records', bg='dodger blue', fg='black', font='Verdana 10 bold',
           activebackground='blue', activeforeground='white', width=20, command=showRecord).place(x=250, y=500)

    Button(root, text="Search", bg='medium blue', fg='white', font='Verdana 10 bold', activebackground='lightGrey',
           activeforeground='black', width=15, command=searchRecord).place(x=1150, y=500)

    record_tree.bind('<<TreeviewSelect>>', displaySelectedItem)
    root.mainloop()


# signup button
Label(loginWin, text='New to Password Manager?', width=30, font='Verdana 12', fg='blue').place(x=850, y=650)
sign_up_btn = Button(loginWin, text="Sign Up Now", command=signup, bg='dodger blue', fg='black', font='Verdana 10 bold',
                     activebackground='blue', activeforeground='white', width=15)
sign_up_btn.place(x=1120, y=650)

loginWin.mainloop()
