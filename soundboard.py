#!python3
import playsound
import tkinter as tk

win = tk.Tk()
win.geometry("680x320")
win.title("SoundBoard")
but1 = tk.Button(win,text="Goat",font="5",height=8,width=24)
but1.grid(column=0,row=0)

but2= tk.Button(win,text="Ben",font="5",height=8,width=24)
but2.grid(column=1,row=0)

but3 = tk.Button(win,text="OpenNaDoor",font="5",height=8,width=24)
but3.grid(column=2,row=0)

but4 = tk.Button(win,text="FortniteW",font="5",height=8,width=24)
but4.grid(column=0,row=1)

but5 = tk.Button(win,text="Ahh",font="5",height=8,width=24)
but5.grid(column=1,row=1)

but6 = tk.Button(win,text="FortDie",font="5",height=8,width=24)
but6.grid(column=2,row=1)
def Goat(e):
        playsound.playsound("thegoat.mp3",block=False)
def Ben(e):
     playsound.playsound("ben.mp3",block=False)
def Opendoor(e):
     playsound.playsound("opennadoor.mp3",block=False)
def FortniteW(e):
     playsound.playsound("fortnitew.mp3",block=False)
def Ahh(e):
     playsound.playsound("ahh.mp3",block=False)
def Fortdie(e):
     playsound.playsound("fortdie.mp3",block=False)
but1.bind("<Button-1>",Goat)
but2.bind("<Button-1>",Ben)
but3.bind("<Button-1>",Opendoor)
but4.bind("<Button-1>",FortniteW)
but5.bind("<Button-1>",Ahh)
but6.bind("<Button-1>",Fortdie)
win.mainloop()
