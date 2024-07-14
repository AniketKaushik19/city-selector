import tkinter as tk
from tkinter import ttk
from tkinter import *

def on_select(event):
    selected_item = monthchoosen.get()
    label.config(text="Selected State: " + selected_item)
    label1.config(text="Country: " + c[selected_item])
    
c={
    'New York': 'United States',
    'London': 'United Kingdom',
    'Tokyo': 'Japan',
    'Paris': 'France',
    'Sydney': 'Australia',
    "Andhra Pradesh": "India",
    "Arunachal Pradesh": "India",
    "Assam": "India",
    "Bihar": "India",
    "Chhattisgarh": "India",
    "Goa": "India",
    "Gujarat": "India",
    "Haryana": "India",
    "Himachal Pradesh": "India",
    "Jammu and Kashmir": "India",
    "Jharkhand": "India",
    "Karnataka": "India",
    "Kerala": "India",
    "Madhya Pradesh": "India",
    "Maharashtra": "India",
    "Manipur": "India",
    "Meghalaya": "India",
    "Mizoram": "India",
    "Nagaland": "India",
    "Odisha": "India",
    "Punjab": "India",
    "Rajasthan": "India",
    "Sikkim": "India",
    "Tamil Nadu": "India",
    "Telangana": "India",
    "Tripura": "India",
    "Uttar Pradesh": "India",
    "Uttarakhand": "India",
    "West Bengal": "India"
}

# Create a tkinter window
window = tk.Tk()
window.title('Aniket project')
window.geometry('500x250')
window.configure(bg="#71d6e3")
# Create a label and combobox
ttk.Label(window, text="Select the State :", font=("Times New Roman", 12)).place(relx=0.2, rely=0.3,anchor=CENTER)
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width=27, textvariable=n)
monthchoosen['values'] = list(c.keys())
#s=monthchoosen.get()
#print(s)
label = tk.Label(window, text="Selected Item: ",fg="green")
label.place(relx=0.5, rely=0.5,anchor=CENTER)
label1 = tk.Label(window, text="Country: ",fg="green")
label1.place(relx=0.5, rely=0.6,anchor=CENTER)
monthchoosen.bind("<<ComboboxSelected>>", on_select)
#ttk.Label(window, text="India", font=("Times New Roman", 10)).grid(column=0, row=6, padx=10, pady=25)
monthchoosen.place(relx=0.5, rely=0.3,anchor=CENTER)
