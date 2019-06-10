from tkinter import *
from tkinter import filedialog
import os

import youtube_dl

window=Tk()
window.title('Youtube Video Downloader')
window.configure(background='snow')
window.geometry('1280x720')

def clear():
    entry1.delete(first=0,last=100)

def save_to():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def download():
        URL = entry1.get()
        PATH = entry2.get()
        ydl_opts = {}
        os.chdir(PATH)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            window.title('Downloading... ' + URL)
            ydl.download([URL])
        print(ydl_opts)
        notif='Your video Downloaded'
        window.title(notif)


folder_path=StringVar()

lbl1=Label(window,text='Video URL', width=20, fg='black',bg='sandy brown',font=('times',15,'bold'))
lbl1.place(x=100,y=100)
lbl2=Label(window,text='Save to',width=20,fg='black',bg='sandy brown',font=('times',15,'bold'))
lbl2.place(x=100,y=300)
lbl3=Label(window,text='YOUTUBE VIDEO DOWNLOADER', width=30, fg='white',bg='red',font=('times',15,'bold'))
lbl3.place(x=400,y=50)

entry1= Entry(window,width=55,fg='black',bg='grey')
entry1.place(x=400,y=100)
entry2= Entry(window,width=55,textvariable=folder_path,fg='black',bg='grey')
entry2.place(x=400,y=300)

btn1=Button(window,text='Clear',command=clear ,width=20,fg='snow',bg='red',activebackground='grey')
btn1.place(x=800,y=100)
btn2=Button(window,text='Save to',width=20,command=save_to,fg='snow',bg='red',activebackground='grey')
btn2.place(x=800,y=300)
btn3=Button(window,text='Download',width=20,command=download,fg='black',bg='white',activebackground='grey')
btn3.place(x=450,y=500)



window.mainloop()

