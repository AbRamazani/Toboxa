from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageFilter, ImageTk, ExifTags

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
        self.canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set, xscrollcommand=xscrollbar.set, width=kw.get("width"), height=kw.get("height"))
        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=self.canvas.yview)
        xscrollbar.config(command=self.canvas.xview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(self.canvas)
        interior_id = self.canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            self.canvas.config(scrollregion="0 0 %s %s" % size)
        interior.bind('<Configure>', _configure_interior)

def open_filter_i_page(pre_page):
    pre_page.destroy()
    filter_i = Tk()
    filter_i.config(bg="light blue")
    filter_i.title("Toboxa=>put filter for image")
    filter_i.geometry("650x600+50+50")
    filter_i.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/image/filter-image_icon.png")

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
            filter_i.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            filter_i.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(filter_i, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(filter_i, width=150, height=600, bg="#01ab8c")

    def home():
        filter_i.destroy()
        from Toboxa import home
        home()

    def crop_i():
        from crop_image import open_crop_i_page
        open_crop_i_page(filter_i)

    def resize_i():
        from resize_image import open_resize_i_page
        open_resize_i_page(filter_i)

    def format_i():
        from format_image import open_format_i_page
        open_format_i_page(filter_i)

    def rotate_i():
        from rotate_image import open_rotate_i_page
        open_rotate_i_page(filter_i)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="بُرش تصویر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=crop_i).place(x=0, y=65)
    Button(hamburgar_menu, text="تغییر اندازه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=resize_i).place(x=0, y=100)
    Button(hamburgar_menu, text="تغییر پسوند", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=format_i).place(x=0, y=135)
    Button(hamburgar_menu, text="چرخاندن تصویر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=rotate_i).place(x=0, y=170)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn Medium", 15), command=filter_i.destroy).place(x=0, y=550)

    # title and img
    Label(filter_i, image=img, bg="light blue").place(x=150, y=0)
    Label(filter_i, text="قراردادن فیلتر", bg="light blue", justify="center", font=("Vazirmatn Medium", 35, "bold")).place(x=325, y=0)

    # categories

    cadr = Frame(filter_i, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
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
        img_p.title(f"Toboxa=>put filter for image=>{path.split('/')[-1]}")
        img_p.resizable(width=False, height=False)
        photo = fix_rotate(Image.open(path))
        ta = photo.height / photo.width
        n_h = photo.height / 400
        hn = round(photo.height / n_h)
        wn = round(hn / ta)
        photo1 = ImageTk.PhotoImage(image=photo.resize((wn, hn)))
        img_filter = Label(img_p, image=photo1, bd=0)
        img_filter.pack()
        photo.resize((round(wn*n_h), round(hn*n_h)))

        filters = VerticalScrolledFrame(img_p, width=0, height=0)
        filters.pack(pady=8)

        global mode_filter
        mode_filter = ""

        def filter_show(mode):
            global mode_filter
            ta = photo.height / photo.width
            n_h = photo.height / 400
            hn = round(photo.height / n_h)
            wn = round(hn / ta)
            mode_filter = mode
            filter_img = photo.resize((wn, hn))
            global img
            img = ImageTk.PhotoImage(filter_img.filter(mode_filter))
            img_filter.config(image=img)
            render.pack()

        ta = photo.height / photo.width
        n_h = photo.height / 100
        hn = round(photo.height / n_h)
        wn = round(hn / ta)
        img_resize = photo.resize((wn, hn))
        blur = ImageTk.PhotoImage(img_resize.filter(ImageFilter.BLUR))
        contour = ImageTk.PhotoImage(img_resize.filter(ImageFilter.CONTOUR))
        detail = ImageTk.PhotoImage(img_resize.filter(ImageFilter.DETAIL))
        edge_enhance = ImageTk.PhotoImage(img_resize.filter(ImageFilter.EDGE_ENHANCE))
        edge_enhance_more = ImageTk.PhotoImage(img_resize.filter(ImageFilter.EDGE_ENHANCE_MORE))
        emboss = ImageTk.PhotoImage(img_resize.filter(ImageFilter.EMBOSS))
        fine_edges = ImageTk.PhotoImage(img_resize.filter(ImageFilter.FIND_EDGES))
        smooth = ImageTk.PhotoImage(img_resize.filter(ImageFilter.SMOOTH))
        smooth_more = ImageTk.PhotoImage(img_resize.filter(ImageFilter.SMOOTH_MORE))
        sharpen = ImageTk.PhotoImage(img_resize.filter(ImageFilter.SHARPEN))
        Button(filters.interior, image=blur, bd=0, command=lambda: filter_show(ImageFilter.BLUR)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=contour, bd=0, command=lambda: filter_show(ImageFilter.CONTOUR)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=detail, bd=0, command=lambda: filter_show(ImageFilter.DETAIL)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=edge_enhance, bd=0, command=lambda: filter_show(ImageFilter.EDGE_ENHANCE)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=edge_enhance_more, bd=0, command=lambda: filter_show(ImageFilter.EDGE_ENHANCE_MORE)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=emboss, bd=0, command=lambda: filter_show(ImageFilter.EMBOSS)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=fine_edges, bd=0, command=lambda: filter_show(ImageFilter.FIND_EDGES)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=smooth, bd=0, command=lambda: filter_show(ImageFilter.SMOOTH)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=smooth_more, bd=0, command=lambda: filter_show(ImageFilter.SMOOTH_MORE)).pack(side=LEFT, padx=5)
        Button(filters.interior, image=sharpen, bd=0, command=lambda: filter_show(ImageFilter.SHARPEN)).pack(side=LEFT, padx=5)

        def filter_image():
            global mode_filter
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن تصویر",
            initialdir="/",
            filetypes=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))),
            defaultextension=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))))
            if file_name_out != "":
                filtered = photo.filter(mode_filter)
                if file_name_out.name.split(".")[-1] == "jpg" or file_name_out.name.split(".")[-1] == "jpeg":
                    filtered.convert("RGB").save(file_name_out.name)
                else:
                    filtered.save(file_name_out.name)
                img_p.destroy()
                messagebox.showinfo("ذخیره کردن تصویر", ".تصویر با موفقیت ذخیره شد")

        render = Button(img_p, text="انجام", bg="light blue", font=("Vazirmatn Medium", 15, "bold"), command=filter_image)

        img_p.update()
        filters.canvas.config(width=img_p.winfo_width(), height=100)
        
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

    filter_i.mainloop()