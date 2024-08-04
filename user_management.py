import tkinter as tk

def noGUIuser():
    def cUser():
        pass

    def delUser():
        pass

    def modUser():
        pass


    def idUser():
        pass

def GUIuser():
    def cUser():
        usergui.destroy()
        cUserGUI = tk.Tk()
        cUserGUI.geometry("520x900")
        nuntext=tk.Label(cUserGUI,text="Enter new username:")
        nuntext.place(x=10,y=40)
        nunentry = tk.Entry(cUserGUI)
        nunentry.place(x=130,y=40)
    def delUser():
        pass
    
    def modUser():
        pass
    usergui = tk.Tk()
    usergui.geometry("200x120")
    cub = tk.Button(usergui,text="Create user",command=lambda:[cUser()])
    cub.grid(column=0,row=0,pady=2)
    mub = tk.Button(usergui,text="Modify User")
    mub.grid(column=0,row=1,pady=2)
    dub = tk.Button(usergui, text="Delete User")
    dub.grid(column=0,row=2,pady=2)

    usergui.mainloop()


GUIuser()