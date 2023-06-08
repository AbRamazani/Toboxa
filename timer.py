from tkinter import *
from winsound import Beep

def open_timer_page(pre_page):
    pre_page.destroy()
    timer = Tk()
    timer.config(bg="light blue")
    timer.title("Toboxa=>timer")
    timer.geometry("650x600+50+50")
    timer.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/other/timer_icon.png")

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
            timer.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            timer.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(timer, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(timer, width=150, height=600, bg="#01ab8c")

    def home():
        timer.destroy()
        from Toboxa import home
        home()

    def stopwatch():
        from stopwatch import open_stopwatch_page
        open_stopwatch_page(timer)

    def net_speed():
        from net_speed import open_net_speed_page
        open_net_speed_page(timer)

    def password_maker():
        from password_maker import open_password_maker_page
        open_password_maker_page(timer)

    def qrcode_maker():
        from qrcode_maker import open_qrcode_maker_page
        open_qrcode_maker_page(timer)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="کرنومتر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=stopwatch).place(x=0, y=65)
    Button(hamburgar_menu, text="سرعت اینرنت", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=net_speed).place(x=0, y=100)
    Button(hamburgar_menu, text="تولیدکننده رمز", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=password_maker).place(x=0, y=135)
    Button(hamburgar_menu, text="تولیدکننده\nQRcode", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=qrcode_maker).place(x=0, y=170)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=timer.destroy).place(x=0, y=550)

    # title and img
    Label(timer, image=img, bg="light blue").place(x=150, y=0)
    Label(timer, text="تایمر", bg="light blue", justify="center", font=("Vazirmatn Medium", 35, "bold")).place(x=365, y=0)

    # categories

    cadr = Frame(timer, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    global mode, reset_m
    mode = ""
    reset_m = False

    h_t = Label(cadr,font=('Vazirmatn Medium',15,'bold'), text="ساعت", relief="ridge", bg="light blue")                
    h_t.place(y=0, x=0, width=162, height=45)

    m_t = Label(cadr,font=('Vazirmatn Medium',15,'bold'), text="دقیقه", relief="ridge", bg="light blue")                
    m_t.place(y=0, x=162, width=162, height=45)

    s_t = Label(cadr,font=('Vazirmatn Medium',15,'bold'), text="ثانیه", relief="ridge", bg="light blue")                
    s_t.place(y=0, x=324, width=162, height=45)

    h = Label(cadr,font=('Vazirmatn Medium',15,'bold'), text="0", relief="ridge", bg="light blue")                
    h.place(y=45, x=0, width=162, height=45)

    m = Label(cadr,font=('Vazirmatn Medium',15,'bold'), text="00", relief="ridge", bg="light blue")                
    m.place(y=45, x=162, width=162, height=45)

    s = Label(cadr,font=('Vazirmatn Medium',15,'bold'), text="00", relief="ridge", bg="light blue")                
    s.place(y=45, x=324, width=162, height=45)

    h_val = IntVar(value=0)
    h_s = Spinbox(cadr, textvariable=h_val, from_=0, to=24, wrap=True, font=('Vazirmatn Medium',15,'bold'))
    h_s.place(x=0, y=95, width=162, height=45)

    m_val = IntVar(value=0)
    m_s = Spinbox(cadr, textvariable=m_val, from_=0, to=59, wrap=True, font=('Vazirmatn Medium',15,'bold'))
    m_s.place(x=162, y=95, width=162, height=45)

    s_val = IntVar(value=1)
    s_s = Spinbox(cadr, textvariable=s_val, from_=0, to=59, wrap=True, font=('Vazirmatn Medium',15,'bold'))
    s_s.place(x=324, y=95, width=162, height=45)

    def second_go(hour, minute, second, c=False):
        global mode, reset_m
        sh = (second >= 1 or (minute > 0 or hour > 0)) and not reset_m
        if sh:
            if c and mode=="go":
                if second >= 1:
                    second -= 1
                    second_t = str(second)
                    if len(str(second)) == 1:
                        second_t = f"0{second}"
                    s.config(text=second_t)
                elif minute > 0:
                    minute -= 1
                    second = 59
                    minute_t = str(minute)
                    if len(str(minute)) == 1:
                        minute_t = f"0{minute}"
                    m.config(text=str(minute_t))
                    s.config(text="59")
                elif hour > 0:
                    hour -= 1
                    minute = 59
                    second = 59
                    h.config(text=str(hour))
                    m.config(text="59")
                    s.config(text="59")
            timer.after(1000, lambda: second_go(hour, minute, second, True))
        else:
            stop_b.place_forget()
            cont_b.place_forget()
            reset_b.place_forget()
            start_b.place(x=0, y=150, width=486, height=45)
            if not (second >= 1 or (minute > 0 or hour > 0)):
                Beep(1500, 500)
                Beep(1500, 500)
                Beep(1500, 500)
            h_s.config(state=NORMAL)
            m_s.config(state=NORMAL)
            s_s.config(state=NORMAL)
            reset_m = False

    def start():
        global mode
        try:
            hour = h_val.get()
            minute = m_val.get()
            second = s_val.get()
            sh = hour >= 0 and hour <= 24 and minute >= 0 and minute <= 59 and (second >= 1 or (minute > 0 or hour > 0)) and second <= 59
            if sh:
                mode = "go"
                h_s.config(state=DISABLED)
                m_s.config(state=DISABLED)
                s_s.config(state=DISABLED)

                h.config(text=str(hour))
                if len(str(minute)) == 1:
                    minute = f"0{minute}"
                m.config(text=str(minute))
                if len(str(second)) == 1:
                    second = f"0{second}"
                s.config(text=str(second))

                hour = h_val.get()
                minute = m_val.get()
                second = s_val.get()

                start_b.place_forget()
                stop_b.place(x=0, y=150, width=242, height=45)
                reset_b.place(x=244, y=150, width=242, height=45)
                second_go(hour, minute, second)
        except:
            pass

    def stop():
        global mode
        stop_b.place_forget()
        cont_b.place(x=0, y=150, width=242, height=45)
        mode = "stop"

    def cont():
        global mode
        cont_b.place_forget()
        stop_b.place(x=0, y=150, width=242, height=45)
        mode = "go"

    def reset():
        global reset_m
        reset_m = True
        h.config(text="0")
        m.config(text="00")
        s.config(text="00")
        h_val.set(0)
        m_val.set(0)
        s_val.set(1)

    start_b = Button(cadr, text="شروع", bg="light blue", font=('Vazirmatn Medium',15,'bold'), command=start)
    start_b.place(x=0, y=150, width=486, height=45)

    stop_b = Button(cadr, text="توقف", bg="light blue", font=('Vazirmatn Medium',15,'bold'), command=stop)
    cont_b = Button(cadr, text="ادامه", bg="light blue", font=('Vazirmatn Medium',15,'bold'), command=cont)
    reset_b = Button(cadr, text="بازنشانی", bg="light blue", font=('Vazirmatn Medium',15,'bold'), command=reset)
    
    timer.mainloop()