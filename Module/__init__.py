import os
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def clear_window_widget(root):
    root.window.label_titel.destroy()
    root.window.canva_class_name.destroy()
    root.window.label_class_name.destroy()
    root.window.entry_class_name.destroy()
    root.window.label_class_path.destroy()
    root.window.canva_class_path.destroy()
    root.window.entry_class_path.destroy()
    root.window.btn_select_class_folder.destroy()
    root.window.btn_next_step.destroy()
    return

def add_new_attr(root):
    root.window.titel = Label(root.window, text="Ajouté attribute ", font="Bite-Chocolate 18 underline",
                            bg=root.bg_color, fg=root.fg_color, bd=0)
    my_image = Image.open('Images/img_textBox0.png')
    my_icon = ImageTk.PhotoImage(my_image)
    root.window.canva_class_name = Label(root.window, image=my_icon, height=40, width=238, bg=root.bg_color)
    root.window.canva_class_name.image = my_icon
    root.window.label_class_name = Label(root.window, text="Nom ", bd=0, fg=root.fg_color, bg=root.bg_secondary,
            font="Bite-Chocolate 11")
    root.window.entry_class_name = Entry(root.window, highlightthickness=0, 
            bd=0, bg=root.bg_secondary, textvariable=root.attr_name, fg=root.fg_secondary)
    #default focus :
    root.window.entry_class_name.focus()
    # add to window : 
    root.window.titel.place(relx=0.35, rely=0.1)
    root.window.label_class_name.place(relx=0.37, rely=0.21)
    root.window.canva_class_name.place(relx=0.35, rely=0.2)
    root.window.entry_class_name.place(relx=0.385, rely=0.24, width = 180.0, height=17)

    return



def next_step(root):
    if not root.class_name.get() == "" and not root.class_path.get() == "":
        clear_window_widget(root)
        # create header file : 
        try:
            my_heder_file = open(root.class_path.get()+"/"+root.class_name.get()+".hpp", mode="w")
            # create body of prototype file : 
            my_cpp_file = open(root.class_path.get()+"/"+root.class_name.get()+".cpp", mode="w")
        except Exception as e:
            messagebox.showerror("Erreur",e)
        finally:
            my_heder_file.close()
            my_cpp_file.close()
        # seconde window setup :
        root.window.geometry("1200x550")
        # add  a side frame : 
        root.window.side_frame = Frame(root.window, bg=root.bg_secondary, width=250,height=550)
        # add liste items : 
        my_image = Image.open('Images/icons8-ajouter-30.png')
        my_icon = ImageTk.PhotoImage(my_image)
        # add a canva btn : 
        root.window.canva_attr_add = Label(root.window.side_frame, image=my_icon, height=30, width=30, bg=root.bg_secondary)
        root.window.canva_attr_add.image = my_icon
        root.window.label_attr_add = Button(root.window.side_frame, text="Ajouter attribute ", font="Bite-Chocolate 12",
            bg=root.bg_secondary, fg=root.fg_color, bd=0, command=lambda:add_new_attr(root))
        root.window.canva_mth_add = Label(root.window.side_frame, image=my_icon, height=30, width=30, bg=root.bg_secondary)
        root.window.canva_mth_add.image = my_icon
        root.window.label_mth_add = Button(root.window.side_frame, text="Ajouter methode ", font="Bite-Chocolate 12",
            bg=root.bg_secondary, fg=root.fg_color, bd=0)

        # add to window : 
        root.window.side_frame.place(relx=0.0, rely=0.0)
        root.window.canva_attr_add.place(relx=0.0, rely=0.07)
        root.window.label_attr_add.place(relx=0.15, rely=0.08)
        root.window.canva_mth_add.place(relx=0.0, rely=0.17)
        root.window.label_mth_add.place(relx=0.15, rely=0.18)
    else:
        messagebox.showerror("Erreur"," Nom class ou chemin class non disponible")
        root.class_path.set('')
        root.class_name.set('')
        root.window.entry_class_name.focus()
    return


def get_output_folder(root):
    init_path = os.path.expanduser("~")
    root.window.output_folder = filedialog.askdirectory(initialdir=init_path, title="Choisir un dossier ", 
    mustexist = True, parent=root.window)
    root.class_path.set(root.window.output_folder)
    return 

