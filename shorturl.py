import tkinter
import pyshorteners
from tkinter import messagebox

window=tkinter.Tk()
window.configure(bg='cornflower blue')
window.geometry('500x300')
window.title('URL Shortener')

frame=tkinter.Frame(bg='cornflower blue')

def shorturl():
    shortners=pyshorteners.Shortener()
    short_url=shortners.tinyurl.short(url_entry.get())
    newurl_entry.insert(0, short_url)
    messagebox.showinfo(title="Shortened URL", message=short_url)



#creating widgets

heading_label=tkinter.Label(frame,text='URL Shortener', font=('Times New Roman', 20), fg='midnight blue', bg='cornflower blue')
url_label=tkinter.Label(frame, text='Enter URL',bg='cornflower blue', fg='#FFFFFF', font=('Times New Roman', 12))
url_entry=tkinter.Entry(frame)
newurl_label=tkinter.Label(frame,text='Shortened URL',bg='cornflower blue', fg='#FFFFFF', font=('Times New Roman', 12))
newurl_entry=tkinter.Entry(frame)
submit_button=tkinter.Button(frame, text='Submit', font=('Times New Roman', 8), command=shorturl)

ending=tkinter.Label(frame, text='''~   _      _      _
>(.)__ <(.)__ =(.)__
 (___/  (___/  (___/ ''',bg='cornflower blue')

#displaying widgets
url_label.grid(row=1, column=0, padx=10)
url_entry.grid(row=1, column=1, pady=10)
newurl_label.grid(row=2, column=0, padx=10)
newurl_entry.grid(row=2, column=1, pady=10)
heading_label.grid(row=0, column=0, columnspan=2, pady=20)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)
ending.grid(row=4, column=0, columnspan=2, pady=0)

frame.pack()


window.mainloop()