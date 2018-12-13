from tkinter import *
import os

#create object
app = Tk()
label = Label(text='All hidden files', font =('Hack',25,'bold'))
label.pack()
listbox = Listbox(bg='#f2f2f2', fg = 'red')
listbox.pack(fill =BOTH, expand=True)


#find all hidden files in given path/directory
path = '/Users/andy/'
files = os.listdir(path)

#for each hidden files add a list to show the list of file
for f in files:
    if f.startswith('.'):
        listbox.insert(END,f)

app.mainloop()

#app.run()