from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ExifTags

def open_resize_i_page(pre_page):
    pre_page.destroy()
    resize_i = Tk()
    resize_i.config(bg="light blue")
    resize_i.title("Toboxa=>resize image")
    resize_i.geometry("650x600+50+50")
    resize_i.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/image/resizing_icon.png")

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
            resize_i.after(10, open_hamburger)

    def close_hamburger():
        global mak_ham
        if mak_ham == -150:
            hamburger_b.config(image=hamburger_img)
        if mak_ham >= -150:
            hamburger_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            resize_i.after(10, close_hamburger)

    hamburger_img = PhotoImage(file="files/images/root/menu.png")
    hamburger_b = Button(resize_i, image=hamburger_img, bg="light blue", bd=0, command=open_hamburger)
    hamburger_b.place(x=0, y=0)

    hamburger_menu = Frame(resize_i, width=150, height=600, bg="#01ab8c")

    def home():
        resize_i.destroy()
        from Toboxa import home
        home()

    def crop_i():
        from crop_image import open_crop_i_page
        open_crop_i_page(resize_i)

    def format_i():
        from format_image import open_format_i_page
        open_format_i_page(resize_i)

    def rotate_i():
        from rotate_image import open_rotate_i_page
        open_rotate_i_page(resize_i)

    def filter_i():
        from filter_image import open_filter_i_page
        open_filter_i_page(resize_i)

    Label(hamburger_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburger_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburger).place(x=125, y=0)
    Button(hamburger_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburger_menu, text="بُرش تصویر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=crop_i).place(x=0, y=65)
    Button(hamburger_menu, text="تغییر پسوند", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=format_i).place(x=0, y=100)
    Button(hamburger_menu, text="چرخاندن تصویر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=rotate_i).place(x=0, y=135)
    Button(hamburger_menu, text="قراردادن فیلتر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=filter_i).place(x=0, y=170)
    Button(hamburger_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=resize_i.destroy).place(x=0, y=550)

    # title and img
    Label(resize_i, image=img, bg="light blue").place(x=150, y=0)
    Label(resize_i, text="تغییر اندازه", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=350, y=0)

    # categories

    cadr = Frame(resize_i, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    def fix_rotate(image):
        try:
            for orientation in ExifTags.TAGS.keys() : 
                if ExifTags.TAGS[orientation]=='Orientation' : break 
            exif=dict(image._getexif().items())

            if   exif[orientation] == 3 : 
                image=image.rotate(180, expand=True)
            elif exif[orientation] == 6 : 
                image=image.rotate(270, expand=True)
            elif exif[orientation] == 8 : 
                image=image.rotate(90, expand=True)
        except:
            pass
        return image

    def open_img_page(path):
        img_p = Toplevel()
        img_p.config(bg="light blue")
        img_p.title(f"Toboxa=>resize image=>{path.split('/')[-1]}")
        img_p.resizable(width=False, height=False)
        photo = fix_rotate(Image.open(path))
        ta = photo.height / photo.width
        n_h = photo.height / 400
        hn = round(photo.height / n_h)
        wn = round(hn / ta)
        photo1 = ImageTk.PhotoImage(image=photo.resize((wn, hn)))
        img_resize = Label(img_p, image=photo1, bd=0)
        img_resize.pack()
        photo.resize((round(wn*n_h), round(hn*n_h)))

        def set_proportional_h(*args):
            w = w_value.get()
            if proportional.get():
                nes = int(photo1.width()) / int(photo1.height())
                h_value.set(round(w/nes))

        def set_proportional_w(*args):
            h = h_value.get()
            if proportional.get():
                nes = int(photo1.height()) / int(photo1.width())
                w_value.set(round(h/nes))

        Label(img_p, text="عرض", bg="light blue", font=("Vazirmatn", 14, "bold")).pack()

        w_value = IntVar(value=int(photo.width))
        width = Spinbox(img_p, font=("Vazirmatn", 15, "bold"), textvariable=w_value, from_=1, to=999999999999, wrap=True, command=set_proportional_h)
        width.pack()

        Label(img_p, text="ارتفاع", bg="light blue", font=("Vazirmatn", 14, "bold")).pack()

        h_value = IntVar(value=int(photo.height))
        height = Spinbox(img_p, font=("Vazirmatn", 15, "bold"), textvariable=h_value, from_=1, to=999999999999, wrap=True, command=set_proportional_w)
        height.pack()

        def set_proportional_h_b(e):
            try:
                if e.char == "\x08":
                    insert_p = int(width.index(INSERT))
                    t = str(width.get())[:insert_p-1] + str(width.get())[insert_p:]
                    w_v = int(t)
                else:
                    w_v = int(str(width.get()) + e.char)

                if proportional.get():
                    nes = int(photo1.width()) / int(photo1.height())
                    h_value.set(round(w_v/nes))
            except:
                if e.char != "\x08":
                    messagebox.showerror("خطا", "عدد وارد شده اشتباه می باشد")

        def set_proportional_w_b(e):
            try:
                if e.char == "\x08":
                    insert_h = int(height.index(INSERT))
                    t = str(height.get())[:insert_h-1] + str(height.get())[insert_h:]
                    h_v = int(t)
                else:
                    h_v = int(str(h_value.get()) + e.char)

                if proportional.get():
                    nes = int(photo1.height()) / int(photo1.width())
                    w_value.set(round(h_v/nes))
            except:
                if e.char != "\x08":
                    messagebox.showerror("خطا", "عدد وارد شده اشتباه می باشد")
        
        width.bind("<Key>", set_proportional_h_b)
        height.bind("<Key>", set_proportional_w_b)

        proportional = IntVar()
        proportional_check = Checkbutton(img_p, text="حفظ تناسب ابعاد", variable=proportional, bg="light blue", font=("Vazirmatn", 15, "bold"))
        proportional_check.pack()

        def resize():
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن تصویر",
            initialdir="/",
            filetypes=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))),
            defaultextension=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))))
            if file_name_out != "":
                resizeped = photo.resize((w_value.get(), h_value.get()))
                if file_name_out.name.split(".")[-1] == "jpg" or file_name_out.name.split(".")[-1] == "jpeg":
                    resizeped.convert("RGB").save(file_name_out.name)
                else:
                    resizeped.save(file_name_out.name)
                img_p.destroy()
                messagebox.showinfo("ذخیره کردن تصویر", ".تصویر با موفقیت ذخیره شد")

        s_b = Button(img_p, text="انجام", bg="light blue", font=("Vazirmatn", 12, "bold"), command=resize).pack(pady=7)

        img_p.mainloop()

    def open_img():
        file_name = filedialog.askopenfilename(title="باز کردن تصویر",
        initialdir="/",
        filetypes=(("All images", ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.tiff", "*.ico")), ("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", "*.ico")))
        if file_name != "":
            open_img_page(file_name)
    
    select = PhotoImage(file="files/images/image/select_image.png")
    Button(cadr, image=select, bg="light blue", command=open_img, bd=0, activebackground="light blue").place(x=150, y=0)
    Button(cadr, text="انتخاب تصویر", bg="light blue", font=("Vazirmatn", 17, "bold"), command=open_img, bd=0, activebackground="light blue").place(x=185, y=200)

    resize_i.mainloop()