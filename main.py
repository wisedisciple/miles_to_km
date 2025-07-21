import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(100,100)
window.config(padx=20, pady=20)

miles_converted = 0

#Label
my_label = tkinter.Label(text="is equal to ", font= ("Arial", 24))
my_label.grid(row=1, column=0)

converted_label = tkinter.Label(text="0", font= ("Arial", 24))
converted_label.grid(row=1, column=1)

other_label = tkinter.Label(text="Miles", font= ("Arial", 24))
other_label.grid(row=0, column=3)

km_label = tkinter.Label(text="Km", font= ("Arial", 24))
km_label.grid(row=1, column=3)

def miles_to_km():
    miles = int(input.get())
    miles_converted = (miles * 1.609344)
    converted_label.config(text=f"{round(miles_converted, 2)}", font= ("Arial", 24))

#Button
button = tkinter.Button(text= "Calculate", command=miles_to_km)
button.grid(row=2, column=1)

#Entry
input = tkinter.Entry(width=12)
input.grid(row=0, column=1)

window.mainloop()

