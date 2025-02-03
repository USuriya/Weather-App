from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("weather app")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        
        city=textfield.get()

        geolocator = Nominatim(user_agent="geoapiexercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        #print(result)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime('%I:%M %p')
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5c3a7f688bd46b9a76ad49fa843e274b"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry ! !")


      
#search box
search_image = PhotoImage(file= "D:/python/weather/search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)
myimage.pack(padx=5,pady=5,side= TOP)

textfield=tk.Entry(root,justify="center",width=15,font=("Georgia",25,"bold"),bg="cyan2",border=0,fg="dark orange")
textfield.place(x=250,y=25.5)

textfield.focus()

search_icon=PhotoImage(file="D:/python/weather/search_icon.png",height=50,width=50)
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="orange",command=getWeather)
myimage_icon.place(x=600,y=18)

#background
root.config(bg="cornflower blue")

#logo
logo_image=PhotoImage(file="D:/python/weather/logo.png")
logo=Label(image=logo_image)
logo.place(x=300,y=100)

#BOTTOM BOX
frame_image=PhotoImage(file="D:/python/weather/box.png")
frame=Label(image=frame_image)
frame.pack(padx=5,pady=5,side=BOTTOM)

#TIME
name=Label(root,font=("arial",18,"bold italic"),bg="cornflower blue")
name.place(x=40,y=250)
clock=Label(root,font=("algerian",43,"bold "),fg="red",bg="cornflower blue")
clock.place(x=30,y=170)

#LABEL
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="dark orange",bg="#1ab5ef")
label1.place(x=120,y=400)

label1=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="dark orange",bg="#1ab5ef")
label1.place(x=250,y=400)

label1=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="dark orange",bg="#1ab5ef")
label1.place(x=430,y=400)

label1=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="dark orange",bg="#1ab5ef")
label1.place(x=650,y=400)

t=Label(font=("algerian",70,"bold"),fg="red",bg="cornflower blue")
t.place(x=650,y=150)

c=Label(font=("arial",18,"bold italic"),bg="cornflower blue")
c.place(x=580,y=250)

w=Label(text="...",font=("arial",17,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",17,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font=("arial",17,"bold"),bg="#1ab5ef")
d.place(x=424,y=430)

p=Label(text="...",font=("arial",17,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()
