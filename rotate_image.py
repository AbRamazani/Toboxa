from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ExifTags

def open_rotate_i_page(pre_page):
    pre_page.destroy()
    rotate_i = Tk()
    rotate_i.config(bg="light blue")
    rotate_i.title("Toboxa=>rotate image")
    rotate_i.geometry("650x600+50+50")
    rotate_i.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/image/rotation_icon.png")

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
            rotate_i.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            rotate_i.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(rotate_i, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(rotate_i, width=150, height=600, bg="#01ab8c")

    def home():
        rotate_i.destroy()
        from Toboxa import home
        home()

    def crop_i():
        from crop_image import open_crop_i_page
        open_crop_i_page(rotate_i)

    def resize_i():
        from resize_image import open_resize_i_page
        open_resize_i_page(rotate_i)

    def format_i():
        from format_image import open_format_i_page
        open_format_i_page(rotate_i)

    def filter_i():
        from filter_image import open_filter_i_page
        open_filter_i_page(rotate_i)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="بُرش تصویر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=crop_i).place(x=0, y=65)
    Button(hamburgar_menu, text="تغییر اندازه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=resize_i).place(x=0, y=100)
    Button(hamburgar_menu, text="تغییر پسوند", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=format_i).place(x=0, y=135)
    Button(hamburgar_menu, text="قراردادن فیلتر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=filter_i).place(x=0, y=170)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=rotate_i.destroy).place(x=0, y=550)

    # title and img
    Label(rotate_i, image=img, bg="light blue").place(x=150, y=0)
    Label(rotate_i, text="چرخاندن تصویر", bg="light blue", justify="center", font=("Vazirmatn Medium", 35, "bold")).place(x=315, y=0)

    # categories

    cadr = Frame(rotate_i, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
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
        img_p.title(f"Toboxa=>rotate image=>{path.split('/')[-1]}")
        img_p.resizable(width=False, height=False)
        photo = fix_rotate(Image.open(path))
        ta = photo.height / photo.width
        n_h = photo.height / 400
        hn = round(photo.height / n_h)
        wn = round(hn / ta)
        photo1 = ImageTk.PhotoImage(image=photo.resize((wn, hn)))
        Label(img_p, text="توجه : تصویر زیر تنها برای نمایش خروجی است و خروجی با کیفیت اصلی ذخیره می شود", bg="light blue", font=("Vazirmatn Medium", 10, "bold"), fg="red").pack()
        img_rotate = Label(img_p, image=photo1, bd=0)
        img_rotate.pack()
        photo.resize((round(wn*n_h), round(hn*n_h)))

        def z_360(val):
            r = val
            if val > 360:
                r = val - 360
            return r

        def rotate_show(e = None):
            try:
                if e != None:
                    if e.char == "\x08":
                        insert_p = int(rotate_s.index(INSERT))
                        t = str(rotate_s.get())[:insert_p-1] + str(rotate_s.get())[insert_p:]
                        v = int(t)
                    else:
                        v = int(str(rotate_s.get()) + e.char)
                else:
                    v = rotate_val.get()
                ta = photo.height / photo.width
                n_h = photo.height / 400
                hn = round(photo.height / n_h)
                wn = round(hn / ta)
                r_i = photo.resize((wn, hn)).rotate(v)    
                global img
                img = ImageTk.PhotoImage(r_i)
                img_rotate.config(image=img)
            except:
                if e.char != "\x08":
                    messagebox.showerror("خطا", "عدد وارد شده اشتباه می باشد")

        def rotate_90(val):
            rotate_value = z_360(rotate_val.get()+val)
            rotate_val.set(rotate_value)
            rotate_show()

        Label(img_p, text="میزان چرخش(پادساعتگرد)", bg="light blue", font=("Vazirmatn Medium", 14, "bold")).pack()

        rotate_val = IntVar(value=360)
        rotate_s = Spinbox(img_p, font=("Vazirmatn Medium", 15, "bold"), textvariable=rotate_val, from_=1, to=360, wrap=True, command=rotate_show)
        rotate_s.pack()

        rotate_s.bind("<Key>", rotate_show)

        rotate_right = PhotoImage(file="files/images/image/rotate_right.png")
        Button(img_p, image=rotate_right, bd=0, bg="light blue", command=lambda: rotate_90(270)).pack(side=RIGHT, anchor=NE)

        rotate_left = PhotoImage(file="files/images/image/rotate_left.png")
        Button(img_p, image=rotate_left, bd=0, bg="light blue", command=lambda: rotate_90(90)).pack(side=LEFT, anchor=NW)

        def rotate_image():
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن تصویر",
            initialdir="/",
            filetypes=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))),
            defaultextension=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))))
            if file_name_out != "":
                rotated = photo.rotate(rotate_val.get(), resample=Image.BICUBIC, expand=True)
                if file_name_out.name.split(".")[-1] == "jpg" or file_name_out.name.split(".")[-1] == "jpeg":
                    rotated.convert("RGB").save(file_name_out.name)
                else:
                    rotated.save(file_name_out.name)
                img_p.destroy()
                messagebox.showinfo("ذخیره کردن تصویر", ".تصویر با موفقیت ذخیره شد")

        def option_pro():
            img_p.destroy()
            pro_p = Toplevel()
            pro_p.config(bg="light blue")
            pro_p.title(f"Toboxa=>flip image=>{path.split('/')[-1]}")
            pro_p.resizable(width=False, height=False)
            photo = fix_rotate(Image.open(path))
            ta = photo.height / photo.width
            n_h = photo.height / 400
            hn = round(photo.height / n_h)
            wn = round(hn / ta)
            photo1 = ImageTk.PhotoImage(image=photo.resize((wn, hn)))
            Label(pro_p, text="توجه : تصویر زیر تنها برای نمایش خروجی است و خروجی با کیفیت اصلی ذخیره می شود", bg="light blue", font=("Vazirmatn Medium", 10, "bold"), fg="red").pack()
            img_flip = Label(pro_p, image=photo1, bd=0)
            img_flip.pack()
            photo.resize((round(wn*n_h), round(hn*n_h)))
            global flip
            flip = ""

            def change_flip(chose):
                global flip
                flip = chose
                ta = photo.height / photo.width
                n_h = photo.height / 400
                hn = round(photo.height / n_h)
                wn = round(hn / ta)
                img_f = photo.resize((wn, hn)).transpose(chose)
                global img
                img = ImageTk.PhotoImage(img_f)
                img_flip.config(image=img)
                f_v.pack_forget()
                f_h.pack_forget()
                render.pack(side=RIGHT, padx=5, fill=X, expand=True, pady=10)
                back.pack(side=RIGHT, padx=5, fill=X, expand=True, pady=10)

            def flip_image():
                global types_s
                file_name_out = filedialog.asksaveasfile(title="ذخیره کردن تصویر",
                initialdir="/",
                filetypes=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))),
                defaultextension=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))))
                if file_name_out != "":
                    flipped = photo.transpose(flip)
                    if file_name_out.name.split(".")[-1] == "jpg" or file_name_out.name.split(".")[-1] == "jpeg":
                        flipped.convert("RGB").save(file_name_out.name)
                    else:
                        flipped.save(file_name_out.name)
                    pro_p.destroy()
                    messagebox.showinfo("ذخیره کردن تصویر", ".تصویر با موفقیت ذخیره شد")

            def back_chose():
                img_flip.config(image=photo1)
                render.pack_forget()
                back.pack_forget()
                f_v.pack(side=RIGHT, padx=5, fill=X, expand=True, pady=10)
                f_h.pack(side=RIGHT, padx=5, fill=X, expand=True, pady=10)

            f_v = Button(pro_p, text="قرینه عمودی", bg="light blue", font=("Vazirmatn Medium", 15, "bold"), command=lambda: change_flip(Image.FLIP_TOP_BOTTOM))
            f_v.pack(side=RIGHT, padx=5, fill=X, expand=True, pady=10)
            f_h = Button(pro_p, text="قرینه افقی", bg="light blue", font=("Vazirmatn Medium", 15, "bold"), command=lambda: change_flip(Image.FLIP_LEFT_RIGHT))
            f_h.pack(side=RIGHT, padx=5, fill=X, expand=True, pady=10)

            render = Button(pro_p, text="انجام", bg="light blue", font=("Vazirmatn Medium", 15, "bold"), command=flip_image)
            back = Button(pro_p, text="بازگشت", bg="light blue", font=("Vazirmatn Medium", 15, "bold"), command=back_chose)

            pro_p.mainloop()

        Button(img_p, text="انجام", bg="light blue", font=("Vazirmatn Medium", 15, "bold"), command=rotate_image).pack()
        Button(img_p, text="گزینه های پیشرفته", bg="light blue", font=("Vazirmatn Medium", 15, "bold"), command=option_pro).pack(pady=10)

        img_p.mainloop()

    def open_img():        
        file_name = filedialog.askopenfilename(title="باز کردن تصویر",
        initialdir="/",
        filetypes=(("All images", ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.tiff", "*.ico")), ("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", "*.ico")))
        if file_name != "":
            open_img_page(file_name)
    
    select = PhotoImage(file="files/images/image/select_image.png")
    Button(cadr, image=select, bg="light blue", command=open_img, bd=0, activebackground="light blue").place(x=150, y=0)
    Button(cadr, text="انتخاب تصویر", bg="light blue", font=("Vazirmatn Medium", 17, "bold"), command=open_img, bd=0, activebackground="light blue").place(x=185, y=200)

    rotate_i.mainloop()