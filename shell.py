import time
import os
import tkinter as tk

os.system('cls')
version = "1.0.0.0"
print("Python OS [Version "+version+"]")
print("Author Wiktor M")

def login():
    root=tk.Tk()
    usernamet = tk.Label(root,text="Username:")
    usernamet.grid(row=0,column=0)
    usertext = tk.Entry(root)
    usertext.grid(row=0,column=1)
    passwordt = tk.Label(root,text="Password:")
    passwordt.grid(row=1,column=0)
    passtext = tk.Entry(root)
    passtext.grid(row=1,column=1)
    root.mainloop()

class colour:
    def __init__(self,code:str) -> None:
        self.code:str = code
    def paint(self,text:str,bold:bool=False) -> str:
        if not bold:
            return f"{self.code}{text}\033[0m"
        elif bold:
            return f"{self.code}\033[1m{text}\033[0m"

BLUE = colour("\033[94m")
GREEN = colour('\033[0;32m')
YELLOW = colour("\033[0;33m")
GREY = colour('\033[0;30m')


leave = False
while leave != True:
    user = input("> ")
    #help
    if user == "help" or user == "?":
        # Display help with colored items
        print(
            BLUE.paint("Available commands:\n",True),
            GREEN.paint("exit          "),GREY.paint("- Exit the program\n"),
            GREEN.paint("help          "),GREY.paint("- Show this help message\n"),
            GREEN.paint("login         "),GREY.paint("- Login on the console\n"),
            GREEN.paint("login [GUI]   "),GREY.paint("- Use this to log in with a window"),
            GREEN.paint("print [text]  "),GREY.paint("- Print the text inside the brackets\n")
        )

    # elif user == "credit":
    #     print(f"{BLUE}Wiktor and NothingItIs{RESET}")
    #exit
    elif user == "exit":
        print("Done")
        leave = True
        os.system('cls')
    elif user == "login":
        usernameask = input("Enter your username \n> ")
        passwordask = input("Enter your password \n> ")
        
    elif user == "login [GUI]":
        login()
    #print
    elif user.startswith("print [") and user.endswith("]"):
        tprint = user[7:-1]
        print(tprint)
    else:
        print("Invalid command. Type help or ? to see commands")
    
