from tkinter import *
from tkinter import filedialog, messagebox, ttk
from moviepy.editor import VideoFileClip
import os

def open_format_v_page(pre_page):
    pre_page.destroy()
    format_v = Tk()
    format_v.config(bg="light blue")
    format_v.title("Toboxa=>change video format")
    format_v.geometry("650x600+50+50")
    format_v.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/video/format-film_icon.png")

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
            format_v.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            format_v.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(format_v, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(format_v, width=150, height=600, bg="#01ab8c")

    def home():
        format_v.destroy()
        from Toboxa import home
        home()

    def crop_v():
        from crop_video import open_crop_v_page
        open_crop_v_page(format_v)

    def rotate_v():
        from rotate_video import open_rotate_v_page
        open_rotate_v_page(format_v)

    def merge_v():
        from merge_video import open_merge_v_page
        open_merge_v_page(format_v)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="برش ویدئو", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=crop_v).place(x=0, y=65)
    Button(hamburgar_menu, text="چرخاندن ویدئو", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=rotate_v).place(x=0, y=100)
    Button(hamburgar_menu, text="ادغام ویدئوها", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=merge_v).place(x=0, y=135)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=format_v.destroy).place(x=0, y=550)

    # title and img
    Label(format_v, image=img, bg="light blue").place(x=150, y=0)
    Label(format_v, text="تغییر پسوند", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=325, y=0)

    # categories

    cadr = Frame(format_v, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    global types_s
    types_s = (("MP4 files", "*.mp4"), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi"), ("MKV files", "*.mkv"), ("WebM files", "*.webm"), ("FLV files", "*.flv"), ("OGV files", "*.ogv"))
    types_c = ("MP4 files(.mp4)", "MOV files(.mov)", "WMV files(.wmv)", "AVI files(.avi)", "MKV files(.mkv)", "WebM files(.webm)", "FLV files(.flv)", "OGV files(.ogv)")

    def open_vid_page(path):
        vid_p = Toplevel()
        vid_p.config(bg="light blue")
        vid_p.title(f"Toboxa=>change video format=>{path.split('/')[-1]}")
        vid_p.resizable(width=False, height=False)
        vid_p.geometry("600x400")

        video_detail = Frame(vid_p, width=600, height=200, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
        video_detail.pack(pady=5)

        details = LabelFrame(video_detail, text="اطلاعات فایل", bg="light blue", font=("Vazirmatn", 15, "bold"), height=180)
        details.pack(side="right", pady=10, padx=5)

        def convert_time(seconds):
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            return "%d:%02d:%02d" % (hours, minutes, seconds)

        def convert_size(bytes):
            if bytes < 1000:
                bytes = f"{bytes} بایت"
            elif 1000 <= bytes < 1000000:
                bytes = f"{round(bytes/1000, 2)} کیلوبایت"
            elif 1000000 <= bytes < 1000000000:
                bytes = f"{round(bytes/1000000, 2)} مگابایت"
            else:
                bytes = f"{round(bytes/1000000000, 2)} گیگابایت"
            return bytes

        file_name = Label(details, text=f"{path.split('/')[-1]} : نام فایل", font=("Vazirmatn", 14, "bold"), bg="light blue").pack()
        file_size = Label(details, text=f"حجم فایل : {convert_size(os.path.getsize(path))}", font=("Vazirmatn", 12), bg="light blue").pack()
        file_time = Label(details, text=f"{convert_time(VideoFileClip(path).duration)} : زمان فایل", font=("Vazirmatn", 12), bg="light blue").pack()

        f_img = PhotoImage(file=f"files/images/video/formats/{path.split('/')[-1].split('.')[-1]}.png")
        format_img = Label(video_detail, image=f_img, bg="light blue").pack(side="left", padx=5)

        format_now = Label(vid_p, text=f"{path.split('/')[-1].split('.')[-1]} : پسوند کنونی", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()

        format_to = Label(vid_p, text=": تبدیل به", bg="light blue", font=("Vazirmatn", 15, "bold")).pack()

        to_format = StringVar()
        to_format_cadr = ttk.Combobox(vid_p, textvariable=to_format, values=types_c, state="readonly", justify="center", font=("Vazirmatn", 10, "bold"))
        to_format_cadr.pack()

        def change_combo(e):
            global types_s
            select = to_format.get().split("(")[-1][:-1].split(" , ")
            
            now = [(f"{select[0][1:].upper()} files", f"*{select[0]}")]

            types_s = now
            render.pack(pady=5)

        to_format_cadr.bind("<<ComboboxSelected>>", change_combo)

        def format():
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن ویدئو",
            initialdir="/",
            filetypes=types_s,
            defaultextension=types_s)
            if file_name_out != None:    
                film = VideoFileClip(path)                       
                audio_f = "mp3"
                if file_name_out.name.split(".")[-1] == "mp4":
                    codec_f = 'libx264'
                elif file_name_out.name.split(".")[-1] == "mov":
                    codec_f = 'mpeg4'
                elif file_name_out.name.split(".")[-1] == "wmv":
                    codec_f = 'libx264'
                elif file_name_out.name.split(".")[-1] == "avi":
                    codec_f = 'png'
                elif file_name_out.name.split(".")[-1] == "mkv":
                    codec_f = 'libx264'
                elif file_name_out.name.split(".")[-1] == "webm":
                    codec_f = 'libvpx'
                    audio_f = "ogg"
                elif file_name_out.name.split(".")[-1] == "flv":
                    codec_f = 'libx264'
                elif file_name_out.name.split(".")[-1] == "ogv":
                    codec_f = 'libtheora'
                    audio_f = "ogg"

                audio_path = False
                format_v.title("Toboxa=>change video format=>processing...")
                vid_p.title(f"Toboxa=>change video format=>{path.split('/')[-1]}=>processing...")
                if film.audio != None:
                    audio_path = f"{file_name_out.name[:-(len(file_name_out.name.split('.')[-1])+1)]}.{audio_f}"
                    film.audio.write_audiofile(audio_path)
                film.write_videofile(file_name_out.name, codec=codec_f, audio=audio_path)
                format_v.title("Toboxa=>change video format")
                vid_p.destroy()
                messagebox.showinfo("ذخیره کردن ویدئو", ".ویدئو با موفقیت ذخیره شد")

        render = Button(vid_p, text="انجام", bg="light blue", font=("Vazirmatn", 15, "bold"), command=format)

        vid_p.mainloop()

    def open_vid():
        file_name = filedialog.askopenfilename(title="باز کردن ویدئو",
        initialdir="/",
        filetypes=(("All videos", ("*.mp4", "*.mov", "*.wmv", "*.avi", "*.mkv", "*.webm", "*.flv", "*.ogv")), ("MP4 files", "*.mp4"), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi"), ("MKV files", "*.mkv"), ("WebM files", "*.webm"), ("FLV files", "*.flv"), ("OGV files", "*.ogv")))
        if file_name != "":
            open_vid_page(file_name)
       
    select = PhotoImage(file="files/images/image/select_image.png")
    Button(cadr, image=select, bg="light blue", bd=0, activebackground="light blue", command=open_vid).place(x=150, y=0)
    Button(cadr, text="انتخاب ویدئو", bg="light blue", font=("Vazirmatn", 17, "bold"), bd=0, activebackground="light blue", command=open_vid).place(x=185, y=200)

    format_v.mainloop()
