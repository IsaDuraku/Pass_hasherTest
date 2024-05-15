from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$tEbXGoELKTQyV/rnKTylyOXDmtxvwOGo6tON1vi6Nc0ZNRMmA/4qm'
    password = bytes(password, encoding='utf-8')

    if bcrypt.checkpw(password, hash):
        validation_message.set("Login successful")
    else:
        validation_message.set("Invalid Password")

root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

validation_message = StringVar()
validation_label = Label(root, textvariable=validation_message)
validation_label.pack()

button = Button(text="Validate", command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()