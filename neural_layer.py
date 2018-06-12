#Created by Animesh Srivastava  on 12 June 2018
from Tkinter import *
import work #to get the folder path to be able to create the csv file to save the neural layer information
class Neural(object):
    def __init__(self,neuralmaster):
       #Create a frame inside the Master window
       neuralmaster.title('NESSY DSL SIMULATION')
       neuralmaster.geometry('{}x{}'.format(800, 100))
       top_frame = Frame(neuralmaster, bg='white', width=800, height=100)
       top_frame.grid(row=0, sticky="ew")
       
       self.menubar = Menu(top_frame)
       neuralmaster.config(menu=self.menubar)
       submenu = Menu(self.menubar, tearoff=0)
       self.menubar.add_cascade(label="Options",menu=submenu)
       submenu.add_command(label="Quit",command=neuralmaster.quit)
       #Neural group 1
       #To type the name of the neuron group,size,modeling type,threshold values
       #Just for seeing we need to store it too
       self.neuron_group1_name=Label(top_frame,text="Enter name of your first neuron group" ,fg="red")
       self.neuron_group1_name.grid(row=0, padx=20, sticky=W)
       self.neuron_group1_name_entry=Entry(top_frame)
       self.neuron_group1_name_entry.grid(row=0,column=1, padx=20, sticky=W)
       self.neuron_group1_size=Label(top_frame,text="Enter the size of your first neuron group",fg="red")       
       self.neuron_group1_size.grid(row=1, padx=20, sticky=W)
       self.neuron_group1_size_entry=Spinbox(top_frame,from_=10,to=100)
       self.neuron_group1_size_entry.grid(row=1,column=1, padx=20, sticky=W)
      
       self.neuron_group1_threshold=Label(top_frame,text="Enter the threshold value unit=mV ",fg="red")
       self.neuron_group1_threshold.grid(row=2, padx=20, sticky=W)
       self.neuron_group1_threshold_entry=Spinbox(top_frame,from_=10,to=100)
       self.neuron_group1_threshold_entry.grid(row=2,column=1, padx=20, sticky=W)
       
       #bind the creation function to the button and drop down for modeling options [pending work]
       self.neuron_group1_modeling=Label(top_frame,text="Select the Modeling Option" ,fg="red")
       self.neuron_group1_modeling.grid(row=3,column=0, padx=20, sticky=W)
       self.neuron_group1_final=Button(top_frame,text="Create the first neural network layer",fg="blue")
       self.neuron_group1_final.grid(row=3,column=2, padx=20, sticky=W)
       self.neuron_group1_final.bind("<Button-1>", self.save_layer_csv)

    def save_layer_csv(self,event):
       print("Successfully created the first layer")
       print('network hasNeunronGroup '+ '"'+self.neuron_group1_name_entry.get()+'"' +' ofSize '+self.neuron_group1_size_entry.get()+'modeling LIF')
 

def main():
    pass

#if we want to import this file and prevent it running there automatically just put the function call in the statements below
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
       root = Tk()
       run=Neural(root)
       root.mainloop()


