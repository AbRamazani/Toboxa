from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def is_float(str):
    try:
        float(str)
        return True
    except:
        return False

def open_unit_math_page(pre_page):
    pre_page.destroy()
    unit_math = Tk()
    unit_math.config(bg="light blue")
    unit_math.title("Toboxa=>math units converter")
    unit_math.geometry("650x600+50+50")
    unit_math.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/math/cost_icon.png")

    # hamburger menu
    global mak_ham
    mak_ham = -150
    def open_hamburger():
        global mak_ham
        if mak_ham == -150:
            hamburger_b.config(bd=0, image="")
        if mak_ham <= 0:
            hamburger_menu.place(x=mak_ham, y=0)
            mak_ham += 1
            unit_math.after(10, open_hamburger)

    def close_hamburger():
        global mak_ham
        if mak_ham == -150:
            hamburger_b.config(image=hamburger_img)
        if mak_ham >= -150:
            hamburger_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            unit_math.after(10, close_hamburger)

    hamburger_img = PhotoImage(file="files/images/root/menu.png")
    hamburger_b = Button(unit_math, image=hamburger_img, bg="light blue", bd=0, command=open_hamburger)
    hamburger_b.place(x=0, y=0)

    hamburger_menu = Frame(unit_math, width=150, height=600, bg="#01ab8c")

    def home():
        unit_math.destroy()
        from Toboxa import home
        home()

    def area():
        from area import open_area_page
        open_area_page(unit_math)

    def date():
        from date import open_date_page
        open_date_page(unit_math)

    def calculator():
        from calculator import open_calculator_page
        open_calculator_page(unit_math)

    Label(hamburger_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburger_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburger).place(x=125, y=0)
    Button(hamburger_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburger_menu, text="محاسبه مساحت", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=area).place(x=0, y=65)
    Button(hamburger_menu, text="تبدیل تاریخ", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=date).place(x=0, y=100)
    Button(hamburger_menu, text="ماشین حساب", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=calculator).place(x=0, y=135)
    Button(hamburger_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=unit_math.destroy).place(x=0, y=550)

    # title and img
    Label(unit_math, image=img, bg="light blue").place(x=150, y=0)
    Label(unit_math, text="مبدل واحد", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=300, y=0)

    # categories

    cadr = Frame(unit_math, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    def length_page():
        length = Toplevel(bg="light blue")
        length.title("Toboxa=>math units converter=>length")
        length.geometry("500x500")

        Label(length, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("متر", "سانتی متر", "اینچ", "میلی متر", "فوت", "مایل", "کیلومتر", "ذرع", "گز", "یارد")

        con_from = StringVar()
        con_from_box = ttk.Combobox(length, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(length, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(length, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(length, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(length, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def length_comp(from_val, to_val, val):
            from_to_all = {"متر" : 1.0,
             "سانتی متر" : 100.0,
              "اینچ" : 39.37007874,
               "میلی متر" : 1000.0,
                "فوت" : 3.2808399,
                "مایل" : 0.00062137,
                  "کیلومتر" : 0.001,
                   "ذرع" : 0.96153846,
                    "گز" : 0.96153846,
                    "یارد" : 1.0936133}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{length_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(length, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(length, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(length, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        length.mainloop()





    def weight_page():
        weight = Toplevel(bg="light blue")
        weight.title("Toboxa=>math units converter=>weight")
        weight.geometry("500x500")

        Label(weight, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("تن", "کیلوگرم", "پوند", "گرم", "اسلاگ", "مثقال", "سیر", "نخود", "خروار")

        con_from = StringVar()
        con_from_box = ttk.Combobox(weight, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(weight, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(weight, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(weight, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(weight, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def weight_comp(from_val, to_val, val):
            from_to_all = {"گرم" : 1.0,
            "تن" : 0.000001,
            "کیلوگرم" : 0.001,
            "پوند" : 0.00220462,
                "اسلاگ" : 0.00006852,
                "مثقال" : 0.21701389,
                "سیر" : 0.01333333,
                "نخود" : 5.20833333,
                    "خروار" : 0.00000333}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{weight_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(weight, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(weight, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(weight, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        weight.mainloop()



    def volume_page():
        volume = Toplevel(bg="light blue")
        volume.title("Toboxa=>math units converter=>volume")
        volume.geometry("500x500")

        Label(volume, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("لیتر", "میلی لیتر", "متر مکعب", "فوت مکعب", "سی سی", "اینچ مکعب", "یارد مکعب", "گالن آمریکایی", "گالن انگلیسی")

        con_from = StringVar()
        con_from_box = ttk.Combobox(volume, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(volume, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(volume, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(volume, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(volume, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def volume_comp(from_val, to_val, val):
            from_to_all = {"لیتر" : 1.0,
            "میلی لیتر" : 1000.0,
            "متر مکعب" : 0.001,
            "فوت مکعب" : 0.03531467,
                "سی سی" : 1000.0,
                "اینچ مکعب" : 61.02374409,
                "یارد مکعب" : 0.00130795,
                "گالن آمریکایی" : 0.26417205,
                    "گالن انگلیسی" : 0.21996925}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{volume_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(volume, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(volume, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(volume, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        volume.mainloop()


    def temperature_page():
        temperature = Toplevel(bg="light blue")
        temperature.title("Toboxa=>math units converter=>temperature")
        temperature.geometry("500x500")

        Label(temperature, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("سانتی گراد", "فارنهایت", "کلوین", "رانکین")

        con_from = StringVar()
        con_from_box = ttk.Combobox(temperature, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(temperature, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(temperature, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(temperature, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(temperature, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def temperature_comp(from_val, to_val, val):
            if from_val == to_val:
                finall = val
            elif from_val == "سانتی گراد":
                if to_val == "فارنهایت":
                    finall = (val * 9/5) + 32
                elif to_val == "کلوین":
                    finall = val + 273.15
                elif to_val == "رانکین":
                    finall = (val * 9/5) + 491.67
            elif from_val == "فارنهایت":
                if to_val == "سانتی گراد":
                    finall = (val - 32) * 5/9
                elif to_val == "کلوین":
                    finall = ((val - 32) * 5/9) + 273.15
                elif to_val == "رانکین":
                    finall = val + 459.67
            elif from_val == "کلوین":
                if to_val == "سانتی گراد":
                    finall = val - 273.15
                elif to_val == "فارنهایت":
                    finall = ((val - 273.15) * 9/5) + 32
                elif to_val == "رانکین":
                    finall = (val * 9/5) + 491.67
            elif from_val == "رانکین":
                if to_val == "سانتی گراد":
                    finall = (val - 491.67) * 5/9
                elif to_val == "فارنهایت":
                    finall = val - 459.67
                elif to_val == "کلوین":
                    finall = val * 5/9

            return finall

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{temperature_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(temperature, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(temperature, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(temperature, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        temperature.mainloop()



    def area_page():
        area = Toplevel(bg="light blue")
        area.title("Toboxa=>math units converter=>area")
        area.geometry("500x500")

        Label(area, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("متر مربع", "سانتی متر مربع", "فوت مربع", "اینچ مربع", "مایل مربع", "یارد مربع", "هکتار", "جریب")

        con_from = StringVar()
        con_from_box = ttk.Combobox(area, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(area, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(area, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(area, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(area, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def area_comp(from_val, to_val, val):
            from_to_all = {"متر مربع" : 1.0,
            "سانتی متر مربع" : 10000.0,
            "فوت مربع" : 10.76391042,
            "اینچ مربع" : 1550.00310001,
                "یارد مربع" : 1.19599005,
                "هکتار" : 0.0001,
                "جریب" : 0.000247105,
                "مایل مربع" : 3.86102159 * (10^-7)}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{area_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(area, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(area, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(area, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        area.mainloop()



    # def speed_page():
    #     speed = Toplevel(bg="light blue")
    #     speed.title("Toboxa=>math units converter=>speed")
    #     speed.geometry("500x500")

    #     Label(speed, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

    #     from_to = ("متر", "سانتی متر", "اینچ", "میلی متر", "فوت", "مایل", "کیلومتر", "ذرع", "گز", "یارد")

    #     con_from = StringVar()
    #     con_from_box = ttk.Combobox(speed, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

    #     Label(speed, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

    #     con_to = StringVar()
    #     con_to_box = ttk.Combobox(speed, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

    #     Label(speed, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

    #     value = Entry(speed, font=("Vazirmatn", 15, "bold"))
    #     value.pack()

    def speed_page():
        speed = Toplevel(bg="light blue")
        speed.title("Toboxa=>math units converter=>speed")
        speed.geometry("500x500")

        Label(speed, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("متر بر ثانیه", "فوت بر ثانیه", "کیلومتر بر ساعت", "مایل بر ساعت", "کیلومتر بر ثانیه", "مایل بر ثانیه", "فوت بر دقیقه", "اینچ بر دقیقه")

        con_from = StringVar()
        con_from_box = ttk.Combobox(speed, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(speed, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(speed, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(speed, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(speed, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def speed_comp(from_val, to_val, val):
            from_to_all = {"متر بر ثانیه" : 1.0,
            "فوت بر ثانیه" : 3.2808399,
            "کیلومتر بر ثانیه" : 0.001,
            "کیلومتر بر ساعت" : 3.6,
                "مایل بر ساعت" : 2.23694185,
                "مایل بر ثانیه" : 0.00062137,
                "فوت بر دقیقه" : 196.850394,
                "اینچ بر دقیقه" : 2362.20491041}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{speed_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(speed, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(speed, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(speed, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        speed.mainloop()



    def force_page():
        force = Toplevel(bg="light blue")
        force.title("Toboxa=>math units converter=>force")
        force.geometry("500x500")

        Label(force, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("نیوتن", "گرم-نیرو", "کیلوگرم-نیرو", "پوند-نیرو", "اونس-نیرو", "دین", "پوندال", "کیلوپوند")

        con_from = StringVar()
        con_from_box = ttk.Combobox(force, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(force, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(force, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(force, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(force, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def force_comp(from_val, to_val, val):
            from_to_all = {"نیوتون" : 1.0,
            "گرم-نیرو" : 101.9716213,
            "کیلوگرم-نیرو" : 0.1019716213,
            "پوند-نیرو" : 0.22480894,
                "اونس-نیرو" : 3.59694309,
                "دین" : 100000.0,
                "پوندال" : 7.23301385,
                "کیلوپوند" : 0.1019713213}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{force_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(force, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(force, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(force, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        force.mainloop()



    def energy_page():
        energy = Toplevel(bg="light blue")
        energy.title("Toboxa=>math units converter=>energy")
        energy.geometry("500x500")

        Label(energy, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("ژول", "کیلوژول", "وات ساعت", "کیلو وات ساعت", "کالری", "کیلوکالری", "اسب بخار-ساعت", "فوت پوند")

        con_from = StringVar()
        con_from_box = ttk.Combobox(energy, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(energy, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(energy, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(energy, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(energy, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def energy_comp(from_val, to_val, val):
            from_to_all = {"ژول" : 1.0,
            "کیلوژول" : 0.001,
            "وات ساعت" : 0.000277777778,
            "کیلو وات ساعت" : 2.77777778 * (10 ** -7),
                "کالری" : 0.23900574,
                "کیلوکالری" : 0.00023901,
                "اسب بخار-ساعت" : 3.72506136 * (10*-7),
                "فوت پوند" : 0.73756215}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{energy_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(energy, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(energy, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(energy, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        energy.mainloop()



    def power_page():
        power = Toplevel(bg="light blue")
        power.title("Toboxa=>math units converter=>power")
        power.geometry("500x500")

        Label(power, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("وات", "کیلووات", "اسب بخار", "ژول بر دقیقه", "ژول بر ساعت", "کالری بر دقیقه", "کالری بر ساعت", "لیتر اتمسفر بر دقیقه", "لیتر اتمسفر بر ساعت", "ارگ بر ثانیه")

        con_from = StringVar()
        con_from_box = ttk.Combobox(power, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(power, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(power, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(power, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(power, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def power_comp(from_val, to_val, val):
            from_to_all = {"وات" : 1.0,
            "کیلووات" : 0.001,
            "اسب بخار" : 0.00134102,
            "ژول بر دقیقه" : 60.0,
                "ژول بر ساعت" : 3600.0,
                "کالری بر دقیقه" : 14.34034417,
                "کالری بر ساعت" : 860.4206501,
                "لیتر اتمسفر بر ساعت" : 35.52927968,
                "لیتر اتمسفر بر دقیقه" : 0.59215396,
                "ارگ بر ثانیه" : 10000000}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{power_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(power, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(power, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(power, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()


        power.mainloop()


    def time_page():
        time = Toplevel(bg="light blue")
        time.title("Toboxa=>math units converter=>time")
        time.geometry("500x500")

        Label(time, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("میلی ثانیه", "ثانیه", "دقیقه", "ساعت", "روز", "هفته", "ماه", "سال", "دَهه", "قرن")

        con_from = StringVar()
        con_from_box = ttk.Combobox(time, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(time, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(time, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(time, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(time, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def time_comp(from_val, to_val, val):
            from_to_all = {"میلی ثانیه" : 86400000.0,
            "ثانیه" : 86400.0,
            "دقیقه" : 1440.0,
            "ساعت" : 24.0,
                "روز" : 1.0,
                "هفته" : 0.142857143,
                "دَهه" : 0.00027379,
                "ماه" : 0.03285421,
                "سال" : 0.00273785,
                "قرن" : 0.00002738}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{time_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(time, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(time, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        to_si = Button(time, text="مراجعه نمایید SI برای تبدیل واحد هایی مثل فمتو، دسی، ترا و ... به بخش پسوند های", bg="light blue", activebackground="light blue", fg="red", font=("Vazirmatn", 10, "bold"), bd=0, command=si_page).pack()

        time.mainloop()


    def si_page():
        si = Toplevel(bg="light blue")
        si.title("Toboxa=>math units converter=>SI units")
        si.geometry("500x500")

        Label(si, text=":تبدیل از", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        from_to = ("یوتا", "زتا", "اگزا", "پتا", "ترا", "گیگا", "مگا", "کیلو", "هکتو", "دکا", "یونی", "دسی", "سانتی", "میلی", "میکرو", "نانو", "پیکو", "فمتو", "آتو", "زپتو", "یوکتو")

        con_from = StringVar()
        con_from_box = ttk.Combobox(si, textvariable=con_from, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(si, text=":تبدیل به", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        con_to = StringVar()
        con_to_box = ttk.Combobox(si, textvariable=con_to, values=from_to, state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).pack()

        Label(si, text=":مقدار", bg="light blue", font=("Vazirmatn", 18, "bold")).pack()

        value = Entry(si, font=("Vazirmatn", 15, "bold"))
        value.pack()

        def si_comp(from_val, to_val, val):
            from_to_all = {"یوتا": 1.0,
            "زتا": 1000.0,
            "اگزا": 1000000.0,
            "پتا": 1000000000.0,
            "ترا": 1000000000000.0,
            "گیگا": 1000000000000000.0,
            "مگا": 1000000000000000000.0,
            "کیلو": 1000000000000000000000.0,
            "هکتو": 10000000000000000000000.0,
            "دکا": 100000000000000000000000.0,
            "یونی": 1000000000000000000000000.0,
            "دسی": 10000000000000000000000000.0,
            "سانتی": 100000000000000000000000000.0,
            "میلی": 1000000000000000000000000000.0,
            "میکرو": 1000000000000000000000000000000.0,
            "نانو": 1000000000000000000000000000000000.0,
            "پیکو": 1000000000000000000000000000000000000.0,
            "فمتو": 1000000000000000000000000000000000000000.0,
            "آتو": 1000000000000000000000000000000000000000000.0,
            "زپتو": 1000000000000000000000000000000000000000000000.0,
            "یوکتو": 1000000000000000000000000000000000000000000000000.0,}
            return val * (from_to_all[to_val] / from_to_all[from_val])

        def comp():
            con_from_v = con_from.get()
            con_to_v = con_to.get()
            val = value.get().replace("/", ".")
            if is_float(val):
                text_f = f"{si_comp(con_from_v, con_to_v, float(val))} \n {con_to_v}"
                finall_show.config(text=text_f)
            else:
                messagebox.showerror("خطا", "مقدار وارد شده اشتباه می باشد")
        
        Button(si, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 18, "bold"), command=comp).pack(pady=20)

        finall_show = Label(si, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        si.mainloop()


    Button(cadr, text="طول", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=length_page).place(x=2, y=0)
    Button(cadr, text="جرم", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=weight_page).place(x=166, y=0)
    Button(cadr, text="حجم", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=volume_page).place(x=330, y=0)
    Button(cadr, text="دما", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=temperature_page).place(x=2, y=100)
    Button(cadr, text="مساحت", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=area_page).place(x=166, y=100)
    Button(cadr, text="سرعت", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=speed_page).place(x=330, y=100)
    Button(cadr, text="نیرو", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=force_page).place(x=330, y=200)
    Button(cadr, text="انرژی", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=energy_page).place(x=166, y=200)
    Button(cadr, text="توان", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=power_page).place(x=2, y=200)
    Button(cadr, text="زمان", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=time_page).place(x=330, y=300)
    Button(cadr, text="پسوند های \nSI", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=si_page).place(x=166, y=300)

    unit_math.mainloop()