from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.geometry("450x200")
root.title("Song Selection Menu")

info_label = Label(root, text='Select a song from the drop down list, then click play!')
info_label.grid(row=1,column=1,padx=20,pady=10,sticky='news')

ts_songs = ('Style (Taylor\'s Version) - Taylor Swift',
         'Red (Taylor\'s Version) - Taylor Swift',
         'Love Story (Taylor\'s Version) - Taylor Swift',
         'Enchanted (Taylor\'s Version) - Taylor Swift',
         'champagne problems - Taylor Swift',
         'You Belong with Me (Taylor\'s Version) - Taylor Swift',
         'You\'re On Your Own Kid - Taylor Swift',)

selected_ts_song = StringVar()
ts_song_combobox = ttk.Combobox(root,textvariable=selected_ts_song,width=40)
ts_song_combobox.grid(row=2,column=1,columnspan=3,padx=20,pady=10)
ts_song_combobox['values'] = ts_songs
ts_song_combobox['state'] = "readonly"

buttons_frame = Frame(root)
buttons_frame.grid(row=3,column=1)

def play_song():
    pass

play_button = Button(buttons_frame,text='Play',command=play_song)
play_button.grid(column=1,row=1,padx=10)

quit_button = Button(buttons_frame,text='Quit',command=root.destroy)
quit_button.grid(column=3,row=1,padx=10)

root.mainloop()