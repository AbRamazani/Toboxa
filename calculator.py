from tkinter import *
from tkinter import messagebox

def open_calculator_page(pre_page):
    pre_page.destroy()
    calculator = Tk()
    calculator.config(bg="light blue")
    calculator.title("Toboxa=>calculator")
    calculator.geometry("650x600+50+50")
    calculator.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/math/calculator_icon.png")

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
            calculator.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            calculator.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(calculator, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(calculator, width=150, height=600, bg="#01ab8c")

    def home():
        calculator.destroy()
        from Toboxa import home
        home()

    def area():
        from area import open_area_page
        open_area_page(calculator)

    def date():
        from date import open_date_page
        open_date_page(calculator)

    def unit_math():
        from unit_math import open_unit_math_page
        open_unit_math_page(calculator)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn bold", 15)).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="محاسبه مساحت", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=area).place(x=0, y=65)
    Button(hamburgar_menu, text="تبدیل تاریخ", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=date).place(x=0, y=100)
    Button(hamburgar_menu, text="مبدل واحد", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=unit_math).place(x=0, y=135)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=calculator.destroy).place(x=0, y=550)

    # title and img
    Label(calculator, image=img, bg="light blue").place(x=150, y=0)
    Label(calculator, text="ماشین حساب", bg="light blue", justify="center", font=("Vazirmatn bold", 35)).place(x=300, y=0)

    # categories

    cadr = Frame(calculator, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    display = Entry(cadr, font=('Vazirmatn bold', 20), justify='left', borderwidth=15, bg="#57B2C7")
    display.place(x=0, y=0, width=485)

    def click_app(ap):
        if display.get() == "Error":
            display.delete(0, END)
        display.insert(END, ap)

    def delete_last():
        len_nums = len(display.get())
        display.delete(len_nums-1, END)

    def clear(event=None):
        if event != None and display.get() == "Error":
            display.delete(0, END)
        
        if event == None:
            display.delete(0, END)

    def result(event=None):
        try:
            nums = display.get().replace("×", "*").replace("/", ".").replace("^", "**").replace("÷", "/")
            res = eval(nums)
            display.delete(0, END)
            display.insert(0, str(res))
        except:
            if not display.get() == "":
                display.delete(0, END)
                display.insert(0, "Error")

    display.bind("<Return>", result)
    display.bind("<Key>", clear)

    Button7 = Button(cadr, text=7, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("7")).place(x=0, y=133, width=121.25, height=63)
    Button8 = Button(cadr, text=8, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("8")).place(x=121.25, y=133, width=121.25, height=63)
    Button9 = Button(cadr, text=9, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("9")).place(x=242.5, y=133, width=121.25, height=63)
    Buttonmul = Button(cadr, text="×", font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("×")).place(x=363.74, y=133, width=121.25, height=63)

    Button4 = Button(cadr, text=4, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("4")).place(x=0, y=196, width=121.25, height=63)
    Button5 = Button(cadr, text=5, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("5")).place(x=121.25, y=196, width=121.25, height=63)
    Button6 = Button(cadr, text=6, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("6")).place(x=242.5, y=196, width=121.25, height=63)
    Buttonsub = Button(cadr, text="-", font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("-")).place(x=363.74, y=196, width=121.25, height=63)

    Button1 = Button(cadr, text=1, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("1")).place(x=0, y=259, width=121.25, height=63)
    Button2 = Button(cadr, text=2, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("2")).place(x=121.25, y=259, width=121.25, height=63)
    Button3 = Button(cadr, text=3, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("3")).place(x=242.5, y=259, width=121.25, height=63)
    Buttonplus = Button(cadr, text="+", font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("+")).place(x=363.74, y=259, width=121.25, height=63)

    Button_c = Button(cadr, text="C", font=("Vazirmatn bold", 30), bg="light blue", command=clear).place(x=0, y=322, width=121.25, height=63)
    Button0 = Button(cadr, text=0, font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("0")).place(x=121.25, y=322, width=121.25, height=63)
    Buttonra = Button(cadr, text="/", font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("/")).place(x=242.5, y=322, width=121.25, height=63)
    Buttonequ = Button(cadr, text="=", font=("Vazirmatn bold", 30), bg="light blue", command=result).place(x=363.74, y=322, width=121.25, height=63)    

    Buttondel = Button(cadr, text="Del", font=("Vazirmatn bold", 30), bg="light blue", command=delete_last).place(x=0, y=70, width=121.25, height=63)
    Buttondiv = Button(cadr, text="÷", font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("÷")).place(x=121.25, y=70, width=121.25, height=63)
    Buttonexp = Button(cadr, text="x", font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("^")).place(x=242.5, y=70, width=121.25, height=63)
    Button(cadr, text="x", bg="light blue", font=("Vazirmatn bold", 8), bd=0, command=lambda: click_app("^")).place(x=310, y=75)
    Buttonbra_o = Button(cadr, text="(", font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app("(")).place(x=363.74, y=70, width=60.625, height=63)
    Buttonbra_c = Button(cadr, text=")", font=("Vazirmatn bold", 30), bg="light blue", command=lambda: click_app(")")).place(x=424.365, y=70, width=60.625, height=63)

    calculator.mainloop()