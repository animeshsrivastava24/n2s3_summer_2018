
       self.neuralbutton =Button(self.ctr_left, text ="Click to create the "+ str(self.neural_layer_flag) + " layer")
       self.neuralbutton.grid(row=7,padx=20, pady=10, sticky=W)
       self.neuralbutton.bind("<Button-1>", self.neural_network_window)  


    def neural_network_window(self,event): # new window definition
        self.newwin= Toplevel(self.ctr_left)
        self.display = Label(self.newwin, text="Humm, see a new window !")
        self.display.grid() 
        self.neural_layer_flag+=1
    
