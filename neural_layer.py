#Created by Animesh Srivastava  on 12 June 2018
from Tkinter import *
def Neural_Layer(neuralmaster):
     #Create a frame inside the Master window
     neuralmaster.title('NESSY DSL SIMULATION')
     neuralmaster.geometry('{}x{}'.format(800, 800))
     top_frame = Frame(neuralmaster, bg='yellow', width=800, height=800)
     top_frame.grid(row=0, sticky="ew")
def main():
    pass

#if we want to import this file and prevent it running there automatically just put the function call in the statements below
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
       root = Tk()
       run=Neural_Layer(root)
       root.mainloop()


