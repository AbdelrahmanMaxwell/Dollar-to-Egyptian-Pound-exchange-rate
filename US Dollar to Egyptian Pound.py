from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import urllib
from urllib import request
from datetime import datetime

main_window = Tk()
main_window.title("US Dollar to Egyptian Pound")
main_window.geometry("580x250+400+400")
main_window.resizable(height=False, width=False)
main_window.config(bg="#0a146e")

global prevoius
prevoius = False

# Grab bitcoin price
def update_price():
    global prevoius

    page = urllib.request.urlopen("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EGP").read()
    html = BeautifulSoup(page, "html.parser")
    price_large = html.find(class_="result__BigRate-sc-1bsijpp-1 iGrAod")
    print(price_large)
    # Convert price_large to string
    price_large1 = str(price_large)
    # Get the price from the class
    price_large2 = price_large1[47:52]
    print(price_large2)

    # Define change
    current_price = price_large2
    current_price = current_price.replace(",", "")
    if prevoius:
        if float(prevoius) > float(current_price):
            lable_currentPrice.config(text=f"Price -{round(float(prevoius) - float(current_price), 2)}", fg="red")
        elif float(prevoius) == float(current_price):
            lable_currentPrice.config(text="- Price unchanged -", fg="grey")
        else:
            lable_currentPrice.config(text=f"Price +{round(float(current_price) - float(prevoius), 2)}", fg="green")
    else:
        prevoius = current_price
        lable_currentPrice.config(text="- Price unchanged -")

    # Update bitocin price
    lable_price.config(text=f"{price_large2} EGP")

    # Update price every 60 seconds
    main_window.after(60000, update_price)

def update_time():
    # Current time
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")

    # Update time in status bar
    status_bar.config(text=f"Last Updated  {current_time} ")
    # Update time every 60 seconds
    main_window.after(60000, update_time)

# Create an image background
back_image = PhotoImage(file="bilder/back.png")
# Create canvases
canvas1 = Canvas(main_window, bg="black", borderwidth=0, highlightthickness=0, width=1215, height=700)
canvas1.create_image(0, 0, image=back_image, anchor=NW)

bitcoin_logo = PhotoImage(file="bilder/dollar.png")    # to make it work with .exe
label_bitcoin = Label(main_window, image=bitcoin_logo, bd=0, bg="#0a146e")

# Current time
now = datetime.now()
current_time = now.strftime("%I:%M:%S")

# Network connection
try:
    page = urllib.request.urlopen("https://www.google.com").read()
except:
    messagebox.showerror("No Internet Connection", "Check your internet connection and try again.")
    quit()

# Create lables
lable_price = Label(main_window, text=" Try ", font=("Hind", 45), bg="#0a146e", fg="white", bd=0)

lable_currentPrice = Label(main_window, text="it's Ok", font=("Hind", 8), bg="#0a146e", fg="white", bd=0)

# Create a status bar
status_bar = Label(main_window, text=f"Last Updated  {current_time} ", bd=0, anchor=E, bg="#0a146e", fg="white")

update_price()
update_time()

# Place
#canvas1.place(x=0, y=0)
label_bitcoin.place(x=80, y=40)
lable_price.place(x=280, y=75)
lable_currentPrice.place(x=350, y=160)
status_bar.place(x=455, y=230)

main_window.mainloop()
