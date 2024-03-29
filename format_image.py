from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ExifTags

def open_format_i_page(pre_page):
    pre_page.destroy()
    format_i = Tk()
    format_i.config(bg="light blue")
    format_i.title("Toboxa=>change image format")
    format_i.geometry("650x600+50+50")
    format_i.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/image/format-image_icon.png")

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
            format_i.after(10, open_hamburger)

    def close_hamburger():
        global mak_ham
        if mak_ham == -150:
            hamburger_b.config(image=hamburger_img)
        if mak_ham >= -150:
            hamburger_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            format_i.after(10, close_hamburger)

    hamburger_img = PhotoImage(file="files/images/root/menu.png")
    hamburger_b = Button(format_i, image=hamburger_img, bg="light blue", bd=0, command=open_hamburger)
    hamburger_b.place(x=0, y=0)

    hamburger_menu = Frame(format_i, width=150, height=600, bg="#01ab8c")

    def home():
        format_i.destroy()
        from Toboxa import home
        home()

    def crop_i():
        from crop_image import open_crop_i_page
        open_crop_i_page(format_i)

    def resize_i():
        from resize_image import open_resize_i_page
        open_resize_i_page(format_i)

    def rotate_i():
        from rotate_image import open_rotate_i_page
        open_rotate_i_page(format_i)

    def filter_i():
        from filter_image import open_filter_i_page
        open_filter_i_page(format_i)

    Label(hamburger_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburger_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburger).place(x=125, y=0)
    Button(hamburger_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburger_menu, text="بُرش تصویر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=crop_i).place(x=0, y=65)
    Button(hamburger_menu, text="تغییر اندازه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=resize_i).place(x=0, y=100)
    Button(hamburger_menu, text="چرخاندن تصویر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=rotate_i).place(x=0, y=135)
    Button(hamburger_menu, text="قراردادن فیلتر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=filter_i).place(x=0, y=170)
    Button(hamburger_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=format_i.destroy).place(x=0, y=550)

    # title and img
    Label(format_i, image=img, bg="light blue").place(x=150, y=0)
    Label(format_i, text="تغییر پسوند", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=350, y=0)

    # categories

    cadr = Frame(format_i, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    global types_s
    types_o = (('BMP files', '*.bmp'), ('DDS files', '*.dds'), ('DIB files', '*.dib'), ('ICNS files', '*.icns'), ('ICO files', '*.ico'), ('IM files', '*.im'), ('JPEG files', ('*.jpg', '*.jpeg')), ('PCX files', '*.pcx'), ('PNG files', '*.png'), ('PPM files', '*.ppm'), ('SGI files', '*.sgi'), ('TGA files', '*.tga'), ('TIFF files', '*.tiff'), ('WebP files', '*.webp'))
    types_s = (('BMP files', '*.bmp'), ('DDS files', '*.dds'), ('DIB files', '*.dib'), ('ICNS files', '*.icns'), ('ICO files', '*.ico'), ('IM files', '*.im'), ('JPEG files', ('*.jpg', '*.jpeg')), ('PCX files', '*.pcx'), ('PNG files', '*.png'), ('PPM files', '*.ppm'), ('SGI files', '*.sgi'), ('TGA files', '*.tga'), ('TIFF files', '*.tiff'), ('WebP files', '*.webp'))
    types_c = ('BMP files(.bmp)', 'DDS files(.dds)', 'DIB files(.dib)', 'ICNS files(.icns)', 'ICO files(.ico)', 'IM files(.im)', 'JPEG files(.jpg , .jpeg)', 'PCX files(.pcx)', 'PNG files(.png)', 'PPM files(.ppm)', 'SGI files(.sgi)', 'TGA files(.tga)', 'TIFF files(.tiff)', 'WebP files(.webp)')

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
        img_p.title(f"Toboxa=>change image format=>{path.split('/')[-1]}")
        img_p.resizable(width=False, height=False)
        photo = fix_rotate(Image.open(path))
        ta = photo.height / photo.width
        n_h = photo.height / 400
        hn = round(photo.height / n_h)
        wn = round(hn / ta)
        photo1 = ImageTk.PhotoImage(image=photo.resize((wn, hn)))
        img_format = Label(img_p, image=photo1, bd=0)
        img_format.pack()
        photo.resize((round(wn*n_h), round(hn*n_h)))

        format_now = Label(img_p, text=f"{path.split('/')[-1].split('.')[-1]} : پسوند کنونی", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()

        format_to = Label(img_p, text=": تبدیل به", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()

        to_format = StringVar()
        to_format_cadr = ttk.Combobox(img_p, textvariable=to_format, values=types_c, state="readonly", justify="center", font=("Vazirmatn", 10, "bold"))
        to_format_cadr.pack()

        def change_combo(e):
            global types_s
            select = to_format.get().split("(")[-1][:-1].split(" , ")
            if select[0] == ".jpg":
                now = [("JPEG files", ("*.jpg", "*.jpeg"))]
            else:
                now = [(f"{select[0][1:].upper()} files", f"*{select[0]}")]

            types_s = now
            render.pack(pady=5)

        to_format_cadr.bind("<<ComboboxSelected>>", change_combo)

        def change_format():
            global types_s
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن تصویر",
            initialdir="/",
            filetypes=types_s,
            defaultextension=types_s)
            if file_name_out != "":
                if file_name_out.name.split(".")[-1] == "jpg" or file_name_out.name.split(".")[-1] == "jpeg":
                    p_c_rgb = photo.convert("RGB")
                else:
                    p_c_rgb = photo
                p_c_rgb.save(file_name_out.name)
                img_p.destroy()
                messagebox.showinfo("ذخیره کردن تصویر", ".تصویر با موفقیت ذخیره شد")

        render = Button(img_p, text="انجام", bg="light blue", font=("Vazirmatn", 15, "bold"), command=change_format)

        img_p.mainloop()

    def open_img():        
        file_name = filedialog.askopenfilename(title="باز کردن تصویر",
        initialdir="/",
        filetypes=types_o)
        if file_name != "":
            open_img_page(file_name)
    
    select = PhotoImage(file="files/images/image/select_image.png")
    Button(cadr, image=select, bg="light blue", command=open_img, bd=0, activebackground="light blue").place(x=150, y=0)
    Button(cadr, text="انتخاب تصویر", bg="light blue", font=("Vazirmatn", 17, "bold"), command=open_img, bd=0, activebackground="light blue").place(x=185, y=200)

    format_i.mainloop()