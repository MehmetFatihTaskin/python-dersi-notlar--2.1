
from cProfile import label
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter.font import BOLD
from turtle import left
from tkinter import messagebox
master = Tk()
canvas = Canvas(master , height=450 , width=750)
canvas.pack()


frame_ust = Frame(master , bg="#eab676")
frame_ust.place(relx=0.1 , rely=0.1 , relheight=0.1 , relwidth=0.75)

frame_alt = Frame(master , bg="#eab676")
frame_alt.place(relx=0.1 , rely=0.21 , relheight=0.56 , relwidth=0.75)

giris_etiketi = Label(frame_ust, bg ="#eab676", text ="Uludağ banka hoşgeldiniz.", font="Verdana 12 bold")
giris_etiketi.pack(padx=10 , pady=10 , side=TOP)


sifre_yazısı = Label(frame_alt, bg="#eab676", text ="Lütfen şifrenizi gireceğiniz yöntemi seçin " , font="Verdana 12 bold")
sifre_yazısı.pack(padx=10 , pady=40 , side=TOP)

def gönder():
    son_mesaj = ""

    if var.get:
        if var.get ==1:
            son_mesaj += "Okul hesabıyla girin "
        elif var.get ==2:
            son_mesaj += "Banka şifrenizle girin"
        messagebox.showinfo("Giriş başarılı", son_mesaj)

    return    


metin_alanı = Text(frame_alt , height=2 , width=30)
metin_alanı.tag_configure("style", foreground ="#eab676", font=("Verdana" , "12" , "bold" ))
metin_alanı.pack()

Label(frame_alt, bg ="#eab676", text ="Giriş yöntemi.", font="Verdana 12 bold", padx=10, pady=10, anchor=NW)
var = IntVar()

R1 = Radiobutton(frame_alt, text="Okul hesabıyla", variable=var , value=1, bg="#eab676", font="Verdana 10 bold")
R1.pack(anchor=NW, pady=5, padx=15)


R2 = Radiobutton(frame_alt, text="Banka hesab numarasıyla",variable=var, value=2, bg="#eab676", font="Verdana 10 bold")
R2.pack(anchor=NW, pady=5, padx=15)

if var ==1:
    karşılama_metni1 = "şifrenizi buraya giriniz..."
    metin_alanı.insert(END , karşılama_metni1 , "style")
else :
    karşılama_metni2 = "şifrenizi buraya giriniz..."
    metin_alanı.insert(END , karşılama_metni2 , "style")


giriş_butonu = Button(frame_alt, text="Giriş",command=master.destroy, background="light blue")

giriş_butonu.pack(anchor=S)



master.mainloop() 


<<<<<<< HEAD
=======
master.mainloop()

sayfa3 = Tk()
print("ddeneme")


sayfa3.mainloop()
>>>>>>> c62d8b491d9f79dc35085a542443d165e5c5e974
=======
>>>>>>> 6af652353ccbfb9462e38b41d383f980a156824b















print("yazdığımız dosya nereye gidiyor")