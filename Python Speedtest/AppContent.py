import tkinter as tk
import speedtest as test
import threading

class AppContent(object):
    def __init__(self,master):
        root = master     
        self.root = root
    
        #Window Settings 
        root.title("Speedtest")
        root.geometry("370x600")
        root.resizable(False,False)
        root.configure(bg="#1C113B")
        self.icon = tk.PhotoImage(file="icon.png")
        root.iconphoto(False, self.icon)
        
        #Title banner Settings 
        self.title = tk.PhotoImage(file="title.png")
        self.topTitle = tk.Label(root, image=self.title,bg="#1C113B") 
        self.topTitle.place(x=40,y=10)    

        #Meter image Settings 
        self.meter = tk.PhotoImage(file="meter.png")
        self.topMeter = tk.Label(root, image=self.meter,bg="#1C113B") 
        self.topMeter.place(x=30,y=120)        

        #Line Canvas Settings 
        self.canvas = tk.Canvas(root,width=330,height=150,bg="#1C113B",highlightthickness=0)
        self.canvas.place(x=15,y=300)
        self.canvas.create_line(20,5,320,5,width=3)
        self.canvas.create_line(20,100,320,100,width=3)

        #Ping Label Settings 
        self.pingLabel = tk.Label(root,text = "PING",font=('COURIER', 16, 'bold'),bg="#1C113B",fg="White").place(x=80,y=315)
        self.pingV = tk.Label(root, text="00 ms", font=('COURIER', 18, 'bold'),bg="#1C113B",fg="White",justify="center",width=12)
        self.pingV.place(x=20,y=345)   
 
        #Download Label Settings 
        self.dlLabel = tk.Label(root, text = "DOWNLOAD",font=('COURIER',18, 'bold'),bg="#1C113B",fg="White").place(x=120,y=200)
        self.download = tk.Label(root, text="00 mbps", font=('COURIER',16, 'bold'),bg="#1C113B",fg="White",justify="center",width=15)
        self.download.place(x=80,y=230) 

        #Upload Label Settings 
        self.upLabel = tk.Label(root, text="UPLOAD",font=('COURIER',16, 'bold'),bg="#1C113B",fg="White").place(x=210,y=315)
        self.upload = tk.Label(root, text="00 mbps", font=('COURIER',18, 'bold'),bg="#1C113B",fg="White",justify="center",width=12)
        self.upload.place(x=170,y=345)     
       
        #Start Button Settings 
        self.threadCheck = threading.Thread(target=self.check)
        self.startButton = tk.PhotoImage(file="start.png")
        self.button = tk.Button(root, image= self.startButton, bg="#1C113B", bd=0, activebackground="#1C113B",cursor="hand2",command=self.threadCheck.start)
        self.button.place(x=30,y=420)
    

    def check(self):
        net = test.Speedtest()

        self.Getting = tk.Label(self.root, text = "Testing download speed..." , font=('COURIER',15),bg="#1C113B",fg="White")
        self.Getting.place(x=30,y=510)        
        
        #Getting and displaying download speed
        dlSpeed = round(net.download()/(1024*1024),2)
        self.download.config(text=str(dlSpeed)+' mbps')
        
        self.Getting.config(text="Testing upload speed...")  
        #Getting and displaying upload speed              
        upSpeed = round(net.upload()/(1024*1024),2)        
        self.upload.config(text=str(upSpeed)+' mbps')
                
        #Getting and displaying ping        
        netPing = []
        net.get_servers(netPing)                              
        self.pingV.config(text=str(round(net.results.ping,2))+' ms')  
        self.Getting.config(text="Speedtest complete...")