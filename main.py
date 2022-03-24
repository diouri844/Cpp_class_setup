from Module import *
from tkinter import *
from PIL import Image, ImageTk



class Class_Editeur():
    def __init__(self):
        self.window = Tk()
        self.bg_color = "white"
        self.fg_color = "#3479D7"
        self.fg_secondary = "black"
        self.bg_secondary = "#eee"
        self.class_name = StringVar()
        self.class_path = StringVar()
        self.attr_name = StringVar()
        self.window.geometry("400x550")
        self.window.config(background=self.bg_color)
        self.window.resizable(0, 0)
        self.window.iconbitmap("Images/icons8-c-48.ico")
        self.window.title(' Editeur des classes Cpp v1')
        self.window.label_titel = Label(self.window, text="Inisialisé votre class ici ! ",
            font="Bite-Chocolate 18 underline", bd=0, fg=self.fg_color, bg=self.bg_color)
        # class setup outils :
        my_image = Image.open('Images/img_textBox0.png')
        my_icon = ImageTk.PhotoImage(my_image)
        self.window.canva_class_name = Label(self.window, image=my_icon, height=40, width=238, bg=self.bg_color)
        self.window.canva_class_name.image = my_icon
        self.window.label_class_name = Label(self.window, text="Nom ", bd=0, fg=self.fg_color, bg=self.bg_secondary,
            font="Bite-Chocolate 11")
        self.window.entry_class_name = Entry(self.window, highlightthickness=0, 
            bd=0, bg=self.bg_secondary, textvariable=self.class_name, fg=self.fg_secondary)
        
        self.window.canva_class_path = Label(self.window, image=my_icon, height=40, width=238, bg=self.bg_color)
        self.window.canva_class_path.image = my_icon
        self.window.label_class_path = Label(self.window, text="Emplacement ", bd=0, fg=self.fg_color, bg=self.bg_secondary,
            font="Bite-Chocolate 11")
        self.window.entry_class_path = Entry(self.window, highlightthickness=0, 
            bd=0, bg=self.bg_secondary, textvariable=self.class_path, fg=self.fg_secondary)
        self.window.btn_select_class_folder = Button(self.window,
            bg=self.bg_color, fg=self.fg_color, bd=0, text="Ouvrir", font="Bite-Chocolate 8 underline",
            command=lambda:get_output_folder(self))
        self.window.btn_next_step = Button(self.window,
            bg=self.bg_secondary, fg=self.fg_color,bd=0,text="Continuer", font="Bite-Chocolate 10 underline",
            command=lambda:next_step(self))
        # entry focus : 
        self.window.entry_class_name.focus()
        # add to window :
        self.window.label_titel.place(relx=0.2, rely=0.01)
        self.window.label_class_name.place(relx=0.22, rely=0.21)
        self.window.canva_class_name.place(relx=0.2, rely=0.2)
        self.window.entry_class_name.place(relx=0.32, rely=0.22, width = 180.0, height=15)

        
        self.window.label_class_path.place(relx=0.22, rely=0.41)
        self.window.canva_class_path.place(relx=0.2, rely=0.4)
        self.window.entry_class_path.place(relx=0.47, rely=0.42, width = 100.0, height=15)
        self.window.btn_select_class_folder.place(relx=0.67, rely=0.48)

        self.window.btn_next_step.place(relx=0.75, rely=0.75)

    def Run(self):
        self.window.mainloop()
        return

if __name__ == "__main__":
    my_window = Class_Editeur()
    my_window.Run()