from tkinter import *
import random
root=Tk()
root.title("Picnic Bag List")
root.geometry("600x600")

label_list=Label(root)
label_random=Label(root)


items=["Bottle","Phone","ID Card","Chocolates","chips","Ball","Fruits"]
label_list["text"]="things to take for picnics " + str(items)
label_list.place(relx=0.5,rely=0.3,anchor=CENTER)

def bag():
    r=random.randint(0,6)
    label_random["text"]="selected item is " + str(r)
    
    
btn=Button(root,text="pick the item",command=bag)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label_random.place(relx=0.5,rely=0.6,anchor=CENTER)















root.mainloop()