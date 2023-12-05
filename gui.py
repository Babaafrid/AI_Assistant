from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg = "lightyellow")

#ask fun

def ask():
    user_val = speech_to_text.speechtotext()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->'+ user_val+"\n")
    if bot_val != None:
        text.insert(END, "ITACHI <---"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()


def send(event=None):  # Modified function to take an event argument (defaulted to None)
    send_text()

def send_text():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->' + send + "\n")
    if bot is not None:
        text.insert(END, "ITACHI <---" + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

def del_text():
    text.delete('1.0',"end")

#frame

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="yellow")
frame.grid(row=0,column=1,padx=55,pady=10)

#text label

text_label = Label(frame, text="AI Assistant", font=("comic Sans ms", 14, "bold"), bg="lightgreen")
text_label.grid(row=0, column=0, padx=20,pady=10)

#image label

image = Image.open("image/itachi.png")
resized_image = image.resize((200, 200), Image.BICUBIC)
tk_image = ImageTk.PhotoImage(resized_image)

image_label = Label(frame, image=tk_image)
image_label.grid(row=1,column=0,pady=20)

#Text widget

text = Text(root, font=('courier 10 bold'), bg="yellow")
text.grid(row=2,column=0)
text.place(x=100, y=375, width=375, height=100)

#Entry Widget
entry = Entry(root, justify=CENTER)
entry.place(x=100,y=500,width=350, height=30)
entry.bind("<Return>", send)

#Button 1

Button1 = Button(root, text="Ask",bg="yellow",pady=16,padx=40,borderwidth=3,relief=SOLID, command=ask)
Button1.place(x=70,y=575)

#Button 2

Button2 = Button(root, text="Send",bg="yellow",pady=16,padx=40,borderwidth=3,relief=SOLID, command=send_text)
Button2.place(x=400,y=575)

#Button 3

Button1 = Button(root, text="Delete",bg="yellow",pady=16,padx=40,borderwidth=3,relief=SOLID, command=del_text)
Button1.place(x=225,y=575)



root.mainloop()