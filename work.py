#Created by Animesh Srivastava  June 2018
#Information replace Bureau with Desktop in case you are an English user in the CreateDSL function in the Class
from Tkinter import *
import webbrowser
import datetime
import sys
import os   #to make the directory
import getpass #to get the user's name

'''
#to get the image from the Internet Sources we need to add the following
import io
import base64
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen
'''

class NessyDSL(object):
    #flags are created to monitor the user's multiple click
    __web_click_check_flag=0
    __create_dsl=0

    #Work to be done to add the Nessy Logo [pending task 1 ]
    ''''
    image_url = "https://sourcesup.renater.fr/wiki/n2s3/_media/wiki:logo_n2s3.png"
    image_byt = urlopen(image_url).read()
    image_b64 = base64.encodestring(image_byt)
    '''
    def __init__(self,master=None):
       #Create a frame inside the Master window
       master.title('NESSY DSL SIMULATION')
       master.geometry('{}x{}'.format(800, 800))
       '''
       frame= Frame(master,width=500, height=500, background="bisque")
       frame.pack()
       '''
       self.top_frame = Frame(master, bg='red', width=774, height=300, pady=3)
       self.center = Frame(master, bg='blue', width=774, height=300, padx=3, pady=3)
       self.btm_frame = Frame(master, bg='yellow', width=774, height=100, pady=3)
       self.btm_frame2 = Frame(master, bg='green', width=774, height=80, pady=3)

       # layout all of the main containers
       master.grid_rowconfigure(1, weight=1)
       master.grid_columnconfigure(0, weight=1)

       self.top_frame.grid(row=0, sticky="ew")
       self.center.grid(row=1, sticky="nsew")
       self.btm_frame.grid(row=3, sticky="ew")
       self.btm_frame2.grid(row=4, sticky="ew")

       self.center.grid_rowconfigure(0, weight=1)
       self.center.grid_columnconfigure(1, weight=1)

       self.ctr_left = Frame(self.center, bg='pink', width=300, height=190)
       self.ctr_right = Frame(self.center, bg='purple', width=600, height=190, padx=3, pady=3)

       self.ctr_left.grid(row=0, column=0, sticky="ns")  
       self.ctr_right.grid(row=0, column=1, sticky="nsew")



       #Create a menubar inside the frame
       self.menubar = Menu(self.top_frame)
       master.config(menu=self.menubar)
       submenu = Menu(self.menubar, tearoff=0)
       self.menubar.add_cascade(label="Options",menu=submenu)
       submenu.add_command(label="Quit",command=master.quit)
       submenu.add_separator()
       submenu.add_command(label="About NESSY",command=self.info)
       
       '''
       #Create a submenu now inside the menubar
       submenu = Menu(self.menubar, tearoff=0)
       #Add the menubar labels to show in the submenu

       self.menubar.add_cascade(label="File", menu=submenu)
       submenu.add_command(label="Quit",command=master.quit)
       self.menubar.add_cascade(label="About", menu=submenu)
       submenu.add_command(label="About NESSY",command=self.info)
       '''
       
       #Canvas to add arrows to the buttons after buttons
       '''
       self.C = Canvas(frame, bg="blue", height=250, width=300)
       self.filename = PhotoImage(data=__image_b64)
       self.background_label = Label(frame, image=self.filename)
       self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
       self.C.pack() 
       '''

       #The GUI Working Info
       self.helper_label= Label(self.top_frame,text='Please follow the buttons sequentially to run the DSL')
       self.helper_label.grid(row=1, sticky="nsew")


       #Button to Create DSL 
       self.Create_DSL=Button(self.ctr_left,text='Create Scala Directory on your Desktop')
       self.Create_DSL.grid(row=0,padx=20, pady=20, sticky=W)
       self.Create_DSL.bind("<Button-1>", self.CreateDSL)
      
       #To prevent user to click the button again once pressed
       ''''
       if(self.__create_dsl==1):
        self.Create_DSL.configure(state=self.DISABLED, background='cadetblue')
       else:
        self.Create_DSL.configure(state=self.ENABLED, background='cadetblue')
       '''

       #To do make the helper text fill the bottom frame 2
       #Helper Label
       self.helper=Label(self.btm_frame2, text="", width=100)
       self.helper.grid(sticky=W+E)


       #Button to Declare n2s3 dependencies
       self.Declare_N2S3=Button(self.ctr_left,text='Declare N2S3 as an SBT dependency')
       self.Declare_N2S3.grid(row=2,padx=20, pady=20, sticky=W)
       self.Declare_N2S3.bind("<Button-1>", self.N2S3_Dependency)
       self.Declare_N2S3.bind("<Enter>", self.on_enter)
       self.Declare_N2S3.bind("<Leave>", self.on_leave)



       #Button to import the classes
       self.Import_Classes=Button(self.ctr_left,text='Add the necessary imports')
       self.Import_Classes.grid(row=4,padx=20, pady=20, sticky=W)
       self.Import_Classes.bind("<Button-1>", self.Import)       


       #Button to create n2s3 object
       self.Create_Object=Button(self.ctr_left,text='Build a N2S3SimulationDSL Object')
       self.Create_Object.grid(row=6,padx=20, pady=20, sticky=W)
       self.Create_Object.bind("<Button-1>", self.create)  
       

       #Specifying the input format
       self.input_dataset_help=Label(self.ctr_left,text="Choose the type of Input Dataset")
       self.input_dataset_help.grid(row=8, padx=20, pady=20, sticky=W)
       self.choices = ['InputMnist', 'InputAER']
       self.variable = StringVar(self.ctr_right)
       self.variable.set('Click Here to Choose')
       self.w = OptionMenu( self.ctr_right, self.variable, *self.choices)
       self.w.grid(row=8, padx=20, pady=20, sticky=W)
        

    #Define helper text for each of the buttons, this one is just for Declare_N2S3

    def on_enter(self, event):
         self.helper.configure(text="This button is used to Declare N2S3 as an SBT dependency")

    def on_leave(self, enter):
         self.helper.configure(text="")



    def callback(self,event):
       __web_click_check_flag=1
       webbrowser.open_new(event.widget.cget("text"))
       #bug fix required , prevent user to click on the About multiple times to keep adding the link
            
         
 
    def info(self,master=None):
       frame= Frame( self.btm_frame2,width=100, height=100, background="bisque")
       frame.grid()
       self.theLabel=Label(frame,text="https://sourcesup.renater.fr/wiki/n2s3/start",fg="blue", cursor="hand2")
       self.theLabel.grid()
       self.theLabel.bind("<Button-1>", self.callback)

    #functions to create a Scala Directory with the Name of the folder as user's name inside scala and to create a build.sbt file
    def CreateDSL(self,event):
      __create_dSl=1
      self.username= str(getpass.getuser())
      self.desktop_path='/home/'+self.username+'/Bureau'
      self.current_now= str(datetime.datetime.now())

      #Nested Creations
      self.inside_folders= ['resource','scala','java']
      self.sub_folders= ['test','main']
      self.final_path=self.desktop_path+'/'+self.current_now+'/'
      os.mkdir(self.final_path)
      for p in self.sub_folders:
         os.mkdir(self.final_path+p)
         os.mkdir(self.final_path+p+'/resource')
         os.mkdir(self.final_path+p+'/scala')
         os.mkdir(self.final_path+p+'/java')

      #Scala file Creation
      self.scala_file_path= self.final_path+p+'/scala'
      self.name_of_file1 = self.username 
      self.complete1=os.path.join(self.scala_file_path, self.name_of_file1+".scala"  )      
      self.file1 = open(self.complete1, "w")  #This is the main file in which we are going to write

      #Build.sbt file creation
      self.name_of_file2 = "build"
      self.complete2= os.path.join(self.final_path, self.name_of_file2+".sbt")
      self.file2 = open(self.complete2, "w")
      print("Successful creation")


    
    def N2S3_Dependency(self,event):
      with open(self.complete2, "w")  as self.filehandle: 
         self.filebuffer2 = [r'name := "My Project"',r'version := "1.0"',r'scalaVersion := "2.11.6"',r'libraryDependencies ++= Seq(',
         r'   "fr.univ-lille.cristal" %% "n2s3" % "1.1.1" exclude("net.sf", "jaer_2.11"),',
         r'   "net.sf" %% "jaer" % "1.0" from "https://sourcesup.renater.fr/frs/download.php/file/5047/jaer.jar")',r')']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer2)  
      self.filehandle.close() 
      print("Successful Dependency Declaration") 

 
    def Import(self,event):
      with open(self.complete1,"w")  as self.filehandle: 
         self.filebuffer1 = [r'import fr.univ_lille.cristal.emeraude.n2s3.dsl.N2S3DSLImplicits._',
                             r'import fr.univ_lille.cristal.emeraude.n2s3.dsl.N2S3SimulationDSL']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful Classes Import") 

    def create(self,event):
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'implicit val network = N2S3SimulationDSL()']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful Created Object") 

root = Tk()
run=NessyDSL(root)
root.mainloop()
