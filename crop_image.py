from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ExifTags
from tkVideoPlayer import TkinterVideo
import datetime

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
                        yscrollcommand=vscrollbar.set, xscrollcommand=xscrollbar.set, width=600, height=500)
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

def open_crop_i_page(pre_page):
    pre_page.destroy()
    crop_i = Tk()
    crop_i.config(bg="light blue")
    crop_i.title("Toboxa=>crop image")
    crop_i.geometry("650x600+50+50")
    crop_i.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/image/crop_icon.png")

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
            crop_i.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            crop_i.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(crop_i, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(crop_i, width=150, height=600, bg="#01ab8c")

    def home():
        crop_i.destroy()
        from Toboxa import home
        home()

    def resize_i():
        from resize_image import open_resize_i_page
        open_resize_i_page(crop_i)

    def format_i():
        from format_image import open_format_i_page
        open_format_i_page(crop_i)

    def rotate_i():
        from rotate_image import open_rotate_i_page
        open_rotate_i_page(crop_i)

    def filter_i():
        from filter_image import open_filter_i_page
        open_filter_i_page(crop_i)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn bold", 15)).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="تغییر اندازه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=resize_i).place(x=0, y=65)
    Button(hamburgar_menu, text="تغییر پسوند", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=format_i).place(x=0, y=100)
    Button(hamburgar_menu, text="چرخاندن تصویر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=rotate_i).place(x=0, y=135)
    Button(hamburgar_menu, text="قراردادن فیلتر", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=filter_i).place(x=0, y=170)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=crop_i.destroy).place(x=0, y=550)

    # title and img
    Label(crop_i, image=img, bg="light blue").place(x=150, y=0)
    Label(crop_i, text="برش تصویر", bg="light blue", justify="center", font=("Vazirmatn bold", 35)).place(x=350, y=0)

    # categories

    cadr = Frame(crop_i, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
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
        img_p.resizable(width=False, height=False)
        img_p.config(bg="light blue")
        img_p.title(f"Toboxa=>crop image=>{path.split('/')[-1]}")
        photo = fix_rotate(Image.open(path))
        photo1 = ImageTk.PhotoImage(image=photo)

        if int(photo1.height()) > img_p.winfo_screenheight()-100 or int(photo1.width()) > img_p.winfo_screenwidth()-100:
            img_f = VerticalScrolledFrame(img_p)
            img_f.pack()

            img_crop = Label(img_f.interior, image=photo1, bd=0)
            img_crop.pack()
        else:
            img_crop = Label(img_p, image=photo1, bd=0)
            img_crop.pack()

        top_l = Label(img_crop, bg="red")
        top_l.place(x=0, y=0, width=photo1.width(), height=5)

        right_l = Label(img_crop, bg="blue")
        right_l.place(x=photo1.width()-5, y=0, width=5, height=photo1.height())

        left_l = Label(img_crop, bg="green")
        left_l.place(x=0, y=0, width=5, height=photo1.height())

        bellow_l =Label(img_crop, bg="yellow")
        bellow_l.place(x=0, y=photo1.height()-5, width=photo1.width(), height=5)

        global color
        color = None

        def set_color(color_s):
            global color
            color = color_s

        def con():
            t_l_i = int(top_l.place_info()["y"])
            r_l_i = int(right_l.place_info()["x"])
            l_l_i = int(left_l.place_info()["x"])
            b_l_i = int(bellow_l.place_info()["y"])

            top_l.place_forget()
            right_l.place_forget()
            left_l.place_forget()
            bellow_l.place_forget()

            top_l.place(x=0, y=t_l_i, width=photo1.width(), height=5)
            right_l.place(x=r_l_i, y=0, width=5, height=photo1.height())
            left_l.place(x=l_l_i, y=0, width=5, height=photo1.height())
            bellow_l.place(x=0, y=b_l_i, width=photo1.width(), height=5)

        def change_pmo(e):
            global color
            if color == "red":
                if int(top_l.place_info()["y"])+1 < int(bellow_l.place_info()["y"]):
                    top_l.place_configure(y=int(top_l.place_info()["y"])+1)
                    con()
            elif color == "blue":
                if int(right_l.place_info()["x"])+1 < photo1.width():
                    right_l.place_configure(x=int(right_l.place_info()["x"])+1)
                    con()
            elif color == "green":
                if int(left_l.place_info()["x"])+1 < int(right_l.place_info()["x"]):
                    left_l.place_configure(x=int(left_l.place_info()["x"])+1)
                    con()
            elif color == "yellow":
                if int(bellow_l.place_info()["y"])+1 < photo1.height():
                    bellow_l.place_configure(y=int(bellow_l.place_info()["y"])+1)
                    con()

        def change_pma(e):
            global color
            if color == "red":
                if int(top_l.place_info()["y"])-1 > 0:
                    top_l.place_configure(y=int(top_l.place_info()["y"])-1)
                    con()
            elif color == "blue":
                if int(right_l.place_info()["x"])-1 > int(left_l.place_info()["x"]):
                    right_l.place_configure(x=int(right_l.place_info()["x"])-1)
                    con()
            elif color == "green":
                if int(left_l.place_info()["x"])-1 > 0:
                    left_l.place_configure(x=int(left_l.place_info()["x"])-1)
                    con()
            elif color == "yellow":
                if int(bellow_l.place_info()["y"])-1 > int(top_l.place_info()["y"]):
                    bellow_l.place_configure(y=int(bellow_l.place_info()["y"])-1)
                    con()

        def crop():
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن تصویر",
            initialdir="/",
            filetypes=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))),
            defaultextension=(("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", ("*.ico", "*.cur"))))
            if file_name_out != "":
                cropped = photo.crop((int(left_l.place_info()["x"])+5, int(top_l.place_info()["y"])+5, int(right_l.place_info()["x"]), int(bellow_l.place_info()["y"])))
                if file_name_out.name.split(".")[-1] == "jpg" or file_name_out.name.split(".")[-1] == "jpeg":
                    cropped.convert("RGB").save(file_name_out.name)
                else:
                    cropped.save(file_name_out.name)

                img_p.destroy()
                messagebox.showinfo("ذخیره کردن تصویر", ".تصویر با موفقیت ذخیره شد")

        def help_page():
            help_p = Toplevel()
            help_p.title("Toboxa=>crop image=>help")
            help_p.resizable(width=False, height=False)
            help_p.geometry("538x684")
            help_p.config(bg="light blue")

            Label(help_p, text="ویدئوی آموزش بُرش زدن تصویر", bg="light blue", font=("Vazirmatn bold", 15)).pack()
            def update_duration(event):
                """ updates the duration after finding the duration """
                end_time["text"] = str(datetime.timedelta(seconds=vid_player.duration())).split(".")[0]
                progress_slider["to"] = vid_player.duration()


            def update_scale(event):
                """ updates the scale value """
                progress_slider.set(vid_player.current_duration())
                start_time["text"] = str(datetime.timedelta(seconds=vid_player.current_duration())).split(".")[0]


            def seek(value):
                """ used to seek a specific timeframe """
                vid_player.seek(int(value))
                start_time["text"] = str(datetime.timedelta(seconds=vid_player.current_duration())).split(".")[0]
                vid_player.play()
                if int(value) < 85:
                    play_pause_btn["text"] = "توقف"
                else:
                    play_pause_btn["text"] = "پخش"


            def skip(value: int):
                """ skip seconds """
                vid_player.skip_sec(value)
                progress_slider.set(progress_slider.get() + value)
                start_time["text"] = str(datetime.timedelta(seconds=vid_player.current_duration())).split(".")[0]


            def play_pause():
                """ pauses and plays """
                if vid_player.is_paused():
                    vid_player.play()
                    play_pause_btn["text"] = "توقف"

                else:
                    vid_player.pause()
                    play_pause_btn["text"] = "پخش"


            def video_ended(event):
                """ handle video ended """
                progress_slider.set(progress_slider["to"])
                play_pause_btn["text"] = "پخش"

            vid_player = TkinterVideo(scaled=True, pre_load=False, master=help_p)
            vid_player.load(r"files/videos/root/help crop.mp4")
            vid_player.pack(expand=True, fill="both")

            vid_player.play()

            play_pause_btn = Button(help_p, text="توقف", bg="light blue", font=("Vazirmatn"), command=play_pause)
            play_pause_btn.pack()

            skip_plus_5sec = Button(help_p, text="پنج ثانیه قبل", bg="light blue", font=("Vazirmatn"), command=lambda: skip(-5))
            skip_plus_5sec.pack(side="left")

            start_time = Label(help_p, text=str(datetime.timedelta(seconds=0)), bg="light blue", font=("Vazirmatn"))
            start_time.pack(side="left")

            progress_slider = Scale(help_p, from_=0, to=vid_player.duration(), orient="horizontal", command=seek, bg="light blue", font=("Vazirmatn"))
            progress_slider.pack(side="left", fill="x", expand=True)
            
            end_time = Label(help_p, text=str(datetime.timedelta(seconds=vid_player.duration())).split(".")[0], bg="light blue", font=("Vazirmatn"))
            end_time.pack(side="left")

            vid_player.bind("<<Duration>>", update_duration)
            vid_player.bind("<<SecondChanged>>", update_scale)
            vid_player.bind("<<Ended>>", video_ended )

            skip_plus_5sec = Button(help_p, text="پنج ثانیه بعد", bg="light blue", font=("Vazirmatn"), command=lambda: skip(5))
            skip_plus_5sec.pack(side="left")

            help_p.mainloop()

        c_b = Button(img_p, text="انجام", bg="light blue", font=("Vazirmatn bold", 12), command=crop)
        c_b.pack(pady=25)
        h_b = Button(img_p, text="راهنما", bg="light blue", font=("Vazirmatn bold", 11), command=help_page)
        h_b.pack()

        img_p.update()
        page_width = img_p.winfo_width()
        if int(photo1.height()) > img_p.winfo_screenheight()-100 or int(photo1.width()) > img_p.winfo_screenwidth()-100:
            img_height = 520
        else:
            img_height = int(photo1.height())

        w_bs = page_width/4

        Button(img_p, bg="red", command=lambda: set_color("red"), text="بالا", font=("Vazirmatn bold", 10)).place(x=w_bs*3, y=img_height+1.5, width=w_bs, height=20)
        Button(img_p, bg="blue", command=lambda: set_color("blue"), text="راست", font=("Vazirmatn bold", 10)).place(x=w_bs*2, y=img_height+1.5, width=w_bs, height=20)
        Button(img_p, bg="green", command=lambda: set_color("green"), text="چپ", font=("Vazirmatn bold", 10)).place(x=w_bs, y=img_height+1.5, width=w_bs, height=20)
        Button(img_p, bg="yellow", command=lambda: set_color("yellow"), text="پایین", font=("Vazirmatn bold", 10)).place(x=2, y=img_height+1.5, width=w_bs, height=20)

        img_p.bind("<Up>", change_pmo)
        img_p.bind("<Down>", change_pma)

        img_p.mainloop()

    def open_img():
        file_name = filedialog.askopenfilename(title="باز کردن تصویر",
        initialdir="/",
        filetypes=(("All images", ("*.jpg", "*.jpeg", "*.png", "*.webp", "*.tiff", "*.ico")), ("JPG files", ("*.jpg", "*.jpeg")), ("PNG files", "*.png"), ("WebP files", "*.webp"), ("TIFF files", "*.tiff"), ("ICO files", "*.ico")))
        if file_name != "":
            open_img_page(file_name)

    select = PhotoImage(file="files/images/image/select_image.png")
    Button(cadr, image=select, bg="light blue", command=open_img, bd=0, activebackground="light blue").place(x=150, y=0)
    Button(cadr, text="انتخاب تصویر", bg="light blue", font=("Vazirmatn bold", 17), command=open_img, bd=0, activebackground="light blue").place(x=185, y=200)

    crop_i.mainloop()