from tkinter import*
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv



root =Tk()
root.geometry("600x700+400+80")
root.resizable(False,False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")
from tkinter import*
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv



root =Tk()
root.geometry("600x700+400+80")
root.resizable(False,False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

def Record():
    freq= 44100
    dur= int(duration.grt())
    recording= sound.rec(dur*freq,
                            samplerate= freq, channels=2)
    sound.wait()
    write("recording.wav", freq, recording)



# #icon
# image_icon=PhotoImage(file="image.png")
# root.iconphoto(False, image_icon)


#name
Label(text="Voice Recorder", font="arial 30 bold" , background= "#4a4a4a", fg= "white").pack()

#entry box
duration= StringVar()
entry=Entry(root,textvariable= duration, font ="arial 30 ", width =15).pack(pady=10)
Label(text="Enter time in seconds", font ="arial 15" , background ="#4a4a4a", fg="white").pack()


#button 
record= Button(root, font="arial 20", text ="Record", bg= "#111111", fg ="white", border =0, command= Record).pack(pady=30)
root.mainloop ()
def Record():
    freq= 44100
    dur= int(duration.get())
    recording= sound.rec(dur*freq,
                            samplerate= freq, channels=2)
    sound.wait()
    write("recording.wav", freq, recording)



# #icon
# image_icon=PhotoImage(file="image.png")
# root.iconphoto(False, image_icon)


#name
Label(text="Voice Recorder", font="arial 30 bold" , background= "#4a4a4a", fg= "white").pack()

#entry box
duration= StringVar()
entry=Entry(root,textvariable= duration, font ="arial 30 ", width =15).pack(pady=10)
Label(text="Enter time in seconds", font ="arial 15" , background ="#4a4a4a", fg="white").pack()


#button 
record= Button(root, font="arial 20", text ="Record", bg= "#111111", fg ="white", border =0, command= Record).pack(pady=30)
root.mainloop ()