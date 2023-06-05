from tkinter import *
from tkinter import messagebox

def is_float(str):
    try:
        float(str)
        return True
    except:
        return False

def open_area_page(pre_page):
    pre_page.destroy()
    area = Tk()
    area.config(bg="light blue")
    area.title("Toboxa=>calculate area")
    area.geometry("650x600+50+50")
    area.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/math/select_icon.png")

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
            area.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            area.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(area, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(area, width=150, height=600, bg="#01ab8c")

    def home():
        area.destroy()
        from Toboxa import home
        home()

    def date():
        from date import open_date_page
        open_date_page(area)

    def calculator():
        from calculator import open_calculator_page
        open_calculator_page(area)

    def unit_math():
        from unit_math import open_unit_math_page
        open_unit_math_page(area)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="تبدیل تاریخ", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=date).place(x=0, y=65)
    Button(hamburgar_menu, text="ماشین حساب", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=calculator).place(x=0, y=100)
    Button(hamburgar_menu, text="مبدل واحد", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=unit_math).place(x=0, y=135)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=area.destroy).place(x=0, y=550)

    # title and img
    Label(area, image=img, bg="light blue").place(x=150, y=0)
    Label(area, text="محاسبه مساحت", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=300, y=0)

    # categories

    cadr = Frame(area, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    def rectangle_page():
        rectangle = Toplevel()
        rectangle.geometry("500x500")
        rectangle.config(bg="light blue")
        rectangle.title("Toboxa=>calculate area=>rectangle")
        rectangle_img = PhotoImage(file="files/images/math/area/rectangle.png")
        Label(rectangle, image=rectangle_img, bg="light blue").pack()

        # sides:
        Label(rectangle, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(rectangle, font=("Vazirmatn", 10, "bold"))
        side_a.pack()
        Label(rectangle, text=":b ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_b = Entry(rectangle, font=("Vazirmatn", 10, "bold"))
        side_b.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                num_b = side_b.get().replace("/", ".")
                if is_float(num_b):
                    num_b = float(num_b)
                    finall = num_a * num_b
                    finall_show.config(text=f"= مساحت \n{finall}")
                else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")
            else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")            

        Button(rectangle, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(rectangle, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        rectangle.mainloop()

    def square_page():
        square = Toplevel()
        square.geometry("500x500")
        square.config(bg="light blue")
        square.title("Toboxa=>calculate area=>square")
        square_img = PhotoImage(file="files/images/math/area/square.png")
        Label(square, image=square_img, bg="light blue").pack()

        # sides:
        Label(square, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(square, font=("Vazirmatn", 10, "bold"))
        side_a.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                finall = num_a * num_a
                finall_show.config(text=f"= مساحت \n{finall}")
            else:
                messagebox.showerror("خطا", "لطفا عدد وارد کنید")   

        Button(square, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(square, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        square.mainloop()

    def parallelogram_page():
        parallelogram = Toplevel()
        parallelogram.geometry("500x500")
        parallelogram.config(bg="light blue")
        parallelogram.title("Toboxa=>calculate area=>parallelogram")
        parallelogram_img = PhotoImage(file="files/images/math/area/parallelogram.png")
        Label(parallelogram, image=parallelogram_img, bg="light blue").pack()

        # sides:
        Label(parallelogram, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(parallelogram, font=("Vazirmatn", 10, "bold"))
        side_a.pack()
        Label(parallelogram, text=":h ارتفاع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_b = Entry(parallelogram, font=("Vazirmatn", 10, "bold"))
        side_b.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                num_b = side_b.get().replace("/", ".")
                if is_float(num_b):
                    num_b = float(num_b)
                    finall = num_a * num_b
                    finall_show.config(text=f"= مساحت \n{finall}")
                else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")
            else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")            

        Button(parallelogram, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(parallelogram, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        parallelogram.mainloop()

    def rhombus_page():
        rhombus = Toplevel()
        rhombus.geometry("500x500")
        rhombus.config(bg="light blue")
        rhombus.title("Toboxa=>calculate area=>rhombus")
        rhombus_img = PhotoImage(file="files/images/math/area/rhombus.png")
        Label(rhombus, image=rhombus_img, bg="light blue").pack()

        # sides:
        Label(rhombus, text=":k1 قطر", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(rhombus, font=("Vazirmatn", 10, "bold"))
        side_a.pack()
        Label(rhombus, text=":k2 قطر", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_b = Entry(rhombus, font=("Vazirmatn", 10, "bold"))
        side_b.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                num_b = side_b.get().replace("/", ".")
                if is_float(num_b):
                    num_b = float(num_b)
                    finall = (num_a * num_b) / 2
                    finall_show.config(text=f"= مساحت \n{finall}")
                else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")
            else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")            

        Button(rhombus, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(rhombus, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        rhombus.mainloop()

    def triangle_page():
        triangle = Toplevel()
        triangle.geometry("500x500")
        triangle.config(bg="light blue")
        triangle.title("Toboxa=>calculate area=>triangle")
        triangle_img = PhotoImage(file="files/images/math/area/triangle.png")
        Label(triangle, image=triangle_img, bg="light blue").pack()

        # sides:
        Label(triangle, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(triangle, font=("Vazirmatn", 10, "bold"))
        side_a.pack()
        Label(triangle, text=":h ارتفاع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_b = Entry(triangle, font=("Vazirmatn", 10, "bold"))
        side_b.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                num_b = side_b.get().replace("/", ".")
                if is_float(num_b):
                    num_b = float(num_b)
                    finall = (num_a * num_b) / 2
                    finall_show.config(text=f"= مساحت \n{finall}")
                else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")
            else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")            

        Button(triangle, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(triangle, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        triangle.mainloop()

    def trapezoid_page():
        trapezoid = Toplevel()
        trapezoid.geometry("500x500")
        trapezoid.config(bg="light blue")
        trapezoid.title("Toboxa=>calculate area=>trapezoid")
        trapezoid_img = PhotoImage(file="files/images/math/area/trapezoid.png")
        Label(trapezoid, image=trapezoid_img, bg="light blue").pack()

        # sides:
        Label(trapezoid, text=":c ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(trapezoid, font=("Vazirmatn", 10, "bold"))
        side_a.pack()
        Label(trapezoid, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_b = Entry(trapezoid, font=("Vazirmatn", 10, "bold"))
        side_b.pack()
        Label(trapezoid, text=":h ارتفاع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_h = Entry(trapezoid, font=("Vazirmatn", 10, "bold"))
        side_h.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                num_b = side_b.get().replace("/", ".")
                if is_float(num_b):
                    num_b = float(num_b)
                    num_h = side_h.get().replace("/", ".")
                    if is_float(num_h):
                        num_h = float(num_h)
                        finall = ((num_a + num_b)/ 2) * num_h
                        finall_show.config(text=f"= مساحت \n{finall}")
                    else:
                        messagebox.showerror("خطا", "لطفا عدد وارد کنید")
                else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")
            else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")            

        Button(trapezoid, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(trapezoid, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        trapezoid.mainloop()

    def pentagon_page():
        pentagon = Toplevel()
        pentagon.geometry("500x500")
        pentagon.config(bg="light blue")
        pentagon.title("Toboxa=>calculate area=>pentagon")
        pentagon_img = PhotoImage(file="files/images/math/area/pentagon.png")
        Label(pentagon, image=pentagon_img, bg="light blue").pack()

        # sides:
        Label(pentagon, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(pentagon, font=("Vazirmatn", 10, "bold"))
        side_a.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                finall = 1.72047740059 * (num_a ** 2)
                finall_show.config(text=f"≈ مساحت \n{finall}")
            else:
                messagebox.showerror("خطا", "لطفا عدد وارد کنید")   

        Button(pentagon, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(pentagon, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        pentagon.mainloop()

    def hexagon_page():
        hexagon = Toplevel()
        hexagon.geometry("500x500")
        hexagon.config(bg="light blue")
        hexagon.title("Toboxa=>calculate area=>hexagon")
        hexagon_img = PhotoImage(file="files/images/math/area/hexagon.png")
        Label(hexagon, image=hexagon_img, bg="light blue").pack()

        # sides:
        Label(hexagon, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(hexagon, font=("Vazirmatn", 10, "bold"))
        side_a.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                finall = 2.59807621135 * (num_a ** 2)
                finall_show.config(text=f"≈ مساحت \n{finall}")
            else:
                messagebox.showerror("خطا", "لطفا عدد وارد کنید")   

        Button(hexagon, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(hexagon, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        hexagon.mainloop()

    def octagon_page():
        octagon = Toplevel()
        octagon.geometry("500x500")
        octagon.config(bg="light blue")
        octagon.title("Toboxa=>calculate area=>octagon")
        octagon_img = PhotoImage(file="files/images/math/area/octagon.png")
        Label(octagon, image=octagon_img, bg="light blue").pack()

        # sides:
        Label(octagon, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(octagon, font=("Vazirmatn", 10, "bold"))
        side_a.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                finall = 4.82842712475 * (num_a ** 2)
                finall_show.config(text=f"≈ مساحت \n{finall}")
            else:
                messagebox.showerror("خطا", "لطفا عدد وارد کنید")   

        Button(octagon, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(octagon, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        octagon.mainloop()

    def circle_page():
        circle = Toplevel()
        circle.geometry("500x500")
        circle.config(bg="light blue")
        circle.title("Toboxa=>calculate area=>circle")
        circle_img = PhotoImage(file="files/images/math/area/circle.png")
        Label(circle, image=circle_img, bg="light blue").pack()

        # sides:
        Label(circle, text=":a شعاع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(circle, font=("Vazirmatn", 10, "bold"))
        side_a.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                finall = 3.14159265359 * (num_a ** 2)
                finall_show.config(text=f"≈ مساحت \n{finall}")
            else:
                messagebox.showerror("خطا", "لطفا عدد وارد کنید")   

        Button(circle, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(circle, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        circle.mainloop()

    def ellipse_page():
        ellipse = Toplevel()
        ellipse.geometry("500x500")
        ellipse.config(bg="light blue")
        ellipse.title("Toboxa=>calculate area=>ellipse")
        ellipse_img = PhotoImage(file="files/images/math/area/ellipse.png")
        Label(ellipse, image=ellipse_img, bg="light blue").pack()

        # sides:
        Label(ellipse, text=":a ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_a = Entry(ellipse, font=("Vazirmatn", 10, "bold"))
        side_a.pack()
        Label(ellipse, text=":b ضلع", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()
        side_b = Entry(ellipse, font=("Vazirmatn", 10, "bold"))
        side_b.pack()

        def comp():
            num_a = side_a.get().replace("/", ".")
            if is_float(num_a):
                num_a = float(num_a)
                num_b = side_b.get().replace("/", ".")
                if is_float(num_b):
                    num_b = float(num_b)
                    finall = num_a * num_b * 3.14159265359
                    finall_show.config(text=f"= مساحت \n{finall}")
                else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")
            else:
                    messagebox.showerror("خطا", "لطفا عدد وارد کنید")            

        Button(ellipse, text="محاسبه کن", bg="light blue", font=("Vazirmatn", 15, "bold"), command=comp).pack(pady=20)

        finall_show = Label(ellipse, bg="light blue", font=("Vazirmatn", 15, "bold"))
        finall_show.pack()

        ellipse.mainloop()

    Button(cadr, text="مستطیل", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=rectangle_page).place(x=2, y=0)
    Button(cadr, text="مربع", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=square_page).place(x=166, y=0)
    Button(cadr, text="متوازی الاضلاع", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=parallelogram_page).place(x=330, y=0)
    Button(cadr, text="لوزی", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=rhombus_page).place(x=2, y=100)
    Button(cadr, text="مثلث", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=triangle_page).place(x=166, y=100)
    Button(cadr, text="ذوزنقه", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=trapezoid_page).place(x=330, y=100)
    Button(cadr, text="پنج ضلعی", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=pentagon_page).place(x=330, y=200)
    Button(cadr, text="شش ضلعی", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=hexagon_page).place(x=166, y=200)
    Button(cadr, text="هشت ضلعی", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=octagon_page).place(x=2, y=200)
    Button(cadr, text="دایره", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=circle_page).place(x=166, y=300)
    Button(cadr, text="بیضی", font=("Vazirmatn", 15, "bold"), bg="light blue", width=13, height=2, command=ellipse_page).place(x=330, y=300)

    area.mainloop()