from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Test")
        self.geometry("400x400")
        self.configure(bg='white')
    
        self.button = Button(self, text="Click me", command=self.action)
        self.button.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.75, relheight=0.5)

    def action(self):
        self.button.config(text="Nice!")


if __name__ == "__main__":
  app = App()
  app.mainloop()