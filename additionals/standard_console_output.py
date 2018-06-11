#https://gist.githubusercontent.com/RascalTwo/55ea5480af4a7b031e49/raw/d84acf96901c011f054b1757442d8e0929a57cc0/st_to_tkinter.py
import Tkinter
import sys

class StdRedirector():
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.config(state=Tkinter.NORMAL)
        self.text_space.insert("end", string)
        self.text_space.see("end")
        self.text_space.config(state=Tkinter.DISABLED)

class CoreGUI():
    def __init__(self, parent):
        text_box = Tkinter.Text(parent, state=Tkinter.DISABLED)
        text_box.pack()

        sys.stdout = StdRedirector(text_box)
        sys.stderr = StdRedirector(text_box)

        output_button = Tkinter.Button(parent, text="Output", command=self.main)
        output_button.pack()

    def main(self):
        print "Std Output"
        raise ValueError("Std Error")

root = Tkinter.Tk()
CoreGUI(root)
root.mainloop()

