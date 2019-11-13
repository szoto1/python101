import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import HavingFun.openingWebBrowser as open_www
import os
import platform

#Main code

def killApp(appname):

    current_os = platform.system()

    if current_os == "Darwin":
        kill = "pkill "+appname
        try:
            os.system(kill)
        except Exception:
            tk.messagebox.showerror("Killing: "+appname,"Something went wrong.")

        tk.messagebox.showinfo("Killing: "+appname,appname + " killed.")

    elif current_os == "Windows":
        kill = "taskkill /f /im " +appname+ ".exe"

        try:
            os.system(kill)
        except Exception:
            tk.messagebox.showerror("Killing: "+appname,"Something went wrong.")

        tk.messagebox.showinfo("Killing: "+appname,appname + " killed.")

    else:
        tk.messagebox.showerror("Killing: "+appname,"Not supported OS: "+current_os)


app_height = 200
app_width = 200

root = tk.Tk()
root.title("DesktopApp")

#initialize app
canvas = tk.Canvas(root, height=app_height, width=app_width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

gmail_button = ttk.Button(frame, text = "Otwórz gmail'a", command = lambda a=1,b="https://gmail.com": open_www.open_web(a,b))
gmail_button.pack()

mbank_button = ttk.Button(frame, text = "Otwórz mBank", command = lambda a=1,b="https://mbank.pl": open_www.open_web(a,b))
mbank_button.pack()

close_spotify_button = ttk.Button(frame, text = "Zamknij Spotify", command = lambda a="Spotify": killApp(a))
close_spotify_button.pack()

root.mainloop()
exit()
