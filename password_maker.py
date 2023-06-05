from tkinter import *
from tkinter import messagebox
from string import ascii_letters, punctuation, digits
from pyperclip import copy
from random import choice

def open_password_maker_page(pre_page):
    pre_page.destroy()
    password_maker = Tk()
    password_maker.config(bg="light blue")
    password_maker.title("Toboxa=>password maker")
    password_maker.geometry("650x600+50+50")
    password_maker.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/other/password_icon.png")

    # hamburgar menu
    global mak_ham
    mak_ham = -150
    def open_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(bd=0, image="")
        if mak_ham <= 0:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham += 1
            password_maker.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            password_maker.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(password_maker, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(password_maker, width=150, height=600, bg="#01ab8c")

    def home():
        password_maker.destroy()
        from Toboxa import home
        home()

    def timer():
        from timer import open_timer_page
        open_timer_page(password_maker)

    def stopwatch():
        from stopwatch import open_stopwatch_page
        open_stopwatch_page(password_maker)

    def net_speed():
        from net_speed import open_net_speed_page
        open_net_speed_page(password_maker)

    def qrcode_maker():
        from qrcode_maker import open_qrcode_maker_page
        open_qrcode_maker_page(password_maker)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn bold", 15)).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="تایمر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=timer).place(x=0, y=65)
    Button(hamburgar_menu, text="کرنومتر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=stopwatch).place(x=0, y=100)
    Button(hamburgar_menu, text="سرعت اینترنت", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=net_speed).place(x=0, y=135)
    Button(hamburgar_menu, text="تولیدکننده\nQRcode", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=qrcode_maker).place(x=0, y=170)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=password_maker.destroy).place(x=0, y=550)

    # title and img
    Label(password_maker, image=img, bg="light blue").place(x=150, y=0)
    Label(password_maker, text="تولیدکننده رمز", bg="light blue", justify="center", font=("Vazirmatn bold", 30)).place(x=320, y=15)

    # categories

    cadr = Frame(password_maker, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    numbers = IntVar()
    numbers_c = Checkbutton(cadr, text="استفاده از اعداد", variable=numbers, bg="light blue", font=("Vazirmatn", 13)).place(x=300, y=0)

    puncts = IntVar()
    puncts_cadr = Checkbutton(cadr, text="(...,#,*)استفاده از علائم", variable=puncts, bg="light blue", font=("Vazirmatn", 13)).place(x=50, y=0)

    Label(cadr, text=": تعداد کاراکتر", bg="light blue", font=("Vazirmatn bold", 15)).place(x=335, y=50)
    count = IntVar(value=12)
    count_cadr = Spinbox(cadr, from_=5, to=50, textvariable=count, wrap=True, font=("Vazirmatn bold", 13)).place(x=50, y=50, width=280)
    

    def make_lorem():
        nums = numbers.get()
        puncs = puncts.get()
        count_ch = count.get()
        
        char = ascii_letters
        if nums:
            char += digits
        if puncs:
            char += punctuation

        password = ""
        for i in range(count_ch):
            password += choice(char)

        result.delete("1.0", END)
        result.insert(END, password)          

    Button(cadr, text="بساز", bg="light blue", font=("Vazirmatn bold", 15), width=35, command=make_lorem).place(x=50, y=105)

    result = Text(cadr, font=("Vazirmatn bold", 13), height=9, width=42, bg="light yellow")
    result.place(x=35, y=170)

    def copy_result():
        text = result.get("1.0", END)
        copy(text)
        messagebox.showinfo("کپی", "رمز کپی شد")

    Button(cadr, text="کپی", bg="light blue", font=("Vazirmatn bold", 10), command=copy_result).place(x=458, y=399, width=30)

    password_maker.mainloop()