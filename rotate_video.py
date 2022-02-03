from tkinter import *
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk
import cv2

def open_rotate_v_page(pre_page):
    pre_page.destroy()
    rotate_v = Tk()
    rotate_v.config(bg="light blue")
    rotate_v.title("Toboxa=>rotate video")
    rotate_v.geometry("650x600+50+50")
    rotate_v.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/video/rotation_icon.png")

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
            rotate_v.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            rotate_v.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(rotate_v, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(rotate_v, width=150, height=600, bg="#01ab8c")

    def home():
        rotate_v.destroy()
        from Toboxa import home
        home()

    def crop_v():
        from crop_video import open_crop_v_page
        open_crop_v_page(rotate_v)

    def format_v():
        from format_video import open_format_v_page
        open_format_v_page(rotate_v)

    def merge_v():
        from merge_video import open_merge_v_page
        open_merge_v_page(rotate_v)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir bold", 15)).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="برش ویدئو", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=crop_v).place(x=0, y=65)
    Button(hamburgar_menu, text="تغییر پسوند", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=format_v).place(x=0, y=100)
    Button(hamburgar_menu, text="ادغام ویدئوها", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=merge_v).place(x=0, y=135)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=rotate_v.destroy).place(x=0, y=550)

    # title and img
    Label(rotate_v, image=img, bg="light blue").place(x=150, y=0)
    Label(rotate_v, text="چرخاندن ویدئو", bg="light blue", justify="center", font=("vazir bold", 35)).place(x=325, y=0)

    # categories

    cadr = Frame(rotate_v, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    def open_vid_page(path):
        vid_p = Toplevel()
        vid_p.config(bg="light blue")
        vid_p.title(f"Toboxa=>rotate video=>{path.split('/')[-1]}")
        vid_p.resizable(width=False, height=False)
        vid_p.geometry("600x400")
        Label(vid_p, text="توجه : تصویر زیر تنها برای نمایش خروجی است و خروجی با کیفیت اصلی ذخیره می شود", bg="light blue", font=("vazir bold", 10), fg="red").pack()

        vidcap = cv2.VideoCapture(path)
        success,image = vidcap.read()
        img_path = f"{path[:-(len(path.split('.')[-1])+1)]}.jpg"
        cv2.imwrite(img_path, image)

        global first_frame
        first_frame = ImageTk.PhotoImage(image=Image.open(img_path).resize((400, 200)))
        img_rotate = Label(vid_p, image=first_frame, bd=0)
        img_rotate.pack()

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
                r_i = Image.open(img_path).resize((400, 200)).rotate(v)    
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

        Label(vid_p, text="میزان چرخش(پادساعتگرد)", bg="light blue", font=("vazir bold", 14)).pack()

        rotate_val = IntVar(value=360)
        rotate_s = Spinbox(vid_p, font=("vazir bold", 15), textvariable=rotate_val, from_=1, to=360, wrap=True, command=rotate_show)
        rotate_s.pack()

        rotate_s.bind("<Key>", rotate_show)

        rotate_right = PhotoImage(file="files/images/image/rotate_right.png")
        Button(vid_p, image=rotate_right, bd=0, bg="light blue", command=lambda: rotate_90(270)).pack(side=RIGHT, anchor=NE)

        rotate_left = PhotoImage(file="files/images/image/rotate_left.png")
        Button(vid_p, image=rotate_left, bd=0, bg="light blue", command=lambda: rotate_90(90)).pack(side=LEFT, anchor=NW)


        def rotate():
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن ویدئو",
                initialdir="/",
                filetypes=(("MP4 files", "*.mp4"), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")),
                defaultextension=(("MP4 files", "*.mp4"), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")))
            if file_name_out != None:    
                film = VideoFileClip(path)                       
                if file_name_out.name.split(".")[-1] == "mp4":
                    codec_f = 'libx264'
                elif file_name_out.name.split(".")[-1] == "mov":
                    codec_f = 'mpeg4'
                elif file_name_out.name.split(".")[-1] == "wmv":
                    codec_f = 'libx264'
                elif file_name_out.name.split(".")[-1] == "avi":
                    codec_f = 'png'
                audio_path = f"{file_name_out.name[:-(len(file_name_out.name.split('.')[-1])+1)]}.mp3"
                rotate_v.title("Toboxa=>rotate video=>processing...")
                vid_p.title(f"Toboxa=>rotate video=>{path.split('/')[-1]}=>processing...")
                film.audio.write_audiofile(audio_path)
                film = film.rotate(rotate_val.get())
                film.write_videofile(file_name_out.name, codec=codec_f, audio=audio_path)
                rotate_v.title("Toboxa=>rotate video")
                vid_p.destroy()
                messagebox.showinfo("ذخیره کردن ویدئو", ".ویدئو با موفقیت ذخیره شد")

        render = Button(vid_p, text="انجام", bg="light blue", font=("vazir bold", 15), command=rotate).pack()

        vid_p.mainloop()

    def open_vid():
        file_name = filedialog.askopenfilename(title="باز کردن ویدئو",
        initialdir="/",
        filetypes=(("All videos", ("*.mp4", "*.mov", "*.wmv", "*.avi")), ("MP4 files", ("*.mp4")), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")))
        if file_name != "":
            open_vid_page(file_name)
       
    select = PhotoImage(file="files/images/image/select_image.png")
    Button(cadr, image=select, bg="light blue", bd=0, activebackground="light blue", command=open_vid).place(x=150, y=0)
    Button(cadr, text="انتخاب ویدئو", bg="light blue", font=("vazir bold", 17), bd=0, activebackground="light blue", command=open_vid).place(x=185, y=200)

    rotate_v.mainloop()