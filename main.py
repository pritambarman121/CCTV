from tkinter import*
from PIL import Image,ImageTk
from record import record



window = Tk()
window.title("CCTV")
window.iconphoto(False,PhotoImage(file='icon1.png'))
window.geometry('1080x240')

#main frame
mainFrame = Frame(window,bd=2)

label_title = Label(mainFrame,text = "CCTV       AMERA",font=('Helvitica',40,'bold'))
label_title.grid(pady=(10,10),column=1)   #title 

icon_1=Image.open('icons/icon1.png')
icon_1=icon_1.resize((50,50),Image.ANTIALIAS)
icon_1=ImageTk.PhotoImage(icon_1)
label_icon_1=Label(mainFrame,image=icon_1)
label_icon_1.grid(row=0,pady=(5,10),column=1)   #title icon

#record btn
btn_image=Image.open('icons/recording.png')
btn_image=btn_image.resize((60,60),Image.ANTIALIAS)
btn_image=ImageTk.PhotoImage(btn_image)

btn=Button(mainFrame,font=('Helvitica',20,'bold'),height=90,width=200,image=btn_image,compound='left',command=record)
btn.grid(row=1,pady=(20,10),column=0)

#file btn
btn_image1=Image.open('icons/File.png')
btn_image1=btn_image1.resize((60,60),Image.ANTIALIAS)
btn_image1=ImageTk.PhotoImage(btn_image1)

btn=Button(mainFrame,font=('Helvitica',20,'bold'),height=90,width=200,image=btn_image1,compound='left')
btn.grid(row=1,pady=(10,10),column=1)

#exit btn
btn_image2=Image.open('icons/exit.png')
btn_image2=btn_image2.resize((60,60),Image.ANTIALIAS)
btn_image2=ImageTk.PhotoImage(btn_image2)

btn=Button(mainFrame,font=('Helvitica',20,'bold'),height=90,width=200,image=btn_image2,compound='left',command=window.quit)
btn.grid(row=1,pady=(10,10),column=2)



mainFrame.pack()

window.mainloop()