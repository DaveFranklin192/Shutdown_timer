
#importing external files, libraries and external functions for cross platform.
import tkinter as tk
import os
import time


#-----------------------------------------------------------------------------------------------------------------------------------#


# adding functions for buttons

def cancel_timer():
    os.system("shutdown -a")

def shutdown_time():
    os.system("shutdown -a")
    time.sleep(1)
    hour=entry_hour.get()
    hour_in_sec = int(hour) * 3600
    minutes=entry_minute.get()
    minutes_in_sec = int(minutes) * 60
    (secs)= int(hour_in_sec) + int(minutes_in_sec)
    os.system("shutdown -s -t {0}" .format(int(secs)))
    print("shutdown -s -t {0}" .format(int(secs)))
 

def restart():
    os.system("shutdown -a")
    time.sleep(1)
    hour=entry_hour.get()
    hour_in_sec = int(hour) * 3600
    minutes=entry_minute.get()
    minutes_in_sec = int(minutes) * 60
    (secr)= int(hour_in_sec) + int(minutes_in_sec)
    os.system("shutdown -r -t {0}" .format(int(secr)))
    print("shutdown -r -t {0}" .format(int(secr)))
    

#-----------------------------------------------------------------------------------------------------------------------------------#

#starting loop
root = tk.Tk()

#-----------------------------------------------------------------------------------------------------------------------------------#

#Window confgorations 
root.title('Shut Down')
root.iconbitmap('sleep-mode-icon.ico')
root.geometry("250x300")
root.resizable(0,0)
root.configure(bg="light gray")

#-----------------------------------------------------------------------------------------------------------------------------------#


#frames for placing widgets in
frame_main_top = tk.Frame(bg="light gray")
frame_main_top.pack(padx=5, pady=50)

frame_main = tk.Frame(bg="light gray")
frame_main.pack(padx=5, pady=5)

frame_main_bottom = tk.Frame(bg="light gray")
frame_main_bottom.pack(padx=5, pady=5)

#-----------------------------------------------------------------------------------------------------------------------------------#



#lables and input boxes for count down timer
lable_hour = tk.Label(master=frame_main_top, text="hour", bg="light gray", font=('arial', 12))
lable_hour.grid(column=0, row=0)

lable_minute = tk.Label(master=frame_main_top, text="minute", bg="light gray", font=('arial', 12))
lable_minute.grid(column=2, row=0)

lable_time = tk.Label(master=frame_main_top, text="timer", bg="light gray", font=('arial', 12))
lable_time.grid(column=4, row=0)


entry_hour = tk.Spinbox(master=frame_main_top, from_=0, to=24, width=3,  font=('arial', 12))
entry_hour.grid(column=1, row=0)


entry_minute = tk.Spinbox(master=frame_main_top, from_=0, to=60, width=3,  font=('arial', 12))
entry_minute.grid(column=3, row=0)

#-----------------------------------------------------------------------------------------------------------------------------------#


#buttons for shutting down, restarting, sleeping and logging off. 
button_shutdown = tk.Button(master=frame_main, text="Shutdown", bg="blue", fg="yellow", font=('arial', 12, 'bold'), command= shutdown_time)
button_shutdown.grid(column=2, row=0, padx=5, pady=20)

button_restart = tk.Button(master=frame_main, text="Restart", bg="blue", fg="yellow", font=('arial', 12, 'bold'), command= restart)
button_restart.grid(column=0, row=0, padx=5, pady=20)

button_cancel = tk.Button(master=frame_main_bottom, text="Cancel Timer", bg="dark blue", fg="yellow", font=('arial', 12, 'bold'), command= cancel_timer)
button_cancel.grid(column=1, row=0)



#-----------------------------------------------------------------------------------------------------------------------------------#

root.mainloop()
