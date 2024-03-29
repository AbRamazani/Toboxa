from tkinter import *
from tkinter import filedialog, messagebox
from video_class import Video
from moviepy.editor import VideoFileClip

def open_crop_v_page(pre_page):
    pre_page.destroy()
    crop_v = Tk()
    crop_v.config(bg="light blue")
    crop_v.title("Toboxa=>cut video")
    crop_v.geometry("650x600+50+50")
    crop_v.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/video/crop_icon.png")

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
            crop_v.after(10, open_hamburger)

    def close_hamburger():
        global mak_ham
        if mak_ham == -150:
            hamburger_b.config(image=hamburger_img)
        if mak_ham >= -150:
            hamburger_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            crop_v.after(10, close_hamburger)

    hamburger_img = PhotoImage(file="files/images/root/menu.png")
    hamburger_b = Button(crop_v, image=hamburger_img, bg="light blue", bd=0, command=open_hamburger)
    hamburger_b.place(x=0, y=0)

    hamburger_menu = Frame(crop_v, width=150, height=600, bg="#01ab8c")

    def home():
        crop_v.destroy()
        from Toboxa import home
        home()

    def format_v():
        from format_video import open_format_v_page
        open_format_v_page(crop_v)

    def rotate_v():
        from rotate_video import open_rotate_v_page
        open_rotate_v_page(crop_v)

    def merge_v():
        from merge_video import open_merge_v_page
        open_merge_v_page(crop_v)

    Label(hamburger_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburger_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburger).place(x=125, y=0)
    Button(hamburger_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburger_menu, text="تغییر پسوند", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=format_v).place(x=0, y=65)
    Button(hamburger_menu, text="چرخاندن ویدئو", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=rotate_v).place(x=0, y=100)
    Button(hamburger_menu, text="ادغام ویدئوها", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=merge_v).place(x=0, y=135)
    Button(hamburger_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=crop_v.destroy).place(x=0, y=550)

    # title and img
    Label(crop_v, image=img, bg="light blue").place(x=150, y=0)
    Label(crop_v, text="برش ویدئو", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=325, y=0)

    # categories

    cadr = Frame(crop_v, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    def open_vid_page(path):
        vid_p = Toplevel()
        vid_p.config(bg="light blue")
        vid_p.title(f"Toboxa=>cut video=>{path.split('/')[-1]}")
        vid_p.resizable(width=False, height=False)
        vid_p.geometry("538x600")

        v = Video(vid_p, path)

        Label(vid_p, text="شروع و پایان برش(ثانیه)", bg="light blue", font=("Vazirmatn", 14, "bold")).pack(pady=30)

        start = IntVar(value=0)
        start_b = Spinbox(vid_p, font=("Vazirmatn", 15, "bold"), textvariable=start, from_=0, to=v.vid_player.duration(), wrap=True)
        start_b.pack()

        end = IntVar(value=v.vid_player.duration())
        end_b = Spinbox(vid_p, font=("Vazirmatn", 15, "bold"), textvariable=end, from_=0, to=v.vid_player.duration(), wrap=True)
        end_b.pack()
        
        def end_set(e):
            if end_b["to"] == 0:
                end_b.config(to=v.vid_player.duration())
                end_b.config(from_=1)
                start_b.config(to=v.vid_player.duration()-1)
                end.set(int(str(v.vid_player.duration()).split(".")[0]))
            if v.progress_slider["to"] == 0:
                v.progress_slider["to"] = v.vid_player.duration()
            if v.vid_player.current_duration() <= v.vid_player.duration():
                v.progress_slider.set(v.vid_player.current_duration())

        v.vid_player.bind("<<SecondChanged>>", end_set)

        def crop():
            try:
                start_time = start.get()
                end_time = end.get()
                if start_time <= end_time-1 and start_time >= 0 and end_time <= v.vid_player.duration():
                    file_name_out = filedialog.asksaveasfile(title="ذخیره کردن ویدئو",
                    initialdir="/",
                    filetypes=(("MP4 files", "*.mp4"), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")),
                    defaultextension=(("MP4 files", "*.mp4"), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")))
                    if file_name_out != None:    
                        film = VideoFileClip(path)                       
                        film = film.subclip(start_time, end_time)
                        if file_name_out.name.split(".")[-1] == "mp4":
                            codec_f = 'libx264'
                        elif file_name_out.name.split(".")[-1] == "mov":
                            codec_f = 'mpeg4'
                        elif file_name_out.name.split(".")[-1] == "wmv":
                            codec_f = 'libx264'
                        elif file_name_out.name.split(".")[-1] == "avi":
                            codec_f = 'png'
                        audio_path = False
                        crop_v.title("Toboxa=>cut video=>processing...")
                        vid_p.title(f"Toboxa=>cut video=>{path.split('/')[-1]}=>processing...")
                        if film.audio != None:
                            audio_path = f"{file_name_out.name[:-(len(file_name_out.name.split('.')[-1])+1)]}.mp3"
                            film.audio.write_audiofile(audio_path)
                        film.write_videofile(file_name_out.name, codec=codec_f, audio=audio_path)
                        crop_v.title("Toboxa=>cut video")
                        vid_p.destroy()
                        messagebox.showinfo("ذخیره کردن ویدئو", ".ویدئو با موفقیت ذخیره شد")
                else:
                    messagebox.showerror("خطا در ذخیره کردن ویدئو", "مقادیر وارد شده اشتباه می باشند")
            except:
                messagebox.showerror("خطا در ذخیره کردن ویدئو", "مقادیر وارد شده اشتباه می باشند")

        Button(vid_p, text="انجام", bg="light blue", font=("Vazirmatn", 15, "bold"), command=crop).pack()

        vid_p.mainloop()

    def open_vid():
        file_name = filedialog.askopenfilename(title="باز کردن ویدئو",
        initialdir="/",
        filetypes=(("All videos", ("*.mp4", "*.mov", "*.wmv", "*.avi")), ("MP4 files", ("*.mp4")), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")))
        if file_name != "":
            open_vid_page(file_name)
       
    select = PhotoImage(file="files/images/image/select_image.png")
    Button(cadr, image=select, bg="light blue", bd=0, activebackground="light blue", command=open_vid).place(x=150, y=0)
    Button(cadr, text="انتخاب ویدئو", bg="light blue", font=("Vazirmatn", 17, "bold"), bd=0, activebackground="light blue", command=open_vid).place(x=185, y=200)

    crop_v.mainloop()
