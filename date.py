from tkinter import *
from tkinter import messagebox, ttk
from persiantools.jdatetime import JalaliDate

def num_to_name(num, type_d):
    if type_d == 0:
        if num == 1:
            return "1-فروردین"
        elif num == 2:
            return "2-اردیبهشت"
        elif num == 3:
            return "3-خرداد"
        elif num == 4:
            return "4-تیر"
        elif num == 5:
            return "5-مرداد"
        elif num == 6:
            return "6-شهریور"
        elif num == 7:
            return "7-مهر"
        elif num == 8:
            return "8-آبان"
        elif num == 9:
            return "9-آذر"
        elif num == 10:
            return "10-دی"
        elif num == 11:
            return "11-بهمن"
        elif num == 12:
            return "12-اسفند"
    elif type_d == 1:
        if num == 1:
            return "1-January(ژانویه)"
        elif num == 2:
            return "2-February(فوریه)"
        elif num == 3:
            return "3-March(مارس)"
        elif num == 4:
            return "4-April(آوریل)"
        elif num == 5:
            return "5-May(مه)"
        elif num == 6:
            return "6-June(ژوئن)"
        elif num == 7:
            return "7-July(ژوئیه)"
        elif num == 8:
            return "8-August(اوت)"
        elif num == 9:
            return "9-September(سپتامبر)"
        elif num == 10:
            return "10-October(اکتبر)"
        elif num == 11:
            return "11-November(نوامبر)"
        elif num == 12:
            return "12-December(دسامبر)"

def open_date_page(pre_page):
    pre_page.destroy()
    date = Tk()
    date.config(bg="light blue")
    date.title("Toboxa=>date converter")
    date.geometry("650x600+50+50")
    date.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/math/schedule_icon.png")

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
            date.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            date.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(date, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(date, width=150, height=600, bg="#01ab8c")

    def home():
        date.destroy()
        from Toboxa import home
        home()

    def area():
        from area import open_area_page
        open_area_page(date)

    def calculator():
        from calculator import open_calculator_page
        open_calculator_page(date)

    def unit_math():
        from unit_math import open_unit_math_page
        open_unit_math_page(date)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="محاسبه مساحت", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=area).place(x=0, y=65)
    Button(hamburgar_menu, text="ماشین حساب", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=calculator).place(x=0, y=100)
    Button(hamburgar_menu, text="مبدل واحد", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=unit_math).place(x=0, y=135)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=date.destroy).place(x=0, y=550)

    # title and img
    Label(date, image=img, bg="light blue").place(x=150, y=0)
    Label(date, text="تبدیل تاریخ", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=300, y=0)

    # categories

    cadr = Frame(date, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    Label(cadr, text=": نوع تبدیل", bg="light blue", font=("Vazirmatn", 15, "bold")).place(x=300, y=0)
    type_con_t = StringVar()
    type_con = ttk.Combobox(cadr, textvariable=type_con_t, values=("شمسی به میلادی", "میلادی به شمسی"), state="readonly", justify="center", font=("Vazirmatn", 10, "bold"))
    type_con.place(x=135, y=5)

    def show_comboboxes(event):
        global day, month, year
        type_s = type_con_t.get()
        Label(cadr, text=": روز", bg="light blue", font=("Vazirmatn", 15, "bold")).place(x=420, y=40)
        Label(cadr, text=": ماه", bg="light blue", font=("Vazirmatn", 15, "bold")).place(x=180, y=40)
        Label(cadr, text=": سال", bg="light blue", font=("Vazirmatn", 15, "bold")).place(x=250, y=80)
        sub.place(x=200, y=120)
        now.place(x=400, y=100)
        if type_s == "شمسی به میلادی":
            day = StringVar()
            r_d = range(1, 32)
            day_s = ttk.Combobox(cadr, textvariable=day, values=tuple(r_d), state="readonly", justify="center", font=("Vazirmatn", 10, "bold"))
            day_s.place(x=250, y=45)

            month = StringVar()
            months = ("1-فروردین", "2-اردیبهشت", "3-خرداد", "4-تیر", "5-مرداد", "6-شهریور", "7-مهر", "8-آبان", "9-آذر", "10-دی", "11-بهمن", "12-اسفند")
            month_s = ttk.Combobox(cadr, textvariable=month, values=months, state="readonly", justify="center", font=("Vazirmatn", 10, "bold"))
            month_s.place(x=10, y=45)

            year = Entry(cadr, justify="center", font=("Vazirmatn", 10, "bold"))
            year.place(x=100, y=85)
        elif type_s == "میلادی به شمسی":
            day = StringVar()
            r_d = range(1, 32)
            day_s = ttk.Combobox(cadr, textvariable=day, values=tuple(r_d), state="readonly", justify="center", font=("Vazirmatn", 10, "bold"))
            day_s.place(x=250, y=45)

            month = StringVar()
            months = ("1-January(ژانویه)", "2-February(فوریه)", "3-March(مارس)", "4-April(آوریل)", "5-May(مه)", "6-June(ژوئن)", "7-July(ژوئیه)", "8-August(اوت)", "9-September(سپتامبر)", "10-October(اکتبر)", "11-November(نوامبر)", "12-December(دسامبر)")
            month_s = ttk.Combobox(cadr, textvariable=month, values=months, state="readonly", justify="center", font=("Vazirmatn", 10, "bold"))
            month_s.place(x=10, y=45)

            year = Entry(cadr, justify="center", font=("Vazirmatn", 10, "bold"))
            year.place(x=100, y=85)

    type_con.bind("<<ComboboxSelected>>", show_comboboxes)

    def convert():
        global day, month, year
        try:
            type_s = type_con_t.get()
            day_s = day.get().split("-")[0]
            month_s = month.get().split("-")[0]
            year_s = year.get().split("-")[0]
            if day_s.isnumeric() and month_s.isnumeric() and year_s.isnumeric():
                day_s, month_s, year_s = int(day_s), int(month_s), int(year_s)
                if type_s == "شمسی به میلادی":
                    finall = JalaliDate(year_s, month_s, day_s).to_gregorian()
                    type_d = 1
                elif type_s == "میلادی به شمسی":
                    finall = JalaliDate.to_jalali(year_s, month_s, day_s)
                    type_d = 0

                date_r = str(finall).split("-")
                result.config(text=f"{date_r[2]} : روز\n{date_r[1]} : ماه\n{date_r[0]} : سال")
            else:
                messagebox.showerror("خطا" , "مقادیر وارد شده اشتباه می باشد")
        except:
            messagebox.showerror("خطا" , "مقادیر وارد شده اشتباه می باشد")

    def set_now():
        global day, month, year
        type_s = type_con_t.get()
        if type_s == "شمسی به میلادی":
            today = str(JalaliDate.today()).split("-")
            day.set(today[2])
            month.set(num_to_name(int(today[1]), 0))
            year.delete(0, END)
            year.insert(0, today[0])
        elif type_s == "میلادی به شمسی":
            today = str(JalaliDate.today().to_gregorian()).split("-")
            day.set(today[2])
            month.set(num_to_name(int(today[1]), 1))
            year.delete(0, END)
            year.insert(0, today[0])

    sub = Button(cadr, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=convert)
    now = Button(cadr, text="برو به امروز", bg="light blue", font=("Vazirmatn", 8, "bold"), command=set_now)
    result = Label(cadr, bg="light blue", font=("Vazirmatn", 15, "bold"))
    result.place(x=200, y=180)

    date.mainloop()