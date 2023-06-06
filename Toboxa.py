from tkinter import *
from pyglet import font

# math pages
from area import open_area_page
from date import open_date_page
from calculator import open_calculator_page
from unit_math import open_unit_math_page

# programming pages
from lorem import open_lorem_page
from compress import open_compress_page
from text_editor import open_texte_page

# image pages
from crop_image import open_crop_i_page
from resize_image import open_resize_i_page
from format_image import open_format_i_page
from rotate_image import open_rotate_i_page
from filter_image import open_filter_i_page

# video pages
from crop_video import open_crop_v_page
from format_video import open_format_v_page
from rotate_video import open_rotate_v_page
from merge_video import open_merge_v_page

# other pages
from timer import open_timer_page
from stopwatch import open_stopwatch_page
from net_speed import open_net_speed_page
from password_maker import open_password_maker_page
from qrcode_maker import open_qrcode_maker_page

font.add_file("files/font/Vazirmatn.ttf")

def home():
    root = Tk()
    root.config(bg="light blue")
    root.title("Toboxa")
    img = PhotoImage(file="files/images/root/Toboxa.png")
    root.iconphoto(True, img)
    root.geometry("650x600+50+50")
    root.resizable(width=False, height=False)

    # hamburgar menu
    global mak_ham, math_mak, programming_mak, image_mak, video_mak, other_mak, about_mak
    mak_ham = -150
    def open_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(bd=0, image="")
        if mak_ham <= 0:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham += 1
            root.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            root.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(root, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(root, width=150, height=600, bg="#01ab8c")

    # open pages

    def open_home():
        global math_mak, programming_mak, image_mak, video_mak, other_mak, about_mak
        math_page.place_forget()
        if math_mak == 151:
            math_mak -= 496
        programming_page.place_forget()
        if programming_mak == 151:
            programming_mak -= 496
        image_page.place_forget()
        if image_mak == 151:
            image_mak -= 496
        video_page.place_forget()
        if video_mak == 151:
            video_mak -= 496
        other_page.place_forget()
        if other_mak == 151:
            other_mak -= 496
        about_page.place_forget()
        if about_mak == 151:
            about_mak -= 496

    math_mak = -345
    def open_math():
        global math_mak, programming_mak, image_mak, video_mak, other_mak, about_mak
        if math_mak == 151 or math_mak == -345:
            programming_page.place_forget()
            if programming_mak == 151:
                programming_mak -= 496
            image_page.place_forget()
            if image_mak == 151:
                image_mak -= 496
            video_page.place_forget()
            if video_mak == 151:
                video_mak -= 496
            other_page.place_forget()
            if other_mak == 151:
                other_mak -= 496
            about_page.place_forget()
            if about_mak == 151:
                about_mak -= 496
        if math_mak <= 150:
            math_page.place(x=math_mak, y=200)
            math_mak += 1
            a = root.after(5, open_math)

            
    programming_mak = -345
    def open_programming():
        global programming_mak, image_mak, video_mak, other_mak, math_mak, about_mak
        if programming_mak == 151 or programming_mak == -345:
            math_page.place_forget()
            if math_mak == 151:
                math_mak -= 496
            image_page.place_forget()
            if image_mak == 151:
                image_mak -= 496
            video_page.place_forget()
            if video_mak == 151:
                video_mak -= 496
            other_page.place_forget()
            if other_mak == 151:
                other_mak -= 496
            about_page.place_forget()
            if about_mak == 151:
                about_mak -= 496
        if programming_mak <= 150:
            programming_page.place(x=programming_mak, y=200)
            programming_mak += 1
            root.after(5, open_programming)

    image_mak = -345
    def open_image():
        global programming_mak, image_mak, video_mak, other_mak, math_mak, about_mak
        if image_mak == 151 or image_mak == -345:
            math_page.place_forget()
            if math_mak == 151:
                math_mak -= 496
            programming_page.place_forget()
            if programming_mak == 151:
                programming_mak -= 496
            video_page.place_forget()
            if video_mak == 151:
                video_mak -= 496
            other_page.place_forget()
            if other_mak == 151:
                other_mak -= 496
            about_page.place_forget()
            if about_mak == 151:
                about_mak -= 496
        if image_mak <= 150:
            image_page.place(x=image_mak, y=200)
            image_mak += 1
            root.after(5, open_image)

    video_mak = -345
    def open_video():
        global programming_mak, image_mak, video_mak, other_mak, math_mak, about_mak
        if video_mak == 151 or video_mak == -345:
            math_page.place_forget()
            if math_mak == 151:
                math_mak -= 496
            programming_page.place_forget()
            if programming_mak == 151:
                programming_mak -= 496
            image_page.place_forget()
            if image_mak == 151:
                image_mak -= 496
            other_page.place_forget()
            if other_mak == 151:
                other_mak -= 496
            about_page.place_forget()
            if about_mak == 151:
                about_mak -= 496
        if video_mak <= 150:
            video_page.place(x=video_mak, y=200)
            video_mak += 1
            root.after(5, open_video)

    other_mak = -345
    def open_other():
        global programming_mak, image_mak, video_mak, other_mak, math_mak, about_mak
        if other_mak == 151 or other_mak == -345:
            math_page.place_forget()
            if math_mak == 151:
                math_mak -= 496
            programming_page.place_forget()
            if programming_mak == 151:
                programming_mak -= 496
            image_page.place_forget()
            if image_mak == 151:
                image_mak -= 496
            video_page.place_forget()
            if video_mak == 151:
                video_mak -= 496
            about_page.place_forget()
            if about_mak == 151:
                about_mak -= 496
        if other_mak <= 150:
            other_page.place(x=other_mak, y=200)
            other_mak += 1
            root.after(5, open_other)


    about_mak = -345
    def open_about():
        global programming_mak, image_mak, video_mak, other_mak, math_mak, about_mak
        if about_mak == 151 or about_mak == -345:
            math_page.place_forget()
            if math_mak == 151:
                math_mak -= 496
            programming_page.place_forget()
            if programming_mak == 151:
                programming_mak -= 496
            image_page.place_forget()
            if image_mak == 151:
                image_mak -= 496
            video_page.place_forget()
            if video_mak == 151:
                video_mak -= 496
            other_page.place_forget()
            if other_mak == 151:
                other_mak -= 496
        if about_mak <= 150:
            about_page.place(x=about_mak, y=200)
            about_mak += 1
            root.after(5, open_about)

    Label(hamburgar_menu, text="توبوکسا", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 17, "bold")).place(x=0, y=0, width=150, height=35)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=-7)
    Button(hamburgar_menu, text="خانه", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 16), command=open_home).place(x=0, y=45, width=150, height=35)
    Button(hamburgar_menu, text="ریاضی", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 16), command=open_math).place(x=0, y=80, width=150, height=35)
    Button(hamburgar_menu, text="برنامه نویسی", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 16), command=open_programming).place(x=0, y=115, width=150, height=35)
    Button(hamburgar_menu, text="تصویر", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 16), command=open_image).place(x=0, y=150, width=150, height=35)
    Button(hamburgar_menu, text="ویدئو", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 16), command=open_video).place(x=0, y=185, width=150, height=35)
    Button(hamburgar_menu, text="سایر", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 16), command=open_other).place(x=0, y=220, width=150, height=35)
    Button(hamburgar_menu, text="درباره من", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 16), command=open_about).place(x=0, y=255, width=150, height=35)
    Button(hamburgar_menu, text="خروج", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 17), command=root.destroy).place(x=0, y=550, width=150, height=50)

    # title and img
    Label(root, image=img, bg="light blue").place(x=150, y=0)
    Label(root, text="توبوکسا", bg="light blue", justify="center", font=("Vazirmatn", 57, "bold")).place(x=375, y=0)
    Label(root, text="جعبه ابزاری برای رایانه شما", bg="light blue", fg="#404040", justify="center", font=("Vazirmatn", 17, "bold")).place(x=365, y=110)

    # categories

    cadr = Frame(root, width=495, height=395, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=200)

    categories_title = Label(cadr, text="دسته بندی ها", bg="light blue", justify="center", font=("Vazirmatn", 25, "bold")).place(x=145, y=0)

    math_img = PhotoImage(file="files/images/root/math_icon.png")
    math = Button(cadr, image=math_img, bg="light blue", bd=0, activebackground="light blue", command=open_math)
    math_title = Button(cadr, text="ریاضی", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=open_math)
    math.place(x=340, y=50)
    math_title.place(x=365, y=180, height=30)

    programming_img = PhotoImage(file="files/images/root/programming_icon.png")
    programming = Button(cadr, image=programming_img, bg="light blue", bd=0, activebackground="light blue", command=open_programming)
    programming_title = Button(cadr, text="برنامه نویسی", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=open_programming)
    programming.place(x=170, y=55)
    programming_title.place(x=165, y=180, height=30)


    image_img = PhotoImage(file="files/images/root/image_icon.png")
    image = Button(cadr, image=image_img, bg="light blue", bd=0, activebackground="light blue", command=open_image)
    image_title = Button(cadr, text="تصویر", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=open_image)
    image.place(x=0, y=45)
    image_title.place(x=30, y=180, height=30)

    video_img = PhotoImage(file="files/images/root/video_icon.png")
    video = Button(cadr, image=video_img, bg="light blue", bd=0, activebackground="light blue", command=open_video)
    video_title = Button(cadr, text="ویدئو", bg="light blue", bd=-2, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=open_video)
    video.place(x=338, y=210)
    video_title.place(x=370, y=340, height=30)

    other_img = PhotoImage(file="files/images/root/other_icon.png")
    other = Button(cadr, image=other_img, bg="light blue", bd=0, activebackground="light blue", command=open_other)
    other_title = Button(cadr, text="سایر", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=open_other)
    other.place(x=170, y=220)
    other_title.place(x=180, y=340, height=30)

    #close icon:
    close_icon = PhotoImage(file="files/images/root/cancel_icon.png")

    # math parts:
    math_page = Frame(root, width=495, height=395, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    math_page_title = Label(math_page, text="ابزار های ریاضی", bg="light blue", justify="center", font=("Vazirmatn", 25, "bold")).place(x=135, y=0)
    Button(math_page, image=close_icon, bg="light blue", bd=0, activebackground="light blue", command=open_home).place(x=430, y=0)

    perimete_img = PhotoImage(file="files/images/math/select_icon.png")
    perimete = Button(math_page, image=perimete_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_area_page(root))
    perimete_title = Button(math_page, text="محاسبه مساحت", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 17, "bold"), command=lambda: open_area_page(root))
    perimete.place(x=340, y=50)
    perimete_title.place(x=315, y=180, height=30, width=170)

    date_img = PhotoImage(file="files/images/math/schedule_icon.png")
    date = Button(math_page, image=date_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_date_page(root))
    date_title = Button(math_page, text="تبدیل تاریخ", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_date_page(root))
    date.place(x=170, y=50)
    date_title.place(x=170, y=180, height=30)

    calculator_img = PhotoImage(file="files/images/math/calculator_icon.png")
    calculator = Button(math_page, image=calculator_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_calculator_page(root))
    calculator_title = Button(math_page, text="ماشین حساب", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_calculator_page(root))
    calculator.place(x=0, y=50)
    calculator_title.place(x=0, y=180, height=30, width=150)

    unit_math_img = PhotoImage(file="files/images/math/cost_icon.png")
    unit_math = Button(math_page, image=unit_math_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_unit_math_page(root))
    unit_math_title = Button(math_page, text="مبدل واحد", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_unit_math_page(root))
    unit_math.place(x=338, y=210)
    unit_math_title.place(x=345, y=345, height=30)

    # programming parts:
    programming_page = Frame(root, width=495, height=395, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    programming_page_title = Label(programming_page, text="ابزار های برنامه نویسی", bg="light blue", justify="center", font=("Vazirmatn", 25, "bold")).place(x=85, y=0)
    Button(programming_page, image=close_icon, bg="light blue", bd=0, activebackground="light blue", command=open_home).place(x=430, y=0)

    lorem_img = PhotoImage(file="files/images/programming/publishing_icon.png")
    lorem = Button(programming_page, image=lorem_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_lorem_page(root))
    lorem_title = Button(programming_page, text="لورم ساز", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_lorem_page(root))
    lorem.place(x=340, y=50)
    lorem_title.place(x=355, y=180, height=30)

    compress_img = PhotoImage(file="files/images/programming/compression_icon.png")
    compress = Button(programming_page, image=compress_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_compress_page(root))
    compress_title = Button(programming_page, text="فشرده‌سازی‌فایل‌‌وب", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 16, "bold"), command=lambda: open_compress_page(root))
    compress.place(x=170, y=50)
    compress_title.place(x=150, y=180, height=30)

    text_editor_img = PhotoImage(file="files/images/programming/text-editor_icon.png")
    text_editor = Button(programming_page, image=text_editor_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_texte_page(root))
    text_editor_title = Button(programming_page, text="ویرایشگر متن", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_texte_page(root))
    text_editor.place(x=5, y=50)
    text_editor_title.place(x=0, y=180, height=30)

    # image parts:
    image_page = Frame(root, width=495, height=395, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    image_page_title = Label(image_page, text="ابزار های تصویر", bg="light blue", justify="center", font=("Vazirmatn", 25, "bold")).place(x=130, y=0)
    Button(image_page, image=close_icon, bg="light blue", bd=0, activebackground="light blue", command=open_home).place(x=430, y=0)

    crop_i_img = PhotoImage(file="files/images/image/crop_icon.png")
    crop_i = Button(image_page, image=crop_i_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_crop_i_page(root))
    crop_i_title = Button(image_page, text="برش", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_crop_i_page(root))
    crop_i.place(x=340, y=50)
    crop_i_title.place(x=375, y=180, height=30)

    resize_i_img = PhotoImage(file="files/images/image/resizing_icon.png")
    resize_i = Button(image_page, image=resize_i_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_resize_i_page(root))
    resize_i_title = Button(image_page, text="تغییر اندازه", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_resize_i_page(root))
    resize_i.place(x=170, y=50)
    resize_i_title.place(x=170, y=180, height=30)

    foramt_i_img = PhotoImage(file="files/images/image/format-image_icon.png")
    foramt_i = Button(image_page, image=foramt_i_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_format_i_page(root))
    foramt_i_title = Button(image_page, text="تغییر پسوند", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_format_i_page(root))
    foramt_i.place(x=0, y=50)
    foramt_i_title.place(x=0, y=180, height=30)

    rotate_i_img = PhotoImage(file="files/images/image/rotation_icon.png")
    rotate_i = Button(image_page, image=rotate_i_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_rotate_i_page(root))
    rotate_i_title = Button(image_page, text="چرخاندن", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_rotate_i_page(root))
    rotate_i.place(x=338, y=210)
    rotate_i_title.place(x=350, y=340, height=30)

    filter_i_img = PhotoImage(file="files/images/image/filter-image_icon.png")
    filter_i = Button(image_page, image=filter_i_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_filter_i_page(root))
    filter_i_title = Button(image_page, text="قراردادن فیلتر", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_filter_i_page(root))
    filter_i.place(x=175, y=210)
    filter_i_title.place(x=170, y=340, height=30)

    # video parts:
    video_page = Frame(root, width=495, height=395, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    video_page_title = Label(video_page, text="ابزار های ویدئو", bg="light blue", justify="center", font=("Vazirmatn", 25, "bold")).place(x=150, y=0)
    Button(video_page, image=close_icon, bg="light blue", bd=0, activebackground="light blue", command=open_home).place(x=430, y=0)

    crop_v_img = PhotoImage(file="files/images/video/crop_icon.png")
    crop_v = Button(video_page, image=crop_v_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_crop_v_page(root))
    crop_v_title = Button(video_page, text="برش", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_crop_v_page(root))
    crop_v.place(x=340, y=50)
    crop_v_title.place(x=370, y=180, height=30)

    foramt_v_img = PhotoImage(file="files/images/video/format-film_icon.png")
    foramt_v = Button(video_page, image=foramt_v_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_format_v_page(root))
    foramt_v_title = Button(video_page, text="تغییر پسوند", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_format_v_page(root))
    foramt_v.place(x=170, y=50)
    foramt_v_title.place(x=170, y=180, height=30)

    rotate_v_img = PhotoImage(file="files/images/video/rotation_icon.png")
    rotate_v = Button(video_page, image=rotate_v_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_rotate_v_page(root))
    rotate_v_title = Button(video_page, text="چرخاندن", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_rotate_v_page(root))
    rotate_v.place(x=0, y=40)
    rotate_v_title.place(x=16, y=180, height=30)

    paste_v_img = PhotoImage(file="files/images/video/paste-video_icon.png")
    paste_v = Button(video_page, image=paste_v_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_merge_v_page(root))
    paste_v_title = Button(video_page, text="ادغام ویدئوها", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 18, "bold"), command=lambda: open_merge_v_page(root))
    paste_v.place(x=338, y=210)
    paste_v_title.place(x=325, y=345, height=30)

    # other parts:
    other_page = Frame(root, width=495, height=395, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    other_page_title = Label(other_page, text="سایر ابزار ها", bg="light blue", justify="center", font=("Vazirmatn", 20, "bold")).place(x=175, y=0)
    Button(other_page, image=close_icon, bg="light blue", bd=0, activebackground="light blue", command=open_home).place(x=430, y=0)

    timer_img = PhotoImage(file="files/images/other/timer_icon.png")
    timer = Button(other_page, image=timer_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_timer_page(root))
    timer_title = Button(other_page, text="تایمر", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 15, "bold"), command=lambda: open_timer_page(root))
    timer.place(x=340, y=50)
    timer_title.place(x=380, y=170)

    stopwatch_img = PhotoImage(file="files/images/other/stopwatch_icon.png")
    stopwatch = Button(other_page, image=stopwatch_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_stopwatch_page(root))
    stopwatch_title = Button(other_page, text="کرنومتر", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 15, "bold"), command=lambda: open_stopwatch_page(root))
    stopwatch.place(x=170, y=50)
    stopwatch_title.place(x=215, y=170)

    speed_img = PhotoImage(file="files/images/other/speed-test_icon.png")
    speed = Button(other_page, image=speed_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_net_speed_page(root))
    speed_title = Button(other_page, text="سرعت اینترنت", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 15, "bold"), command=lambda: open_net_speed_page(root))
    speed.place(x=0, y=50)
    speed_title.place(x=12, y=170)

    password_img = PhotoImage(file="files/images/other/password_icon.png")
    password = Button(other_page, image=password_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_password_maker_page(root))
    password_title = Button(other_page, text="تولید کننده رمز", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 15, "bold"), command=lambda: open_password_maker_page(root))
    password.place(x=338, y=210)
    password_title.place(x=345, y=330)

    qrcode_img = PhotoImage(file="files/images/other/qr-code_icon.png")
    qrcode = Button(other_page, image=qrcode_img, bg="light blue", bd=0, activebackground="light blue", command=lambda: open_qrcode_maker_page(root))
    qrcode_title = Button(other_page, text="QRcode تولید کننده", bg="light blue", bd=0, activebackground="light blue", font=("Vazirmatn", 15, "bold"), command=lambda: open_qrcode_maker_page(root))
    qrcode.place(x=175, y=210)
    qrcode_title.place(x=160, y=330)

    # about me:
    about_page = Frame(root, width=495, height=395, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    about_page_title = Label(about_page, text="درباره من", bg="light blue", justify="center", font=("Vazirmatn", 20, "bold")).place(x=175, y=0)
    Button(about_page, image=close_icon, bg="light blue", bd=0, activebackground="light blue", command=open_home).place(x=430, y=0)
    
    Label(about_page, text="ابوالفضل رمضانی متولد سال 1386 از قائن هستم", bg="light blue", justify="center", font=("Vazirmatn", 15, "bold")).place(x=35, y=50)
    Label(about_page, text=": راه های تماس", bg="light blue", justify="center", font=("Vazirmatn", 15, "bold")).place(x=150, y=80)

    def open_link(link):
        open(link)

    github_img = PhotoImage(file="files/images/about_me/github.png")
    Button(about_page, image=github_img, bg="light blue", activebackground="light blue", bd=0, command=lambda: open_link("https://github.com/AbRamazani")).place(x=390, y=110)

    instagram_img = PhotoImage(file="files/images/about_me/instagram.png")
    Button(about_page, image=instagram_img, bg="light blue", activebackground="light blue", bd=0, command=lambda: open_link("https://instagram.com/a.b.ramazani")).place(x=300, y=115)

    telegram_img = PhotoImage(file="files/images/about_me/telegram.png")
    Button(about_page, image=telegram_img, bg="light blue", activebackground="light blue", bd=0, command=lambda: open_link("https://t.me/A_b_Ramazani86")).place(x=210, y=110)

    phone_img = PhotoImage(file="files/images/about_me/call.png")
    Button(about_page, image=phone_img, bg="light blue", activebackground="light blue", bd=0, command=lambda: open_link("tel:09158889353")).place(x=120, y=110)

    email_img = PhotoImage(file="files/images/about_me/gmail.png")
    Button(about_page, image=email_img, bg="light blue", activebackground="light blue", bd=0, command=lambda: open_link("mailto:abolfazlramazani86@gmail.com")).place(x=30, y=110)
    
    Label(about_page, text=": راهنمای نرم افزار", bg="light blue", justify="center", font=("Vazirmatn", 15, "bold")).place(x=155, y=180)

    guide_qrcode = PhotoImage(file="files/images/about_me/guide-qrcode.png")
    Button(about_page, image=guide_qrcode, bg="light blue", activebackground="light blue", bd=0, command=lambda: open_link("https://drive.google.com/file/d/1sG7rxTAgtvJ8chH-bD6tUwvBNuY6tfxA/view?usp=sharing"), cursor="hand2").place(x=150, y=215)

    root.mainloop()


if __name__=="__main__":
    home()
