from tkinter import *
from tkinter import ttk, messagebox, filedialog
from pyperclip import copy, paste

def open_texte_page(pre_page):
    pre_page.destroy()
    texte = Tk()
    texte.config(bg="light blue")
    texte.title("Toboxa=>text editor")
    texte.geometry("650x600+50+50")
    texte.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/programming/text-editor_icon.png")

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
            texte.after(10, open_hamburger)

    def close_hamburger():
        global mak_ham
        if mak_ham == -150:
            hamburger_b.config(image=hamburger_img)
        if mak_ham >= -150:
            hamburger_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            texte.after(10, close_hamburger)

    hamburger_img = PhotoImage(file="files/images/root/menu.png")
    hamburger_b = Button(texte, image=hamburger_img, bg="light blue", bd=0, command=open_hamburger)
    hamburger_b.place(x=0, y=0)

    hamburger_menu = Frame(texte, width=150, height=600, bg="#01ab8c")

    def home():
        texte.destroy()
        from Toboxa import home
        home()

    def lorem():
        from lorem import open_lorem_page
        open_lorem_page(texte)

    def compress():
        from compress import open_compress_page
        open_compress_page(texte)

    Label(hamburger_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburger_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburger).place(x=125, y=0)
    Button(hamburger_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburger_menu, text="لورم ساز", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=lorem).place(x=0, y=65)
    Button(hamburger_menu, text="فشرده‌سازی\n‌فایل‌های‌وب", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=compress).place(x=0, y=100)
    Button(hamburger_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=texte.destroy).place(x=0, y=550)

    # title and img
    Label(texte, image=img, bg="light blue").place(x=150, y=0)
    Label(texte, text="ویرایشگر متن", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=330, y=20)

    # categories

    cadr = Frame(texte, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    global opened, file_address
    opened = False
    file_address = ""

    menubar = Frame(cadr, width=485, height=43, bg="#00ADB5")
    menubar.place(x=0, y=0)

    class Line:
        def __init__(self, master) -> None:
            self.line_l = Label(master, text="|", bg="#00ADB5", fg="#EEEEEE", font=("Vazirmatn", 18, "bold"))

        def place(self, x, y):
            """place the widget"""
            self.line_l.place(x=x, y=y)

        def place_forget(self):
            """clear the widget from the screen"""
            self.line_l.place_forget()

    file_name_l = Label(menubar, text="--بدون عنوان--", bg="#00ADB5", fg="#EEEEEE", font=("Vazirmatn", 15, "bold"))
    file_name_l.place(x=0, y=0)

    Line(menubar).place(x=430, y=0)
    Line(menubar).place(x=360, y=0)

    def close_menus():
        file_f.place_forget()
        edit_f.place_forget()
        file_b.config(bg="#00ADB5", fg="#EEEEEE")
        edit_b.config(bg="#00ADB5", fg="#EEEEEE")
        text_box.place(x=0, y=44, width=467, height=390)
        scroll.place(x=467, y=44, height=390)

    def open_file_f(e = None):
        file_f.place(x=0, y=44)
        edit_f.place_forget()
        text_box.place(x=0, y=88, width=467, height=346)
        scroll.place(x=467, y=88, height=346)
        file_b.config(bg="#EEEEEE", fg="#00ADB5")
        edit_b.config(bg="#00ADB5", fg="#EEEEEE")

    file_b = Button(menubar, text="فایل", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=open_file_f)
    file_b.place(x=440, y=0)

    # file
    file_f = Frame(cadr, width=485, height=43, bg="#00ADB5")

    def open_file(e = None, f = None):
        global opened, file_address
        try:
            if f == None:
                file_name = filedialog.askopenfilename(title="باز کردن فایل",
                initialdir="/")

                file = open(file_name, encoding="utf-8")
                file_name_l.config(text=file_name.split("/")[-1])
                file_address = file_name
            else:
                file = open(f, encoding="utf-8")
                file_name_l.config(text=f.split("/")[-1])
                file_address = f

            text_box.delete("1.0", END)
            text_box.insert(END, file.read())

            line_cl.place(x=225, y=0)

            close_b.place(x=140, y=0)

            opened = True
        except:
            pass

    def save_file(e = None):
        if opened:
            file = open(file_address, "w", encoding="utf-8")
            file.write(text_box.get("1.0", END))
            file.close()

            file_name = file_name_l["text"]
            if file_name[0] == "*":
                file_name_l.config(text=file_name[1:])
        else:
            save_as_file()

    def save_as_file(e =  None):
        try:
            file_name_out = filedialog.asksaveasfile(title="ذخیره کردن فایل",
            initialdir="/",
            filetypes=(("Text files", "*.txt"), ("All file", "*.*")),
            defaultextension=(("Text files", "*.txt"), ("All file", "*.*")))

            file = open(file_name_out.name, "w+", encoding="utf-8")
            file.write(text_box.get("1.0", END))
            file.close()

            open_file(f = file_name_out.name)
        except:
            pass

    def close_file(e = None):
        file_name = file_name_l["text"]
        if file_name != "--بدون عنوان--" and file_name != "*--بدون عنوان--":
            try:
                file_name = file_name_l["text"]

                if file_name[0] == "*":
                    ask_save = messagebox.askyesnocancel("بستن فایل", ".فایل هنوز ذخیره نشده است\nفایل ذخیره شود؟")
                    if ask_save:
                        save_file()
                        text_box.delete("1.0", END)
                        file_name_l.config(text="--بدون عنوان--")
                    elif ask_save == False:
                        text_box.delete("1.0", END)
                        file_name_l.config(text="--بدون عنوان--")

                    if ask_save != None:
                        close_b.place_forget()
                        line_cl.place_forget()
                else:
                    text_box.delete("1.0", END)
                    file_name_l.config(text="--بدون عنوان--")
                    close_b.place_forget()
                    line_cl.place_forget()
            except:
                pass

    open_b = Button(file_f, text="باز کردن", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=open_file)
    open_b.place(x=415, y=0)

    Line(file_f).place(x=405, y=0)

    save_b = Button(file_f, text="ذخیره", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=save_file)
    save_b.place(x=355, y=0)

    Line(file_f).place(x=345, y=0)

    save_as_b = Button(file_f, text="ذخیره به عنوان", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=save_as_file)
    save_as_b.place(x=235, y=0)

    line_cl = Line(file_f)

    close_b = Button(file_f, text="بستن فایل", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=close_file)

    close_file_f = Button(file_f, text="×", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 15, "bold"), bd=0, command=close_menus)
    close_file_f.place(x=0, y=0)

    # _________________________________________

    def open_edit_f(e = None):
        file_f.place_forget()
        edit_f.place(x=0, y=44)
        text_box.place(x=0, y=88, width=467, height=346)
        scroll.place(x=467, y=88, height=346)
        file_b.config(bg="#00ADB5", fg="#EEEEEE")
        edit_b.config(bg="#EEEEEE", fg="#00ADB5")

    edit_b = Button(menubar, text="ویرایش", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=open_edit_f)
    edit_b.place(x=370, y=0)

    # edit
    edit_f = Frame(cadr, width=485, height=43, bg="#00ADB5")

    def cut_text():
        text_select = text_box.get(SEL_FIRST, SEL_LAST)
        copy(text_select)
        text_box.delete(SEL_FIRST, SEL_LAST)
        change(None)

    def copy_text():
        text_select = text_box.get(SEL_FIRST, SEL_LAST)
        copy(text_select)

    def paste_text():
        text_paste = paste()
        text_box.insert(INSERT, text_paste)
        change(None)

    def delete_text():
        text_box.delete(SEL_FIRST, SEL_LAST)
        change(None)

    cut_b = Button(edit_f, text="بُرش", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=cut_text)
    cut_b.place(x=440, y=0)

    Line(edit_f).place(x=430, y=0)

    copy_b = Button(edit_f, text="رونوشت", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=copy_text)
    copy_b.place(x=365, y=0)

    Line(edit_f).place(x=355, y=0)

    paste_b = Button(edit_f, text="چسباندن", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=paste_text)
    paste_b.place(x=285, y=0)

    Line(edit_f).place(x=275, y=0)

    delete_b = Button(edit_f, text="حذف", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=delete_text)
    delete_b.place(x=230, y=0)

    close_edit_f = Button(edit_f, text="×", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 15, "bold"), bd=0, command=close_menus)
    close_edit_f.place(x=0, y=0)

    # _________________________________

    def open_help(e = None):
        close_menus()
        help_page = Toplevel()
        help_page.config(bg="light blue")
        help_page.geometry("620x490")
        help_page.title("Toboxa=>text editor=>help")
        help_page.maxsize((620), (490))

        pages = ttk.Notebook(help_page)
        pages.pack(fill="both", expand=True)

        file_h = Frame(pages, bg="#EEEEE0")
        file_h.pack(fill="both", expand=True)

        open_l = LabelFrame(file_h, bg="#EEEEE9", text="باز کردن", font=("Vazirmatn", 12, "bold"))
        open_l.pack(fill="both", expand=True)

        text_o_h = """.این گزینه برای باز کردن یک فایل از داخل رایانه شما و ایجاد تغییرات در آن است"""

        Label(open_l, bg="#EEEEE9", fg="black", font=("Vazirmatn", 10), justify="center", text=text_o_h).pack(fill="both", expand=True)

        save_l = LabelFrame(file_h, bg="#EEEEE9", text="ذخیره", font=("Vazirmatn", 12, "bold"))
        save_l.pack(fill="both", expand=True)

        text_s_h = """.این گزینه برای ذخیره کردن فایل باز شده توسط شما در خود فایل است
        .اگر شما فایلی را باز نکرده باشید با انتخاب این گزینه می توانید این فایل را در رایانه خود ذخیره کنید"""

        Label(save_l, bg="#EEEEE9", fg="black", font=("Vazirmatn", 10), justify="center", text=text_s_h).pack(fill="both", expand=True)

        save_as_l = LabelFrame(file_h, bg="#EEEEE9", text="ذخیره به عنوان", font=("Vazirmatn", 12, "bold"))
        save_as_l.pack(fill="both", expand=True)

        text_sa_h = """.این گزینه برای ذخیره کردن نوشته ها در فایل دیگری در رایانه شماست"""

        Label(save_as_l, bg="#EEEEE9", fg="black", font=("Vazirmatn", 10), justify="center", text=text_sa_h).pack(fill="both", expand=True)

        close_l = LabelFrame(file_h, bg="#EEEEE9", text="بستن", font=("Vazirmatn", 12, "bold"))
        close_l.pack(fill="both", expand=True)

        text_c_h = """.با استفاده از این گزینه می توانید فایل باز شده را ببندید
        اگر فایل را ذخیره نکرده باشید اخطاری به نمایش در خواهد آمد که شما می توانید از بستن یا ذخیره کردن صرف نظر
        .کنید"""

        Label(close_l, bg="#EEEEE9", fg="black", font=("Vazirmatn", 10), justify="center", text=text_c_h).pack(fill="both", expand=True)

        edit_h = Frame(pages, bg="#EEEEE0")
        edit_h.pack(fill="both", expand=True)
        
        cut_l = LabelFrame(edit_h, bg="#EEEEE9", text="بُرش", font=("Vazirmatn", 12, "bold"))
        cut_l.pack(fill="both", expand=True)

        text_cu_h = """می باشد که متن مورد نظر خود را انتخاب و با این گزینه از آن رونوشت گرفته Cut این گزینه معادل
        .و آن قسمت از متن حذف می شود"""

        Label(cut_l, bg="#EEEEE9", fg="black", font=("Vazirmatn", 10), justify="center", text=text_cu_h).pack(fill="both", expand=True)
        
        copy_l = LabelFrame(edit_h, bg="#EEEEE9", text="رونوشت", font=("Vazirmatn", 12, "bold"))
        copy_l.pack(fill="both", expand=True)

        text_co_h = """.می باشد که متن مورد نظر خود را انتخاب و با این گزینه از آن رونوشت گرفته می شود Copy این گزینه معادل"""

        Label(copy_l, bg="#EEEEE9", fg="black", font=("Vazirmatn", 10), justify="center", text=text_co_h).pack(fill="both", expand=True)

        paste_l = LabelFrame(edit_h, bg="#EEEEE9", text="ذخیره به عنوان", font=("Vazirmatn", 12, "bold"))
        paste_l.pack(fill="both", expand=True)

        text_p_h = """.می باشد که متن رونوشت گرفته شده را در مکان موردنظر شما می چسباند Paste این گزینه معادل"""

        Label(paste_l, bg="#EEEEE9", fg="black", font=("Vazirmatn", 10), justify="center", text=text_p_h).pack(fill="both", expand=True)

        delete_l = LabelFrame(edit_h, bg="#EEEEE9", text="بستن", font=("Vazirmatn", 12, "bold"))
        delete_l.pack(fill="both", expand=True)

        text_d_h = """.می باشد که متن مورد نظر خود را انتخاب و با این گزینه آن قسمت متن حذف می شود Delete این گزینه معادل"""

        Label(delete_l, bg="#EEEEE9", fg="black", font=("Vazirmatn", 10), justify="center", text=text_d_h).pack(fill="both", expand=True)

        shortcut = Frame(pages, bg="#EEEEE0")
        shortcut.pack(fill="both", expand=True)

        class Table:
	
            def __init__(self,root):
                
                # code for creating table
                for i in range(total_rows):
                    for j in range(total_columns):
                        
                        self.e = Label(root, width=31,
                                    font=('Vazirmatn',15,'bold'), text=lst[i][j], relief="ridge")
                        
                        self.e.place(y=i*30, x=j*310)

        lst = [("کارکرد","میانبر"),
        ("جابه جایی حروف","Ctrl+T"),
        ("باز کردن یک فایل","Ctrl+O"),
        ("بستن فایل","Ctrl+Shift+C"),
        ("انتخاب تمامی متن","Ctrl+A"),
        ("ذخیره کردن فایل","Ctrl+S"),
        ("ذخیره کردن فایل به عنوان","Ctrl+Shift+S"),
        ("بازگرداندن تغییر","Ctrl+Z"),
        ("برش متن","Ctrl+X"),
        ("رونوشت گرفتن متن","Ctrl+C"),
        ("چسباندن متن","Ctrl+V"),
        ("بازکردن منوی فایل","Alt+F"),
        ("باز کردن منوی ویرایش","Alt+E"),
        ("باز کردن راهنما","F1"),
        ]

        # find total number of rows and
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])

        Table(shortcut)
        Label(shortcut, text="برای استفاده از این میانبر ها باید زبان صفحه کلید انگلیسی باشد", bg="#EEEEE9", fg="red", font=("Vazirmatn", 11)).pack(side="bottom")

        pages.add(file_h, text="فایل")
        pages.add(edit_h, text="ویرایش")
        pages.add(shortcut, text="میانبرها")

        help_page.mainloop()
        

    help_b = Button(menubar, text="راهنما", fg="#EEEEEE", bg="#00ADB5", font=("Vazirmatn", 13, "bold"), bd=0, command=open_help)
    help_b.place(x=310, y=0)


    text_box = Text(cadr, bg="#E3FDFD", font=("Vazirmatn", 15), undo=True, wrap=WORD)
    text_box.place(x=0, y=44, width=467, height=390)

    scroll = Scrollbar(cadr, command=text_box.yview)
    scroll.place(x=467, y=44, height=390)
    text_box.config(yscrollcommand=scroll.set)

    def change(e):
        file_name = file_name_l["text"]
        if file_name[0] != "*" and f"abc{e.char}" != "abc":
            file_name_l.config(text=f"*{file_name}")

    text_box.bind("<Key>", change)

    text_box.bind("<Control-o>", open_file)
    text_box.bind("<Control-s>", save_file)
    text_box.bind("<Control-Shift-S>", save_as_file)
    text_box.bind("<Control-Shift-C>", close_file)
    text_box.bind("<Alt-f>", open_file_f)
    text_box.bind("<Alt-e>", open_edit_f)
    text_box.bind("<F1>", open_help)
    
    texte.mainloop()