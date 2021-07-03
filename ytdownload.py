from tkinter import *
from tkinter import filedialog
from urllib.request import urlopen
import pytube
from pytube import YouTube as Youtube
import webbrowser

class Application:
    def __init__(self, master=None):
        root.title("YT Video Download")
        root.iconbitmap("youtube_logo_mint_icon_134951.ico")
        size = 1
        self.fonte = ("Verdana", "12")

        self.container1 = Frame()
        self.container1["padx"] = 20
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame()
        self.container2["padx"] = 20
        self.container2["pady"] = 10
        self.container2.pack()

        self.container3 = Frame()
        self.container3["padx"] = 20
        self.container3["pady"] = 10
        self.container3.pack()

        self.container4 = Frame()
        self.container4["padx"] = 20
        self.container4["pady"] = 10
        self.container4.pack()


        self.container5 = Frame()
        self.container5["padx"] = 20
        self.container5["pady"] = 10
        self.container5.pack()


        self.container6 = Frame()
        self.container6["padx"] = 20
        self.container6["pady"] = 10
        self.container6.pack()

        self.container7 = Frame()
        self.container7["padx"] = 20
        self.container7["pady"] = 10
        self.container7.pack()

        self.container8 = Frame()
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container10 = Frame()
        self.container10["padx"] = 20
        self.container10["pady"] = 10
        self.container10.pack()

        def downloadAction(url2):
            url = str(url2)
            print(url)
            youtube = Youtube(str(url));
            print(youtube)

            #video =
            #print(youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(directory.get()));
            youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(directory.get());

            #video.download(directory.get());


        def downloadClick():
            parts = self.urlentry.get().split(";")
            for i in range(len(parts)):
                downloadAction(parts[i])

        self.button2 = Button(self.container6, text="Download", command = downloadClick)
        self.button2.pack()

        self.direntrylbl = Label(self.container6, text="Select Directory")
        self.direntrylbl['font'] = ('calibri', '12', 'bold')

        directory = StringVar()

        def selectDirectory():
            directory_selected = filedialog.askdirectory()
            directory.set(directory_selected)
            print(directory.get())

        self.direntry = Entry(self.container8, textvariable=directory)
        self.direntry.pack(side=LEFT)
        self.btnFind = Button(self.container8, text="Select folder", command=selectDirectory)
        self.btnFind.pack(side=RIGHT)


        self.lblurl = Label(self.container1, text = "Url do video: (separe diferentes urls com ';')")
        self.lblurl['font'] = ('calibri','12', 'bold')
        self.lblurl.pack(side=LEFT)

        self.urlentry = Entry(self.container2,
        text="VideoLink: ", font=self.fonte)
        self.urlentry.pack(side=RIGHT)



        self.widget1 = Frame()
        self.widget1.pack()
        self.sair = Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('calibri', '10')
        self.sair['width'] = 5
        self.sair['command'] = self.widget1.quit
        self.sair.pack()

        def callback(url):
            webbrowser.open_new(url)

        self.credits = Label(self.container10, text = "MADE BY Henrique-dSGP | Follow me https://github.com/Henrique-dSGP", fg="blue", cursor="hand2")
        self.credits['font'] = ('arial', '8', 'bold')
        self.credits.pack()
        self.credits.bind("<Button-1>", lambda e: callback("https://github.com/Henrique-dSGP"))

root = Tk()
Application(root)
root.mainloop()
