self.x = Button(self.dialog, text="Download",
                state=NORMAL, command=self.download).pack(side=LEFT)
#in the function call
self.x.config(state="disabled")
