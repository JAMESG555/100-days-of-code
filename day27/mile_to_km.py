from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def converter():
    miles = entry.get()
    km = float(miles) * 1.60934
    output_label["text"] = km



#Equal to title
equal_to_label = Label(text="is equal to", font=("Arial", 12))
equal_to_label.grid(column=0, row=1)
#Input
entry = Entry(width=10, )
entry.grid(column=1, row=0)
#Output Label
output_label = Label(text="0", font=("Arial", 12))
output_label.grid(column=1, row=1)
#Calculate Button
calc_button = Button(text="Calculate", command=converter)
calc_button.grid(column=1, row=2)
#Miles Label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)
#KM Label
km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)



window.mainloop()