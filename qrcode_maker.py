from tkinter import *
from tkinter import messagebox, filedialog
from pyqrcode import create

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        xscrollbar = Scrollbar(self, orient=HORIZONTAL)
        xscrollbar.pack(fill=X, side=BOTTOM, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set, xscrollcommand=xscrollbar.set, width=200, height=200)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)
        xscrollbar.config(command=canvas.xview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
        interior.bind('<Configure>', _configure_interior)

def open_qrcode_maker_page(pre_page):
    pre_page.destroy()
    qrcode_maker = Tk()
    qrcode_maker.config(bg="light blue")
    qrcode_maker.title("Toboxa=>QR code maker")
    qrcode_maker.geometry("650x600+50+50")
    qrcode_maker.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/other/qr-code_icon.png")

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
            qrcode_maker.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            qrcode_maker.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(qrcode_maker, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(qrcode_maker, width=150, height=600, bg="#01ab8c")

    def home():
        qrcode_maker.destroy()
        from Toboxa import home
        home()

    def timer():
        from timer import open_timer_page
        open_timer_page(qrcode_maker)

    def stopwatch():
        from stopwatch import open_stopwatch_page
        open_stopwatch_page(qrcode_maker)

    def net_speed():
        from net_speed import open_net_speed_page
        open_net_speed_page(qrcode_maker)

    def password_maker():
        from password_maker import open_password_maker_page
        open_password_maker_page(qrcode_maker)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir bold", 15)).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="تایمر", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=timer).place(x=0, y=65)
    Button(hamburgar_menu, text="کرنومتر", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=stopwatch).place(x=0, y=100)
    Button(hamburgar_menu, text="سرعت اینترنت", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=net_speed).place(x=0, y=135)
    Button(hamburgar_menu, text="تولیدکننده رمز", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=password_maker).place(x=0, y=170)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=qrcode_maker.destroy).place(x=0, y=550)

    # title and img
    Label(qrcode_maker, image=img, bg="light blue").place(x=150, y=0)
    Label(qrcode_maker, text="QR code تولیدکننده", bg="light blue", justify="center", font=("vazir bold", 30)).place(x=305, y=15)

    # categories

    cadr = Frame(qrcode_maker, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    def make_qrcode():
        text = text_qr.get("1.0", END)
        global img, qr
        qr = create(text, encoding="utf-8")
        img = BitmapImage(data = qr.xbm(scale=5))
        img_lbl.config(image = img)
        f_s.place(x=135, y=170)
        save.place(x=50, y=390, height=40)
    
    def save_qrcode():
        global qr
        file_name_out = filedialog.asksaveasfile(title="ذخیره کردن تصویر",
            initialdir="/",
            filetypes=(("PNG files", "*.png"), ("SVG files", "*.svg")),
            defaultextension=(("PNG files", "*.png"), ("SVG files", "*.svg")))
        if file_name_out != None:
            if file_name_out.name.split(".")[-1] == "png":
                qr.png(file_name_out.name, scale = 8)
            elif file_name_out.name.split(".")[-1] == "svg":
                qr.svg(file_name_out.name, scale = 8)
            messagebox.showinfo("ذخیره کردن تصویر", ".تصویر با موفقیت ذخیره شد")

    text_qr = Text(cadr, font=("vazir bold", 13), width=42, bg="light yellow")
    text_qr.place(x=35, y=5, height=100)    
    scroll = Scrollbar(cadr, command=text_qr.yview, orient='vertical')
    scroll.place(x=20, y=6, height=100)
    text_qr["yscrollcommand"] = scroll.set

    Button(cadr, text="بساز", bg="light blue", font=("vazir bold", 15), width=35, command=make_qrcode).place(x=50, y=110)

    f_s = VerticalScrolledFrame(cadr)
    img_lbl = Label(f_s.interior, bg="light blue", font=("vazir bold", 13))
    img_lbl.pack()

    save = Button(cadr, text="ذخیره", bg="light blue", font=("vazir", 14), width=35, command=save_qrcode)

    qrcode_maker.mainloop()