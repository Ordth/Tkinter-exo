from tkinter import *
input_name =""
input_age = ""

def write_name():
    input_name =value.get()
    label_name.config(text = f"Nom : {input_name}")

def write_age():
    input_age = value.get()
    label_age.config(text = f"Age : {input_age}")

fenetre = Tk()

##############################

# intvar_age = IntVar()
# strvar_name = StringVar()

########### Nom ##############
label_name = Label(fenetre, text=f"Nom : {input_name}")
label_name.pack()


########## Age ################
label_age = Label(fenetre, text=f"Age : {input_age}")
label_age.pack()

# def change_age():
    
########## Boutons ############

bouton_name=Button(fenetre, text="Nom", command = write_name)
bouton_name.pack()

bouton_age=Button(fenetre, text="Age", command = write_age)
bouton_age.pack()

########## input #########

value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()


fenetre.mainloop()

