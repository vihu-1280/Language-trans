from tkinter import*
root = Tk()
root.title("Language translator")
root.geometry("500x300")
label_score = Label(root, text= "Language translator" , font=("Arial",20))
label_score.place(relx=0.5 , rely=0.25, anchor=CENTER)
label_color = Label(root, text="" , font=("Arial",25))
label_color.place(relx=0.5 , rely=0.19, anchor=CENTER)
color_name = Entry(root, text="")
color_name.insert(0, "Enter text to translate")
color_name.place(relx=0.5,rely=0.57, anchor=CENTER)
root.mainloop()