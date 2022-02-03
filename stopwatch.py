from tkinter import *

def open_stopwatch_page(pre_page):
    pre_page.destroy()
    stopwatch = Tk()
    stopwatch.config(bg="light blue")
    stopwatch.title("Toboxa=>stopwatch")
    stopwatch.geometry("650x600+50+50")
    stopwatch.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/other/stopwatch_icon.png")

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
            stopwatch.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            stopwatch.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(stopwatch, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(stopwatch, width=150, height=600, bg="#01ab8c")

    def home():
        stopwatch.destroy()
        from Toboxa import home
        home()

    def timer():
        from timer import open_timer_page
        open_timer_page(stopwatch)

    def net_speed():
        from net_speed import open_net_speed_page
        open_net_speed_page(stopwatch)

    def password_maker():
        from password_maker import open_password_maker_page
        open_password_maker_page(stopwatch)

    def qrcode_maker():
        from qrcode_maker import open_qrcode_maker_page
        open_qrcode_maker_page(stopwatch)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir bold", 15)).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="تایمر", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=timer).place(x=0, y=65)
    Button(hamburgar_menu, text="سرعت اینرنت", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=net_speed).place(x=0, y=100)
    Button(hamburgar_menu, text="تولیدکننده رمز", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=password_maker).place(x=0, y=135)
    Button(hamburgar_menu, text="تولیدکننده\nQRcode", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=qrcode_maker).place(x=0, y=170)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=stopwatch.destroy).place(x=0, y=550)

    # title and img
    Label(stopwatch, image=img, bg="light blue").place(x=150, y=0)
    Label(stopwatch, text="کرنومتر", bg="light blue", justify="center", font=("vazir bold", 35)).place(x=365, y=0)

    # categories

    cadr = Frame(stopwatch, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    global mode, reset_m
    mode = ""
    reset_m = False

    h_t = Label(cadr,font=('vazir',15,'bold'), text="ساعت", relief="ridge", bg="light blue")                
    h_t.place(y=0, x=0, width=121.5, height=45)

    m_t = Label(cadr,font=('vazir',15,'bold'), text="دقیقه", relief="ridge", bg="light blue")                
    m_t.place(y=0, x=121.5, width=121.5, height=45)

    s_t = Label(cadr,font=('vazir',15,'bold'), text="ثانیه", relief="ridge", bg="light blue")                
    s_t.place(y=0, x=243, width=121.5, height=45)

    ss_t = Label(cadr,font=('vazir',15,'bold'), text="صدم ثانیه", relief="ridge", bg="light blue")                
    ss_t.place(y=0, x=364.5, width=121.5, height=45)

    h = Label(cadr,font=('vazir',15,'bold'), text="0", relief="ridge", bg="light blue")                
    h.place(y=45, x=0, width=121.5, height=45)

    m = Label(cadr,font=('vazir',15,'bold'), text="00", relief="ridge", bg="light blue")                
    m.place(y=45, x=121.5, width=121.5, height=45)

    s = Label(cadr,font=('vazir',15,'bold'), text="00", relief="ridge", bg="light blue")                
    s.place(y=45, x=243, width=121.5, height=45)

    ss = Label(cadr,font=('vazir',15,'bold'), text="00", relief="ridge", bg="light blue")                
    ss.place(y=45, x=364.5, width=121.5, height=45)

    def second_go():
        global mode, reset_m
        hour = int(h["text"])
        minute = int(m["text"])
        second = int(s["text"])
        s_second = int(ss["text"])
        if not reset_m:
            if mode=="go":
                if s_second <= 100:
                    s_second += 1
                    if s_second == 100:
                        s_second = 0
                        second += 1
                        second_t = str(second)
                        if len(str(second)) == 1:
                            second_t = f"0{second}"
                        s.config(text=second_t)
                        ss.config(text="00")
                        if second == 60:
                            second = 0
                            minute += 1
                            minute_t = str(minute)
                            if len(str(minute)) == 1:
                                minute_t = f"0{minute}"
                            m.config(text=minute_t)
                            s.config(text="00")
                            if minute == 60:
                                minute = 0
                                hour += 1
                                hour_t = str(hour)
                                if len(str(hour)) == 1:
                                    hour_t = f"0{hour}"
                                h.config(text=hour_t)
                                m.config(text="00")
                    s_second_t = str(s_second)
                    if len(str(s_second)) == 1:
                        s_second_t = f"0{s_second}"
                    ss.config(text=s_second_t)

            stopwatch.after(10, second_go)
        else:
            start_b.place(x=0, y=100, width=486, height=45)
            stop_b.place_forget()
            reset_b.place_forget()
            lap_b.place_forget()
            laps.place_forget()
            sb_list.place_forget()
            reset_m = False

    def start():
        global mode
        mode = "go"
        start_b.place_forget()
        stop_b.place(x=0, y=100, width=242, height=45)
        reset_b.place(x=244, y=100, width=242, height=45)
        lap_b.place(x=0, y=150, width=486, height=45)
        laps.place(x=130, y=200, height=200, width=200)
        sb_list.place(x=328, y=200, height=200)
        second_go()

    def stop():
        global mode
        stop_b.place_forget()
        cont_b.place(x=0, y=100, width=242, height=45)
        mode = "stop"

    def cont():
        global mode
        cont_b.place_forget()
        stop_b.place(x=0, y=100, width=242, height=45)
        mode = "go"

    def reset():
        global reset_m
        reset_m = True
        h.config(text="0")
        m.config(text="00")
        s.config(text="00")
        ss.config(text="00")
        laps.delete(0, END)

    def lap():
        hour = h["text"]
        minute = m["text"]
        second = s["text"]
        s_second = ss["text"]
        laps.insert(END, f"{hour}:{minute}:{second}:{s_second}")

    start_b = Button(cadr, text="شروع", bg="light blue", font=('vazir',15,'bold'), command=start)
    start_b.place(x=0, y=100, width=486, height=45)

    stop_b = Button(cadr, text="توقف", bg="light blue", font=('vazir',15,'bold'), command=stop)
    cont_b = Button(cadr, text="ادامه", bg="light blue", font=('vazir',15,'bold'), command=cont)
    reset_b = Button(cadr, text="بازنشانی", bg="light blue", font=('vazir',15,'bold'), command=reset)

    lap_b = Button(cadr, text="ثبت", bg="light blue", font=('vazir',15,'bold'), command=lap)

    laps = Listbox(cadr, bg="light blue", fg="#01ab8c", font=("vazir", 12)) 

    sb_list = Scrollbar(cadr)

    laps.configure(yscrollcommand=sb_list.set)
    sb_list.configure(command=laps.yview)
    
    stopwatch.mainloop()