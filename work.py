#Created by Animesh Srivastava  
#Information replace 'Bureau' with 'Desktop' in case you are an English user in the CreateDSL function in the Class
from Tkinter import *
import webbrowser
import datetime
import sys
import os   #to make the directory
import getpass #to get the user's name

#to get the image from the Internet Sources
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


flag_neural_layer_name=1
#the class below is for the standard output and input console work, no need to disturb it
class StdRedirector():
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.config(state=NORMAL)
        self.text_space.insert("end", string)
        self.text_space.see("end")
        self.text_space.config(state=DISABLED)

#our main class
class NessyDSL(object):
    print("Welcome")
    global flag_neural_layer_name
    def __init__(self,master):
       #Create a frame inside the Master window
       master.title('NESSY DSL SIMULATION')
       master.geometry('{}x{}'.format(800, 800))
       self.top_frame = Frame(master, bg='white', width=774, height=300, pady=3,relief="sunken")
       self.center = Frame(master, bg='blue', width=774, height=600, padx=3, pady=3,relief="sunken")
       self.btm_frame = Frame(master, bg='medium orchid', width=774, height=100, pady=3,relief="sunken")
       self.btm_frame2 = Frame(master, bg='seashell', width=774, height=80, pady=3,relief="sunken")

       # layout all of the main containers
       master.grid_rowconfigure(1, weight=1)
       master.grid_columnconfigure(0, weight=1)

       self.top_frame.grid(row=0, sticky="ew")
       self.center.grid(row=1, sticky="nsew")
       self.btm_frame.grid(row=3, sticky="ew")
       self.btm_frame2.grid(row=4, sticky="ew")

       self.center.grid_rowconfigure(0, weight=1)
       self.center.grid_columnconfigure(1, weight=1)

       self.ctr_left = Frame(self.center, bg='pale turquoise', width=300, height=190,relief="sunken")
       self.ctr_right = Frame(self.center, bg='medium turquoise', width=600, height=190, padx=3, pady=3,relief="sunken")

       self.ctr_left.grid(row=0, column=0, sticky="ns")  
       self.ctr_right.grid(row=0, column=1, sticky="nsew")
       self.neural_layer_flag=1

       #Create a menubar inside the frame
       self.menubar = Menu(self.top_frame)
       master.config(menu=self.menubar)
       submenu = Menu(self.menubar, tearoff=0)
       self.menubar.add_cascade(label="Options",menu=submenu)
       submenu.add_command(label="Quit",command=master.quit)
       submenu.add_command(label="About NESSY",command=self.info)
       
  
       #The GUI Working Info
       self.helper_label= Label(self.top_frame,text='Please follow the buttons sequentially to run the DSL')
       self.helper_label.grid(row=1, sticky="nsew")

       #Button to Create DSL 
       try:
        self.Create_DSL=Button(self.ctr_left,text='Create Scala Directory on your Desktop',state=NORMAL)
        self.Create_DSL.grid(row=0,padx=20, pady=10, sticky=W)
        self.Create_DSL.bind("<Button-1>", self.CreateDSL)
        self.image_url = "https://sourcesup.renater.fr/wiki/n2s3/_media/wiki:logo_n2s3.png"
        self.image_byt = urlopen(self.image_url).read()
        self.image_b64 = base64.encodestring(self.image_byt)
        self.photo = PhotoImage(data=self.image_b64)
        self.photo = self.photo.zoom(56) #with 250, I ended up running out of memory
        self.photo = self.photo.subsample(30)
        self.cv = Canvas(self.btm_frame,bg='white')
        self.cv.grid()
        self.cv.create_image(10, 10, image=self.photo, anchor='nw')
       except:
        print("Need an active internet connection to download the n2s3 picture")
       



       #To do make the helper text fill the bottom frame 2
       #Helper Label
       self.helper=Label(self.btm_frame2, text="", width=100)
       self.helper.grid(sticky=W+E)
       self.helper.grid_columnconfigure(0, weight=1)



       #stdout and stderr to Tkinter GUI example.
       #https://gist.github.com/RascalTwo/55ea5480af4a7b031e49 
       text_box = Text(self.ctr_right,width=100, height=100, state=DISABLED)
       text_box.grid(row=0,column=2,sticky=W+E+N+S)
       sys.stdout = StdRedirector(text_box)
       sys.stderr = StdRedirector(text_box)
  
       #Button to Declare n2s3 dependencies
       self.Declare_N2S3=Button(self.ctr_left,text='Declare N2S3 as an SBT dependency',state=NORMAL)
       self.Declare_N2S3.grid(row=2,padx=20, pady=10, sticky=W)
       self.Declare_N2S3.bind("<Button-1>", self.N2S3_Dependency)
       self.Declare_N2S3.bind("<Enter>", self.on_enter)
       self.Declare_N2S3.bind("<Leave>", self.on_leave)
      

       #Button to import the classes
       self.Import_Classes=Button(self.ctr_left,text='Add the necessary imports',state=NORMAL)
       self.Import_Classes.grid(row=4,padx=20, pady=10, sticky=W)
       self.Import_Classes.bind("<Button-1>", self.Import)       

      



       #Button to create n2s3 object
       self.Create_Object=Button(self.ctr_left,text='Build a N2S3SimulationDSL Object',state=NORMAL)
       self.Create_Object.grid(row=6,padx=20, pady=10, sticky=W)
       self.Create_Object.bind("<Button-1>", self.create)  
       
       #Add the things mentioned on the simplified syntax page
       #remember this is just added to complete the work on 13 june to begin with the scala part
       '''network hasInput InputMnist.Entry >> SampleToSpikeTrainConverter[Float, InputSample2D[Float]](0, 23, 150 MilliSecond, 350 MilliSecond) >> N2S3Entry
          network hasInputNeuronGroup "input"'''
       self.btn1 = StringVar() #Choose the size of group 1

       self.btn3 = StringVar() #Choose the modeling for the neurons of group_1

       self.btn5 = StringVar() #grp 1
   
       self.btn7 = StringVar() #grp 2

       self.btn9=  StringVar() #grp 1 and grp 2

       self.btn11=  StringVar() #grp1 and itself
 
       self.btn13=  StringVar() #grp 2 and itself
  
       self.btn15=  StringVar()  #input and grp 1
       

       #the code to add the input line
       self.network_input=Label(self.ctr_left,text="Choose the input method with default parameters" ,fg="red")
       self.network_input.grid(row=7, padx=20, sticky=W)
       self.opt1=Radiobutton(self.ctr_left,text="MNIST",value = "InputMnist",variable = self.btn1).grid(row=7, column=1, sticky=W)
       self.opt2=Radiobutton(self.ctr_left,text="AER",value = "InputAer",variable =self.btn1).grid(row=7, column=2, sticky=W)
       self.button_network_input=Button(self.ctr_left,text='Save the input',fg='green',state=NORMAL)
       self.button_network_input.grid(row=8,column=2,padx=20, sticky=W)
       self.button_network_input.bind("<Button-1>", self.Button_network_input)  
       

       self.group_1_size=Label(self.ctr_left,text="Choose the size of group 1" ,fg="red")
       self.group_1_size.grid(row=9, padx=20,pady=20, sticky=W)

       self.group_1_size_value=Spinbox(self.ctr_left, from_=10, to=100)
       self.group_1_size_value.grid(row=9,column=1, padx=20, sticky=W)
 
       #the code to add the group1, it's size, modeling type, threshold values
       #network hasNeunronGroup "group_1" ofSize 28 modeling LIF
       #"group_1" withParameters (MembranePotentialThreshold -> 35.millivolts) 

       self.group_1_size=Label(self.ctr_left,text="Choose the size of group_1" ,fg="red")
       self.group_1_size.grid(row=9, padx=20,pady=20, sticky=W)

       self.group_1_size_value=Spinbox(self.ctr_left, from_=10, to=100)
       self.group_1_size_value.grid(row=9,column=1, padx=20, sticky=W)
 

       self.group_1_modeling=Label(self.ctr_left,text="Choose the modeling for the neurons of group_1" ,fg="blue")
       self.group_1_modeling.grid(row=10, padx=20, sticky=W)
       self.grp1_opt1=Radiobutton(self.ctr_left,text="LIF",value = "LIF",variable = self.btn3).grid(row=10, column=1, sticky=W)
       self.grp1_opt2=Radiobutton(self.ctr_left,text="SRM",value = "SRM",variable =self.btn3).grid(row=10, column=2, sticky=W)
       self.grp1_opt3=Radiobutton(self.ctr_left,text="Izhikevich",value = "Izhikevich",variable =self.btn3).grid(row=10, column=3, sticky=W)
       

       
       self.group_1_MembranePotentialThreshold=Label(self.ctr_left,text="Choose the MembranePotentialThreshold for group_1 in mV" ,fg="blue")
       self.group_1_MembranePotentialThreshold.grid(row=11, padx=20, sticky=W)

       self.group_1_MembranePotentialThreshold_value=Spinbox(self.ctr_left, from_=10, to=100)
       self.group_1_MembranePotentialThreshold_value.grid(row=11,column=1, padx=20, sticky=W)
 
      
       self.button_group1=Button(self.ctr_left,text='Save the group 1',fg='green',state=NORMAL)
       self.button_group1.grid(row=11,column=2,padx=20, sticky=W)
       self.button_group1.bind("<Button-1>", self.Button_group1) 

       
       #the code to add the group2, it's size, modeling type, threshold values
       #network hasNeunronGroup "group_2" ofSize 28 modeling LIF
       #"group_2" withParameters (MembranePotentialThreshold -> 35.millivolts) 
       self.group_2_size=Label(self.ctr_left,text="Choose the size of group_2" ,fg="red")
       self.group_2_size.grid(row=12, padx=20,pady=20, sticky=W)

       self.group_2_size_value=Spinbox(self.ctr_left, from_=10, to=100)
       self.group_2_size_value.grid(row=12,column=1, padx=20, sticky=W)
 

       self.group_2_modeling=Label(self.ctr_left,text="Choose the modeling for the neurons of group_2" ,fg="black")
       self.group_2_modeling.grid(row=13, padx=20,sticky=W)
       self.grp2_opt1=Radiobutton(self.ctr_left,text="LIF",value = "LIF",variable = self.btn5).grid(row=13, column=1, sticky=W)
       self.grp2_opt2=Radiobutton(self.ctr_left,text="SRM",value = "SRM",variable =self.btn5).grid(row=13, column=2, sticky=W)
       self.grp2_opt3=Radiobutton(self.ctr_left,text="Izhikevich",value = "Izhikevich",variable =self.btn5).grid(row=13, column=3, sticky=W)
       

       
       self.group_2_MembranePotentialThreshold=Label(self.ctr_left,text="Choose the MembranePotentialThreshold for group_2 in mV" ,fg="black")
       self.group_2_MembranePotentialThreshold.grid(row=14, padx=20, sticky=W)

       self.group_2_MembranePotentialThreshold_value=Spinbox(self.ctr_left, from_=10, to=100)
       self.group_2_MembranePotentialThreshold_value.grid(row=14,column=1, padx=20, sticky=W)
 
      
       self.button_group2=Button(self.ctr_left,text='Save the group_2',fg='green',state=NORMAL)
       self.button_group2.grid(row=14,column=2,padx=20, sticky=W)
       self.button_group2.bind("<Button-1>", self.Button_group2) 
    
       #the code to connect group1 and group2
       #"group_1" connectsTo "group_2" using  FullConnection withSynapse SimplifiedSTDP

       self.group_12_connection=Label(self.ctr_left,text="Choose the synapse type to connect group_1 and group_2" ,fg="black")
       self.group_12_connection.grid(row=15, padx=20,sticky=W)
       self.grp12_opt1=Radiobutton(self.ctr_left,text="Static",value = "Static",variable = self.btn7).grid(row=15, column=1, sticky=W)
       self.grp12_opt2=Radiobutton(self.ctr_left,text="Standard STDP",value = "StandardSTDP",variable =self.btn7).grid(row=15, column=2, sticky=W)
       self.grp12_opt3=Radiobutton(self.ctr_left,text="Simplified STDP",value = "SimplifiedSTDP",variable =self.btn7).grid(row=15, column=3, sticky=W)
       self.grp12_opt3=Radiobutton(self.ctr_left,text="Ternary",value = "Ternary",variable =self.btn7).grid(row=16, column=1, sticky=W)
       self.grp12_opt3=Radiobutton(self.ctr_left,text="Inhibitory",value = "Inhibitory",variable =self.btn7).grid(row=16, column=2, sticky=W)
       self.button_group12=Button(self.ctr_left,text='Connect group_1 and group_2',fg='green',state=NORMAL)
       self.button_group12.grid(row=16,column=3,padx=20, sticky=W)
       self.button_group12.bind("<Button-1>", self.Button_group12) 


       #the code to connect group1 with itself
       #"group_1" connectsTo "group_1" using FullConnection withSynapse InhibitorySynapse

       self.group_11_connection=Label(self.ctr_left,text="Choose the synapse type to connect group_1 with itself" ,fg="black")
       self.group_11_connection.grid(row=17, padx=20,sticky=W)
       self.grp11_opt1=Radiobutton(self.ctr_left,text="Static",value = "Static",variable = self.btn9).grid(row=17, column=1, sticky=W)
       self.grp11_opt2=Radiobutton(self.ctr_left,text="Standard STDP",value = "StandardSTDP",variable =self.btn9).grid(row=17, column=2, sticky=W)
       self.grp11_opt3=Radiobutton(self.ctr_left,text="Simplified STDP",value = "SimplifiedSTDP",variable =self.btn9).grid(row=17, column=3, sticky=W)
       self.grp11_opt3=Radiobutton(self.ctr_left,text="Ternary",value = "Ternary",variable =self.btn9).grid(row=18, column=1, sticky=W)
       self.grp11_opt3=Radiobutton(self.ctr_left,text="Inhibitory",value = "Inhibitory",variable =self.btn9).grid(row=18, column=2, sticky=W)
       self.button_group11=Button(self.ctr_left,text='Connect group_1 with itself',fg='green',state=NORMAL)
       self.button_group11.grid(row=18,column=3,padx=20, sticky=W)
       self.button_group11.bind("<Button-1>", self.Button_group11) 





       #the code to connect group2 with itself
       # "group_2" connectsTo "group_2" using FullConnection withSynapse InhibitorySynapse

       self.group_22_connection=Label(self.ctr_left,text="Choose the synapse type to connect group_2 with itself" ,fg="black")
       self.group_22_connection.grid(row=19, padx=20,sticky=W)
       self.grp22_opt1=Radiobutton(self.ctr_left,text="Static",value = "Static",variable = self.btn11).grid(row=19, column=1, sticky=W)
       self.grp22_opt2=Radiobutton(self.ctr_left,text="Standard STDP",value = "StandardSTDP",variable =self.btn11).grid(row=19, column=2, sticky=W)
       self.grp22_opt3=Radiobutton(self.ctr_left,text="Simplified STDP",value = "SimplifiedSTDP",variable =self.btn11).grid(row=19, column=3, sticky=W)
       self.grp22_opt3=Radiobutton(self.ctr_left,text="Ternary",value = "Ternary",variable =self.btn11).grid(row=20, column=1, sticky=W)
       self.grp22_opt3=Radiobutton(self.ctr_left,text="Inhibitory",value = "Inhibitory",variable =self.btn11).grid(row=20, column=2, sticky=W)
       self.button_group22=Button(self.ctr_left,text='Connect group_2 with itself',fg='green',state=NORMAL)
       self.button_group22.grid(row=20,column=3,padx=20, sticky=W)
       self.button_group22.bind("<Button-1>", self.Button_group22) 



 
       #the code to connect input to the group1
       #"input" connectsTo "group_1" using  FullConnection withSynapse SimplifiedSTDP
       self.group_i1_connection=Label(self.ctr_left,text="Choose the synapse type to connect input with group_1" ,fg="black")
       self.group_i1_connection.grid(row=21, padx=20,sticky=W)
       self.grpi1_opt1=Radiobutton(self.ctr_left,text="Static",value = "Static",variable = self.btn13).grid(row=21, column=1, sticky=W)
       self.grpi1_opt2=Radiobutton(self.ctr_left,text="Standard STDP",value = "StandardSTDP",variable =self.btn13).grid(row=21, column=2, sticky=W)
       self.grpi1_opt3=Radiobutton(self.ctr_left,text="Simplified STDP",value = "SimplifiedSTDP",variable =self.btn13).grid(row=21, column=3, sticky=W)
       self.grpi1_opt3=Radiobutton(self.ctr_left,text="Ternary",value = "Ternary",variable =self.btn13).grid(row=22, column=1, sticky=W)
       self.grpi1_opt3=Radiobutton(self.ctr_left,text="Inhibitory",value = "Inhibitory",variable =self.btn13).grid(row=22, column=2, sticky=W)
       self.button_groupi1=Button(self.ctr_left,text='Connect input with group_1',fg='green',state=NORMAL)
       self.button_groupi1.grid(row=22,column=3,padx=20, sticky=W)
       self.button_groupi1.bind("<Button-1>", self.Button_groupi1)       
   

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
       frame= Frame(self.btm_frame2,width=100, height=100, background="bisque")
       frame.grid()
       self.theLabel=Label(frame,text="https://sourcesup.renater.fr/wiki/n2s3/start",fg="blue", cursor="hand2")
       self.theLabel.grid()
       self.theLabel.bind("<Button-1>", self.callback)





    #functions to create a Scala Directory with the Name of the folder as user's name inside scala and to create a build.sbt file
    def CreateDSL(self,event):
     try:
      self.Create_DSL['state'] = 'disabled'
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
     except:
      print("The steps are not followed properly")


    

   
    #functions to add the dependencies to the build.sbt file 
    def N2S3_Dependency(self,event):
     try: 
      self.Declare_N2S3.config(state="disabled")
      with open(self.complete2, "w")  as self.filehandle: 
         self.filebuffer2 = [r'name := "My Project"',r'version := "1.0"',r'scalaVersion := "2.11.6"',r'libraryDependencies ++= Seq(',
         r'   "fr.univ-lille.cristal" %% "n2s3" % "1.1.1" exclude("net.sf", "jaer_2.11"),',
         r'   "net.sf" %% "jaer" % "1.0" from "https://sourcesup.renater.fr/frs/download.php/file/5047/jaer.jar")',r')']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer2)  
      self.filehandle.close() 
      print("Successful Dependency Declaration") 
     except:
      print("The steps are not followed properly")



    #functions to add the libraries to the main scala file
    def Import(self,event):
     try:
      self.Import_Classes.config(state="disabled")
      with open(self.complete1,"w")  as self.filehandle: 
         self.filebuffer1 = [r'import fr.univ_lille.cristal.emeraude.n2s3.dsl.N2S3DSLImplicits._',
                             r'import fr.univ_lille.cristal.emeraude.n2s3.dsl.N2S3SimulationDSL']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful Classes Import") 
     except:
      print("The steps are not followed properly")


    #functions to instantiate the dsl object to the main scala file
    def create(self,event):
     try:
      self.Create_Object.config(state="disabled")
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'implicit val network = N2S3SimulationDSL()']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful Created Object") 
     except:
      print("The steps are not followed properly")







    '''
    The below functions definition are for defining the layer, size, moeling and synapse connections for working
    '''

    def Button_network_input(self,event):
     try:
      self.button_network_input.config(state="disabled")
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'network hasInput '+self.btn1.get()+'.Entry >> SampleToSpikeTrainConverter[Float, InputSample2D[Float]](0, 23, 150 MilliSecond, 350 MilliSecond) >> N2S3Entry',r'network hasInputNeuronGroup "input"']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful added the input with default parameters")
      print('network hasInput '+self.btn1.get()+'.Entry >> SampleToSpikeTrainConverter[Float, InputSample2D[Float]](0, 23, 150 MilliSecond, 350 MilliSecond) >> N2S3Entry\n') 
      print(r'network hasInputNeuronGroup "input"')
     except:
      print("The steps are not followed properly")

    def Button_group1(self,event):
     try:
      self.button_group1.config(state="disabled")
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'network hasNeunronGroup "group_1" ofSize '+str(self.group_1_size_value.get())+' modeling '+self.btn3.get(),r'"group_1" withParameters (MembranePotentialThreshold -> '+str(self.group_1_MembranePotentialThreshold_value.get())+'.millivolts) ']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful added parameters of group 1")
      print('network hasNeunronGroup "group_1" ofSize '+str(self.group_1_size_value.get())+' modeling '+self.btn3.get()+'\n')
      print(r'"group_1" withParameters (MembranePotentialThreshold -> '+str(self.group_1_MembranePotentialThreshold_value.get())+'.millivolts') 
     except:
      print("The steps are not followed properly")


    def Button_group2(self,event):
     try:
      self.button_group2.config(state="disabled")
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'network hasNeunronGroup "group_2" ofSize '+str(self.group_2_size_value.get())+' modeling '+self.btn5.get(),r'"group_2" withParameters (MembranePotentialThreshold -> '+str(self.group_2_MembranePotentialThreshold_value.get())+'.millivolts) ']
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful added parameters of group 1")
      print(r'network hasNeunronGroup "group_2" ofSize '+str(self.group_2_size_value.get())+' modeling '+self.btn5.get()+'\n')
      print(r'"group_2" withParameters (MembranePotentialThreshold -> '+str(self.group_2_MembranePotentialThreshold_value.get())+'.millivolts') 
     except:
      print("The steps are not followed properly")



    def Button_group12(self,event):
     try:
      self.button_group12.config(state="disabled")
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'"group_1" connectsTo "group_2" using  FullConnection withSynapse '+self.btn7.get()]
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful connected group_1 and group_2")
      print(r'"group_1" connectsTo "group_2" using  FullConnection withSynapse '+self.btn7.get()) 
     except:
      print("The steps are not followed properly")


    def Button_group11(self,event):
     try:
      self.button_group11.config(state="disabled")
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'"group_1" connectsTo "group_1" using  FullConnection withSynapse '+self.btn9.get()]
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful connected group_1 and group_2")
      print(r'"group_1" connectsTo "group_1" using  FullConnection withSynapse '+self.btn9.get()) 
     except:
      print("The steps are not followed properly")


    def Button_group22(self,event):
     try:
      self.button_group22.config(state="disabled")
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'"group_2" connectsTo "group_2" using  FullConnection withSynapse '+self.btn11.get()]
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful connected group_1 and group_2")
      print(r'"group_2" connectsTo "group_2" using  FullConnection withSynapse '+self.btn11.get()) 
     except:
      print("The steps are not followed properly")



    def Button_groupi1(self,event):
     try:
      self.button_groupi1.config(state="disabled")
      with open(self.complete1,"a")  as self.filehandle: 
         self.filebuffer1 = [r' ',r'"input" connectsTo "group_1" using  FullConnection withSynapse '+self.btn13.get()]
         self.filehandle.writelines("%s\n" % line for line in self.filebuffer1)  
      self.filehandle.close() 
      print("Successful connected group_1 and group2")
      print(r'"input" connectsTo "group_1" using  FullConnection withSynapse '+self.btn13.get()) 
     except:
      print("The steps are not followed properly")
    '''
    The above functions definition are for defining the layer, size, moeling and synapse connections for working
    '''
#the below function is required to just avoid the script to run when connected to the internet
def main():
    pass


#if we want to import this file and prevent it running there automatically just put the function call in the statements below
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
     root = Tk()
     run=NessyDSL(root)
     root.mainloop()

