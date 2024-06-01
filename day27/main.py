from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
#Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=200)

# my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=150, pady=300)
#Button

def button_clicked():
    # my_label["text"] = "Button Got Clicked"
    new_text = input.get()
    my_label["text"] = new_text


#Entry

input = Entry(width=10)
# input.pack()
contents = input.get()
input.grid(column=3, row=3)
button = Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

#Second Button
button_2 = Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)
window.mainloop()