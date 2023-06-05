from tkinter import *
from tkinter import filedialog, messagebox
from pyperclip import copy
import re

def open_compress_page(pre_page):
    pre_page.destroy()
    compress = Tk()
    compress.config(bg="light blue")
    compress.title("Toboxa=>compress web files")
    compress.geometry("650x600+50+50")
    compress.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/programming/compression_icon.png")

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
            compress.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            compress.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(compress, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(compress, width=150, height=600, bg="#01ab8c")

    def home():
        compress.destroy()
        from Toboxa import home
        home()

    def lorem():
        from lorem import open_lorem_page
        open_lorem_page(compress)

    def text_editor():
        from text_editor import open_texte_page
        open_texte_page(compress)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="لورم ساز", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=lorem).place(x=0, y=65)
    Button(hamburgar_menu, text="ویرایشگر متن", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=text_editor).place(x=0, y=100)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=compress.destroy).place(x=0, y=550)

    # title and img
    Label(compress, image=img, bg="light blue").place(x=150, y=0)
    Label(compress, text="فشره‌سازی‌فایل‌های‌وب", bg="light blue", justify="center", font=("Vazirmatn", 27, "bold")).place(x=300, y=25)

    # categories

    cadr = Frame(compress, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    def open_file():
        file_name = filedialog.askopenfilename(title="باز کردن فایل",
        initialdir="/",
        filetypes=(("HTML files", "*.html"), ("CSS files", "*.css"), ("Java Script files", "*.js")))

        ext = file_name.split(".")[-1]
        if ext == "html":
            html.place(x=218, y=200)
            css.place_forget()
            js.place_forget()
        elif ext == "css":
            html.place_forget()
            css.place(x=218, y=200)
            js.place_forget()
        elif ext == "js":
            html.place_forget()
            css.place_forget()
            js.place(x=218, y=200)

        file = open(file_name, encoding="utf-8")

        input_text.delete("1.0", END)
        input_text.insert("1.0", file.read())

        file.close()

        reset.place(x=219, y=400)

    def save_text():
        global file_name_out
        file_name_out = filedialog.asksaveasfile(title="ذخیره کردن فایل",
        initialdir="/",
        filetypes=(("HTML files", "*.html"), ("CSS files", "*.css"), ("Java Script files", "*.js")),
        defaultextension=(("HTML files", "*.html"), ("CSS files", "*.css"), ("Java Script files", "*.js")))

        file = open(file_name_out.name, "w+", encoding="utf-8")
        file.write(output_text.get("1.0", END))
        file.close()

    def delete_comments_html(text: str):
        ''' remove the comments text(<!--...-->) from html code '''
        text_r = text
        count = 0
        while count+1 != len(text_r):
            if text_r[count] == "<" and text_r[count+1] == "!" and text_r[count+2] == "-" and  text_r[count+3] == "-":
                ind = count+4
                while ind+1 != len(text_r)-1 :
                    if text_r[ind] == "-" and text_r[ind+1] == "-" and text_r[ind+2] == ">":
                        text_r = text_r[0: count:] + text_r[ind+2 + 1::]
                        break
                    else:
                        ind += 1
                        continue
                count = 0
            else:
                count += 1

        return text_r

    def compress_html():
        text = input_text.get("1.0", END).replace("\n", "")
        text = re.sub(r'\s+',' ', text)
        
        text = delete_comments_html(text)

        output_text.delete("1.0", END)
        output_text.insert(END, text)
        copy_b.place(x=320, y=400)

    def delete_comments_css(text: str):
        ''' remove the comments text(/*...*/) from css and js code '''
        text_r = text
        count = 0
        while count+1 != len(text_r):
            if text_r[count] == "/" and text_r[count+1] == "*":
                ind = count+2
                while ind+1 != len(text_r)-1 :
                    if text_r[ind] == "*" and text_r[ind+1] == "/":
                        text_r = text_r[0: count:] + text_r[ind+1 + 1::]
                        break
                    else:
                        ind += 1
                        continue
                count = 0
            else:
                count += 1

        return text_r

    def compress_css():
        text = input_text.get("1.0", END).replace("\n", "")
        text = re.sub(r'\s+',' ', text)
        text = delete_comments_css(text)

        output_text.delete("1.0", END)
        output_text.insert(END, text)
        copy_b.place(x=320, y=400)

    def delete_comments_js(text: str):
        ''' remove the comments text(//...) from js code '''
        text_r = text
        count = 0
        while count+1 != len(text_r):
            if text_r[count] == "/" and text_r[count+1] == "/":
                ind = count+2
                while ind+1 != len(text_r)-1 :
                    if text_r[ind] == "\n":
                        text_r = text_r[0: count:] + text_r[ind + 1::]
                        break
                    else:
                        ind += 1
                        continue
                count = 0
            else:
                count += 1

        return text_r

    def compress_js():
        text = input_text.get("1.0", END)
        text = delete_comments_css(delete_comments_js(text))
        text.replace("\n", "")
        text = re.sub(r'\s+',' ', text)

        output_text.delete("1.0", END)
        output_text.insert(END, text)
        copy_b.place(x=320, y=400)

    def reset_data():
        input_text.delete("1.0", END)
        output_text.delete("1.0", END)
        html.place(x=218, y=100)
        css.place(x=218, y=200)
        js.place(x=218, y=300)
        reset.place_forget()
        copy_b.place_forget()

    def write(e):
        reset.place(x=219, y=400)


    Button(cadr, text="بازکردن یک فایل", font=("Vazirmatn", 13, "bold"), bg="light blue", command=open_file).place(x=35, y=0)

    input_text = Text(cadr, font=("Vazirmatn", 10), width=28, height=18, undo=True, wrap=WORD)
    input_text.place(x=0, y=50)
    scroll1 = Scrollbar(cadr, command=input_text.yview)
    scroll1.place(x=200, y=50, height=382)
    input_text.configure(yscrollcommand=scroll1.set)

    html = Button(cadr, text="فشرده\nسازی\nHTML", font=("Vazirmatn", 10, "bold"), bg="light blue", command=compress_html)
    html.place(x=218, y=100)
    css = Button(cadr, text="فشرده\nسازی\nCSS", font=("Vazirmatn", 10, "bold"), bg="light blue", command=compress_css)
    css.place(x=218, y=200)
    js = Button(cadr, text="فشرده\nسازی\nJS", font=("Vazirmatn", 10, "bold"), bg="light blue", command=compress_js)
    js.place(x=218, y=300)
    reset = Button(cadr, text="بازنشانی", font=("Vazirmatn", 8, "bold"), bg="light blue", command=reset_data)
    
    Button(cadr, text="ذخیره کردن خروجی", font=("Vazirmatn", 13, "bold"), bg="light blue", command=save_text).place(x=300, y=0)

    output_text = Text(cadr, font=("Vazirmatn", 10), width=28, height=18, undo=True, wrap=WORD)
    output_text.place(x=265, y=50)
    scroll2 = Scrollbar(cadr, command=output_text.yview)
    scroll2.place(x=465, y=50, height=382)
    output_text.configure(yscrollcommand=scroll2.set)

    input_text.bind("<Key>", write)

    def copy_text():
        text = output_text.get("1.0", END)
        copy(text)
        messagebox.showinfo("کپی", "متن کپی شد")       

    copy_b = Button(cadr, text="کپی کردن خروجی", font=("Vazirmatn", 9, "bold"), bg="light blue", command=copy_text)
    
    compress.mainloop()