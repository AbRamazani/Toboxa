from tkinter import *
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip
from video_class import Video

def open_merge_v_page(pre_page):
    pre_page.destroy()
    merge_v = Tk()
    merge_v.config(bg="light blue")
    merge_v.title("Toboxa=>merge videos")
    merge_v.geometry("650x600+50+50")
    merge_v.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/video/paste-video_icon.png")

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
            merge_v.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            merge_v.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(merge_v, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(merge_v, width=150, height=600, bg="#01ab8c")

    def home():
        merge_v.destroy()
        from Toboxa import home
        home()

    def crop_v():
        from crop_video import open_crop_v_page
        open_crop_v_page(merge_v)

    def format_v():
        from format_video import open_format_v_page
        open_format_v_page(merge_v)

    def rotate_v():
        from rotate_video import open_rotate_v_page
        open_rotate_v_page(merge_v)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir bold", 15)).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="برش ویدئو", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=crop_v).place(x=0, y=65)
    Button(hamburgar_menu, text="تغییر پسوند", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=format_v).place(x=0, y=100)
    Button(hamburgar_menu, text="چرخاندن ویدئو", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=rotate_v).place(x=0, y=135)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("vazir", 15), command=merge_v.destroy).place(x=0, y=550)

    # title and img
    Label(merge_v, image=img, bg="light blue").place(x=150, y=0)
    Label(merge_v, text="ادغام ویدئوها", bg="light blue", justify="center", font=("vazir bold", 35)).place(x=325, y=0)

    # categories

    cadr = Frame(merge_v, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    def open_vid_page(path):
        vid_p = Toplevel()
        vid_p.config(bg="light blue")
        vid_p.title(f"Toboxa=>merge videos=>{path.split('/')[-1]}")
        vid_p.resizable(width=False, height=False)
        vid_p.geometry("600x400")
        
        v = Video(vid_p, path)

        def end_set(e):
            if v.progress_slider["to"] == 0:
                v.progress_slider["to"] = v.vid_player.duration()
            if v.vid_player.current_duration() <= v.vid_player.duration():
                v.progress_slider.set(v.vid_player.current_duration())

        v.vid_player.bind("<<SecondChanged>>", end_set)

        vid_p.mainloop()

    def merge():
        videos_chose = list(videos.get(0, END))
        if len(videos_chose) > 1:
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن ویدئو",
            initialdir="/",
            filetypes=(("MP4 files", "*.mp4"), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")),
            defaultextension=(("MP4 files", "*.mp4"), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")))
            if file_name_out != None:    
                videos_mo = []
                c = 0
                for video in videos_chose:
                    videos_mo.insert(c, VideoFileClip(video))
                    c += 1
                if file_name_out.name.split(".")[-1] == "mp4":
                    codec_f = 'libx264'
                elif file_name_out.name.split(".")[-1] == "mov":
                    codec_f = 'mpeg4'
                elif file_name_out.name.split(".")[-1] == "wmv":
                    codec_f = 'libx264'
                elif file_name_out.name.split(".")[-1] == "avi":
                    codec_f = 'png'
                audio_path = f"{file_name_out.name[:-(len(file_name_out.name.split('.')[-1])+1)]}.mp3"
                merge_v.title("Toboxa=>merge video=>processing...")
                final = concatenate_videoclips(videos_mo, method='compose')
                final.audio.write_audiofile(audio_path, fps=44100)
                final.write_videofile(file_name_out.name, codec=codec_f, audio=audio_path)
                merge_v.title("Toboxa=>merge video")
                messagebox.showinfo("ذخیره کردن ویدئو", ".ویدئو با موفقیت ذخیره شد")
                open_vid_page(file_name_out.name)
        else:
            messagebox.showwarning("مشکل در ادغام", ".برای ادغام حداقل دو ویدئو را انتخاب کنید")

    def select_vid():
        delete_b.place_forget()
        file_name = filedialog.askopenfilename(title="باز کردن ویدئو",
        initialdir="/",
        filetypes=(("All videos", ("*.mp4", "*.mov", "*.wmv", "*.avi")), ("MP4 files", ("*.mp4")), ("MOV files", "*.mov"), ("WMV files", "*.wmv"), ("AVI files", "*.avi")))
        if file_name != "":
            videos.insert(END, file_name)
    
    Label(cadr, text="توجه : ترتیب ادغام ویدئو ها بر اساس ترتیبی است که شما انتخاب می کنید", bg="light blue", font=("vazir bold", 10), fg="red").place(x=50, y=0)

    def show_delete(e):
        if videos.get(0, END) != ():
            index = videos.curselection()[0]
            delete_b.config(command=lambda: delete_vid(index))
            delete_b.place(x=370, y=55.5)

    def delete_vid(index):
        videos.delete(index)
        delete_b.place_forget()

    videos = Listbox(cadr, bg="light blue", fg="#01ab8c", font=("vazir", 12))
    videos.place(x=150, y=30, height=100, width=200)

    videos.bind("<<ListboxSelect>>", show_delete)

    sb_list = Scrollbar(cadr)
    sb_list.place(x=348, y=30, height=100)

    videos.configure(yscrollcommand=sb_list.set)
    sb_list.configure(command=videos.yview)

    delete = PhotoImage(file="files/images/video/delete.png")
    delete_b = Button(cadr, image=delete, bg="light blue", bd=0, activebackground="light blue")

    select = PhotoImage(file="files/images/image/select_image.png")
    Button(cadr, image=select, bg="light blue", bd=0, activebackground="light blue", command=select_vid).place(x=150, y=135)
    Button(cadr, text="ادغام ویدئو ها", bg="light blue", font=("vazir bold", 17), bd=0, activebackground="light blue", command=merge).place(x=180, y=336)

    merge_v.mainloop()