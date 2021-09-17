from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
import youtube_dl
from pygame import mixer
import pkg_resources.py2_warn    #got error while making exe without this
# import winsound
import os

mixer.init()
# winsound.PlaySound("./r/Duplex.mp3",winsound.SND_ALIAS | winsound.SND_ASYNC)
def play_music():
    mixer.music.load(r'C:\Users\aryan\Desktop\Duplex.mp3')
    mixer.music.play()

def startDownload():

    global file_size

    try:
        url = urlfield.get()
        downloadButton.config(text = "Downloading...")
        downloadButton.config(state = DISABLED)
        path_to_save = askdirectory()
        if path_to_save is None:
            return

        ydl_opts = {}
        os.chdir(path_to_save)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Done")

        showinfo("Download status","Downloaded Sucessfully")
        urlfield.delete(0,END)
        downloadButton.config(text = "Start Download")
        downloadButton.config(state = NORMAL)

    except Exception as e:
        print(e)
        print("Error")

def startDownloadThread():
    thread = Thread(target = startDownload)
    thread.start()

# GUI
main = Tk()
# play_music()
main.config(background='#cc495b')
main.title("Youtube Downloader")
main.iconbitmap('./res/logo.ico')

main.geometry("600x700")


file2 = PhotoImage(file ='./res/yt.png')
headingIcon = Label(main,image = file2)
headingIcon.pack(side = TOP,pady=10)

# Url text field
urlfield = Entry(main,font =("verdana",18),justify = CENTER)
urlfield.pack(side = TOP,fill = X,padx=30,pady =50)

# Download Button
downloadButton = Button(main,text = "Start Download",font = ("verdana",18),relief = 'ridge',command = startDownloadThread)
downloadButton.pack(side = TOP)

main.mainloop()


