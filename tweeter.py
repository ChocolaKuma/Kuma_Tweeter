import tweepy
import tkinter as tk
from tkinter import ttk
import webbrowser
import os
import urllib.request
import keys

#Api refrance
#http://tweepy.readthedocs.io/en/v3.5.0/api.html

usedacount = keys.usedacount
access_token = keys.access_token
access_token_secret = keys.access_token_secret
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
useravi= keys.useravi
UserName = keys.UserName

GetIcon = False

LARGE_FONT= ("Verdana", 12)
MED_FONT= ("Verdana", 8)

starttext = """This Program is still in development \nPlease keep that in mind. \nNothing in this is the final product."""


class POSIS(tk.Tk):

    def __init__(self, *args, **kwargs):       
        if(GetIcon==True):
            global useravi
            urllib.request.urlretrieve(useravi, "src/avi.png")
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self,default="src/icons/icon.ico")
        tk.Tk.wm_title(self,"KumaTweeter © 2017")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, Tweet,AccountInfo, AccountStats):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=starttext, font=LARGE_FONT)
        label.grid(row=1,column=1,columnspan=2)

        button = ttk.Button(self, text="Accept",
                            command=lambda: controller.show_frame(Tweet))
        button.grid(row=2,column=1)

        button1 = ttk.Button(self, text="Decline",
                            command=lambda: quit())
        button1.grid(row=2,column=2)

class Tweet(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="Tweet",
                            command=lambda: controller.show_frame(Tweet))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Account Info",
                            command=lambda: controller.show_frame(AccountInfo))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Account Stats",
                            command=lambda: controller.show_frame(AccountStats))
        button3.grid(row=2,column=3)         
##         TODO somthing Buggy Here "(widgetName, self._w) + extra + self._options(cnf))
##_tkinter.TclError: image "avi.png" doesn't exist""
##
##        avi = tk.PhotoImage(file="avi.png")
##        avi = avi.zoom(25) 
##        avi = avi.subsample(40)    
##        l = tk.Label(self, image="avi.png").grid(row=4,column=1)
##
        global e
        e = ttk.Entry(self)
        e.grid(row=5,column=1,columnspan=2)
        button4 = ttk.Button(self, text="Tweet",
                            command=lambda: tweetit())
        button4.grid(row=5,column=3)        


        
        
class AccountInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="Tweet",
                            command=lambda: controller.show_frame(Tweet))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Account Info",
                            command=lambda: controller.show_frame(AccountInfo))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Account Stats",
                            command=lambda: controller.show_frame(AccountStats))
        button3.grid(row=2,column=3)        
        label = tk.Label(self, text="Handle: "+UserName, font=MED_FONT)
        label.grid(row=3,column=1,columnspan=3)
        #TODO add Token output to show if it is correct
        label1 = tk.Label(self, text="access_token: "+access_token, font=MED_FONT)
        label1.grid(row=5,column=1,columnspan=3)
        label2 = tk.Label(self, text="access_token_secret: "+access_token_secret, font=MED_FONT)
        label2.grid(row=6,column=1,columnspan=3)        
        label3 = tk.Label(self, text="consumer_key: "+consumer_key, font=MED_FONT)
        label3.grid(row=7,column=1,columnspan=3)
        label4 = tk.Label(self, text="consumer_secret: "+consumer_secret, font=MED_FONT)
        label4.grid(row=8,column=1,columnspan=3)
        
def tweetit():
    print("Message Tweet")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet = e.get()
    print(tweet)
    api.update_status(tweet)
    
class AccountStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        user = api.me()
        button1 = ttk.Button(self, text="Tweet",
                            command=lambda: controller.show_frame(Tweet))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Account Info",
                            command=lambda: controller.show_frame(AccountInfo))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Account Stats",
                            command=lambda: controller.show_frame(AccountStats))
        button3.grid(row=2,column=3)
        Nickname = ""
        Handle = "@"+user.screen_name
        Following = 0 #Not supported in tweepy
        Followers = user.followers_count
        Following = str(Following)
        Followers = str(Followers)

        label1 = tk.Label(self, text="Nickname: "+Nickname, font=MED_FONT)
        label1.grid(row=3,column=1,columnspan=3)
        label2 = tk.Label(self, text="Handle: "+Handle, font=MED_FONT)
        label2.grid(row=4,column=1,columnspan=3)        
        label3 = tk.Label(self, text="Following: "+Following, font=MED_FONT)
        label3.grid(row=5,column=1,columnspan=3)
        label4 = tk.Label(self, text="Followers: "+Followers, font=MED_FONT)
        label4.grid(row=6,column=1,columnspan=3)   
app = POSIS()
app.mainloop()
#http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/
