from tkinter import *
import speedtest  
import subprocess

def open_net_speed_page(pre_page):
    pre_page.destroy()
    net_speed = Tk()
    net_speed.config(bg="light blue")
    net_speed.title("Toboxa=>test internet speed")
    net_speed.geometry("650x600+50+50")
    net_speed.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/other/speed-test_icon.png")

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
            net_speed.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            net_speed.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(net_speed, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(net_speed, width=150, height=600, bg="#01ab8c")

    def home():
        net_speed.destroy()
        from Toboxa import home
        home()

    def timer():
        from timer import open_timer_page
        open_timer_page(net_speed)

    def stopwatch():
        from stopwatch import open_stopwatch_page
        open_stopwatch_page(net_speed)

    def password_maker():
        from password_maker import open_password_maker_page
        open_password_maker_page(net_speed)

    def qrcode_maker():
        from qrcode_maker import open_qrcode_maker_page
        open_qrcode_maker_page(net_speed)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="تایمر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=timer).place(x=0, y=65)
    Button(hamburgar_menu, text="کرنومتر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=stopwatch).place(x=0, y=100)
    Button(hamburgar_menu, text="تولیدکننده رمز", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=password_maker).place(x=0, y=135)
    Button(hamburgar_menu, text="تولیدکننده\nQRcode", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=qrcode_maker).place(x=0, y=170)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=net_speed.destroy).place(x=0, y=550)

    # title and img
    Label(net_speed, image=img, bg="light blue").place(x=150, y=0)
    Label(net_speed, text="تست سرعت اینترنت", bg="light blue", justify="center", font=("Vazirmatn Medium", 28, "bold")).place(x=320, y=15)

    # categories

    cadr = Frame(net_speed, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    st = speedtest.Speedtest()

    def start_du():
        net_speed.title("Toboxa=>test internet speed=>processing...")
        ping_b.place_configure(y=200)
        url_l.place_forget()
        url_e.place_forget()
        pings_b.place_forget()
        ping_l.place_forget()
        download_s.config(text=f"سرعت بارگیری : {round(float(st.download())/8000000, 5)} مگابایت بر ثانیه")
        download_s.place(x=100, y=100)
        upload_s.config(text=f"سرعت بارگذاری : {round(float(st.upload())/8000000, 5)} مگابایت بر ثانیه")
        upload_s.place(x=100, y=150)
        net_speed.title("Toboxa=>test internet speed")

    def open_ping():
        download_s.place_forget()
        upload_s.place_forget()
        ping_b.place_configure(y=100)
        url_l.place(x=295, y=150)
        url_e.place(x=70, y=150)
        pings_b.place(x=20, y=200, width=446, height=45)

    def start_ping():
        net_speed.title("Toboxa=>test internet speed=>processing...")
        p = subprocess.Popen(["ping.exe", url_e.get()], stdout = subprocess.PIPE)
        p = str(p.communicate()[0]).split(r"\r\n")
        if len(p) > 3:
            try:
                p = p[-2].split(",")
                min = int(p[0].split(" ")[-1][:-2])
                max = int(p[1].split(" ")[-1][:-2])
                avg = int(p[2].split(" ")[-1][:-2])
                t = f"""
                بیشترین : {max} میلی ثانیه
                کمترین : {min} میلی ثانیه
                میانگین : {avg} میلی ثانیه
                """
                ping_l.config(text=t)
                ping_l.place(x=100, y=250)
            except:
                t = f"""
خطا در دریافت اطلاعات
ممکن است مدیر سایت این امکان را بسته است
            """
                ping_l.config(text=t)
                ping_l.place(x=70, y=250)
        else:
            t = f"""
خطا در دریافت اطلاعات
ممکن است آدرس را اشتباه وارد کرده باشید
(google.com : آدرس را بدون هیچ حرف اضافه ای وارد کنید مثل)
            """
            ping_l.config(text=t)
            ping_l.place(x=10, y=250)
        net_speed.title("Toboxa=>test internet speed")

    du_b = Button(cadr, text="سرعت بارگیری و بارگذاری", bg="light blue", font=('Vazirmatn Medium',15,'bold'), command=start_du)
    du_b.place(x=0, y=50, width=486, height=45)

    download_s = Label(cadr, bg="light blue", font=('Vazirmatn Medium',13))
    upload_s = Label(cadr, bg="light blue", font=('Vazirmatn Medium',13))

    ping_b = Button(cadr, text="اندازه گیری پینگ", bg="light blue", font=('Vazirmatn Medium',15,'bold'), command=open_ping)
    ping_b.place(x=0, y=100, width=486, height=45)

    url_l = Label(cadr, text=": آدرس سایت", bg="light blue", font=('Vazirmatn Medium',13))
    url_e = Entry(cadr, font=('Vazirmatn Medium',15,'bold'))
    pings_b = Button(cadr, text="اندازه گیری", bg="light blue", font=('Vazirmatn Medium',13,'bold'), command=start_ping)

    ping_l = Label(cadr, bg="light blue", font=('Vazirmatn Medium',13))
    
    net_speed.mainloop()