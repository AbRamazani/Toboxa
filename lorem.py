from tkinter import *
from tkinter import ttk, messagebox
from random import randint
from pyperclip import copy

def open_lorem_page(pre_page):
    pre_page.destroy()
    lorem = Tk()
    lorem.config(bg="light blue")
    lorem.title("Toboxa=>lorem ipsum generator")
    lorem.geometry("650x600+50+50")
    lorem.resizable(width=False, height=False)

    img = PhotoImage(file="files/images/programming/publishing_icon.png")

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
            lorem.after(10, open_hamburgar)

    def close_hamburgar():
        global mak_ham
        if mak_ham == -150:
            hamburgar_b.config(image=hamburgar_img)
        if mak_ham >= -150:
            hamburgar_menu.place(x=mak_ham, y=0)
            mak_ham -= 1
            lorem.after(10, close_hamburgar)

    hamburgar_img = PhotoImage(file="files/images/root/menu.png")
    hamburgar_b = Button(lorem, image=hamburgar_img, bg="light blue", bd=0, command=open_hamburgar)
    hamburgar_b.place(x=0, y=0)

    hamburgar_menu = Frame(lorem, width=150, height=600, bg="#01ab8c")

    def home():
        lorem.destroy()
        from Toboxa import home
        home()

    def compress():
        from compress import open_compress_page
        open_compress_page(lorem)

    def text_editor():
        from compress import open_compress_page
        open_compress_page(lorem)

    Label(hamburgar_menu, text="توبوکسا", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15, "bold")).place(x=0, y=0)
    Button(hamburgar_menu, text="×", bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=close_hamburgar).place(x=125, y=0)
    Button(hamburgar_menu, text="خانه", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=home).place(x=0, y=30)
    Button(hamburgar_menu, text="فشرده‌سازی\n‌فایل‌های‌وب", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=compress).place(x=0, y=65)
    Button(hamburgar_menu, text="ویرایشگر متن", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=text_editor).place(x=0, y=135)
    Button(hamburgar_menu, text="خروج", width=13, bg="#01ab8c", fg="white", bd=0, font=("Vazirmatn", 15), command=lorem.destroy).place(x=0, y=550)

    # title and img
    Label(lorem, image=img, bg="light blue").place(x=150, y=0)
    Label(lorem, text="لورم ساز", bg="light blue", justify="center", font=("Vazirmatn", 35, "bold")).place(x=400, y=0)

    # categories

    cadr = Frame(lorem, width=495, height=445, bg="light blue", highlightbackground="#01ab8c", highlightthickness=5)
    cadr.place(x=150, y=150)

    Label(cadr, text=": نوع خروجی", bg="light blue", font=("Vazirmatn", 15, "bold")).place(x=350, y=0)
    type_l = StringVar()
    type_l_cadr = ttk.Combobox(cadr, textvariable=type_l, values=("پاراگراف", "جمله", "کلمه"), state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).place(x=185, y=5)

    is_reandom = IntVar()
    is_reandom_cadr = Checkbutton(cadr, text="تصادفی", variable=is_reandom, bg="light blue", font=("Vazirmatn", 15, "bold")).place(x=50, y=0)

    Label(cadr, text=": زبان خروجی", bg="light blue", font=("Vazirmatn", 15, "bold")).place(x=350, y=50)
    language = StringVar()
    language_cadr = ttk.Combobox(cadr, textvariable=language, values=("français", "English", "فارسی", "العَرَبِيّة", "русский", "Deutsch"), state="readonly", justify="center", font=("Vazirmatn", 10, "bold")).place(x=185, y=55)

    Label(cadr, text=": تکرار", bg="light blue", font=("Vazirmatn", 15, "bold")).place(x=90, y=50)
    repeat = IntVar()
    repeat_cadr = Spinbox(cadr, from_=0, to=100, textvariable=repeat, wrap=True, font=("Vazirmatn", 13, "bold"), width=2).place(x=50, y=50)
    

    def make_lorem():
        type_l_g = type_l.get()
        if type_l_g == "کلمه":
            type_en = "word"
        elif type_l_g == "جمله":
            type_en = "sentence"
        elif type_l_g == "پاراگراف":
            type_en = "paragraph"
        is_reandom_g = is_reandom.get()
        lang = language.get()
        rep = repeat.get()

        persian = {
            "word" : ["برنامه نویس", "راهکار", "رایانه", "سوالات", "پیوسته", "تکنولوژی", "کتاب", "دنیا", "متن", "زمان"],
            "sentence" : ["لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.", "با این همه، ما تا آنجا که ممکن است، با علاقه فراوان و دلواپسی زیاد به زندگی ادامه می دهیم، همان‌ طور که تا آنجا که ممکن است طولانی‌ تر در یک حباب صابون می‌ دمیم تا بزرگتر شود، گر چه با قطعیتی تمام می‌ دانیم که خواهد ترکید.", "مداد رنگی ها مشغول بودند به جز مداد سفید، هیچکس به او کار نمیداد.", "استفاده از این متن تستی می تواند سرعت پیشرفت پروژه را افزایش دهد، و طراحان به جای تایپ و نگارش متن می توانند تنها با یک کپی و پست این متن را در کادرهای مختلف جایگزین نمائید."],
            "paragraph" : ["لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است. چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است و برای شرایط فعلی تکنولوژی مورد نیاز و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد. کتابهای زیادی در شصت و سه درصد گذشته، حال و آینده شناخت فراوان جامعه و متخصصان را می طلبد تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی و فرهنگ پیشرو در زبان فارسی ایجاد کرد. در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها و شرایط سخت تایپ به پایان رسد وزمان مورد نیاز شامل حروفچینی دستاوردهای اصلی و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد.", "این یک نوشته آزمایشی است که به طراحان و برنامه نویسان کمک میکند تا این عزیزان با بهره گیری از این نوشته تستی و آزمایشی بتوانند نمونه تکمیل شده از پروژه و طرح خودشان را به کارفرما نمایش دهند، استفاده از این متن تستی می تواند سرعت پیشرفت پروژه را افزایش دهد، و طراحان به جای تایپ و نگارش متن می توانند تنها با یک کپی و پست این متن را در کادرهای مختلف جایگزین نمائید.", "وقتی ثروت‌ های بزرگ به دست برخی مردم می‌افتد در پرتو آن نیرومند می‌شوند و در سایهٔ نیرومندی و ثروت خیال می‌ کنند که می‌توانند در خارج از وطن خود زندگی نمایند و خوشبخت و سرافراز باشند ولی به زودی می‌ فهمند که اشتباه کرده‌ اند و عظمت هر ملتی بر روی خرابه‌ های وطن خودش می‌باشد و بس!", "هر نفسی که فرو می‌ بریم، مرگی را که مدام به ما دست‌ اندازی می‌کند پس می‌زند... در نهایت این مرگ است که باید پیروز شود، زیرا از هنگام تولد بخشی از سرنوشت ما شده و فقط مدت کوتاهی پیش از بلعیدن طعمه اش، با آن بازی می کند. با این همه، ما تا آنجا که ممکن است، با علاقه فراوان و دلواپسی زیاد به زندگی ادامه می دهیم، همان‌ طور که تا آنجا که ممکن است طولانی‌ تر در یک حباب صابون می‌ دمیم تا بزرگتر شود، گر چه با قطعیتی تمام می‌ دانیم که خواهد ترکید."]
        }

        english = {
            "word": ["Programmer", "Solution", "Computer", "Questions", "Continuous", "Technology", "Book", "World", "Text", "Time"],
            "sentence": ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "Colored pencils were busy except for the white pencil, no one worked for him.", "Nevertheless, we continue to live as much as possible with much interest and concern, as long as we may think longer in a soap bubble to become larger, albeit with full certainty. That will burst.", "using this test text can speed up the progress of the project. Instead of typing and writing text, designers can replace this text in different boxes with a single copy and post."],
            "paragraph": ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "This is a test piece that helps designers and programmers to use these test letters to demonstrate their completed designs and designs to the employer, using this test text can speed up the progress of the project. Instead of typing and writing text, designers can replace this text in different boxes with a single copy and post.", "When large fortunes fall into the hands of some people, they become strong in the light of it, and in the shadow of strength and wealth they dream that they can live out of their homeland and be happy and proud, they will soon realize that they have made mistakes, and the greatness of every nation On the ruins of his homeland and cease!", "Every breath we surrender will turn back the death that continues to inflict on us ... Ultimately, this death is to be won, because it was part of our destiny since our birth and just shortly before devouring its prey, It plays with it. Nevertheless, we continue to live as much as possible with much interest and concern, as long as we may think longer in a soap bubble to become larger, albeit with full certainty. That will burst."]
        }

        arabic = {
            "word": ["مبرمج" , "حل" , "كمبيوتر" , "أسئلة" , "مستمر" , "تقنية" , "كتاب" , "العالم" , "نص" , "الوقت"] ,
            "sentence": ["لوريم إيبسوم هو ببساطة نص شكلي (بمعنى أن الغاية هي الشكل وليس المحتوى) ويُستخدم في صناعات المطابع ودور النشر.", "فإننا لا نزال نعيش بأكبر قدر ممكن مع الكثير من الاهتمام والقلق ، طالما أننا قد نفكر لفترة أطول في فقاعة الصابون لتصبح أكبر ، وإن كان على يقين تام. سوف تنفجر.", "كانت أقلام الرصاص الملونة مشغولة باستثناء قلم الرصاص الأبيض ، ولم يعمل أحد من أجله.", "ذلك باستخدام نص الاختبار هذا الذي يمكن أن يسرع من تقدم المشروع. بدلاً من كتابة النص وكتابته ، يمكن للمصممين استبدال هذا النص في مربعات مختلفة بنسخة ورسالة واحدة."],
            "paragraph": ["لوريم إيبسوم هو ببساطة نص شكلي (بمعنى أن الغاية هي الشكل وليس المحتوى) ويُستخدم في صناعات المطابع ودور النشر. كان لوريم إيبسوم ولايزال المعيار للنص الشكلي منذ القرن الخامس عشر عندما قامت مطبعة مجهولة برص مجموعة من الأحرف بشكل عشوائي أخذتها من نص، لتكوّن كتيّب بمثابة دليل أو مرجع شكلي لهذه الأحرف. خمسة قرون من الزمن لم تقضي على هذا النص، بل انه حتى صار مستخدماً وبشكله الأصلي في الطباعة والتنضيد الإلكتروني. انتشر بشكل كبير في ستينيّات هذا القرن مع إصدار رقائق 'ليتراسيت' البلاستيكية تحوي مقاطع من هذا النص، وعاد لينتشر مرة أخرى مؤخراَ مع ظهور برامج النشر الإلكتروني مثل 'ألدوس بايج مايكر' والتي حوت أيضاً على نسخ من نص لوريم إيبسوم.", "هذه هي قطعة اختبار تساعد المصممين والمبرمجين على استخدام رسائل الاختبار هذه لإثبات تصاميمهم وتصاميمهم التي تم إكمالها لصاحب العمل ، وذلك باستخدام نص الاختبار هذا الذي يمكن أن يسرع من تقدم المشروع. بدلاً من كتابة النص وكتابته ، يمكن للمصممين استبدال هذا النص في مربعات مختلفة بنسخة ورسالة واحدة.", "عندما تقع ثروات كبيرة في أيدي بعض الناس ، فإنها تصبح قوية في ضوء ذلك ، وفي ظل القوة والثروة يحلمون بأنهم يستطيعون العيش خارج وطنهم وأن يكونوا سعداء وفخورين ، وسوف يدركون قريبا أنهم قد ارتكبوا أخطاء ، وعظمة كل أمة على أنقاض وطنه والتوقف!", "كل نفس نستسلم سوف يعيد الموت الذي يستمر في إلحاقه بنا ... في نهاية المطاف ، يجب الفوز بهذا الموت ، لأنه كان جزءًا من مصيرنا منذ ولادتنا وقبل إفتلال فرائسها بوقت قصير ، انها تلعب معها. ومع ذلك ، فإننا لا نزال نعيش بأكبر قدر ممكن مع الكثير من الاهتمام والقلق ، طالما أننا قد نفكر لفترة أطول في فقاعة الصابون لتصبح أكبر ، وإن كان على يقين تام. سوف تنفجر."]
        }

        russian = {
            "word": ["Программист", "Решение", "Компьютер", "Вопросы", "Непрерывный", "Технология", "Книга", "Мир", "Текст", "Время"],
            "sentence": ["Лорем ипсум долор сит амет, ут иусто бонорум яуи. Доминг яуодси садипсцинг вис те.", "Цветные карандаши были заняты, кроме белого, никто не работал на него", "Тем не менее, мы продолжаем. жить как можно дольше с большим интересом и заботой, пока мы можем дольше думать в мыльном пузыре, чтобы стать больше, хотя и с полной уверенностью. Это лопнет. "," использование этого тестового текста может ускорить продвижение проект. Вместо того, чтобы набирать и писать текст, дизайнеры могут заменить этот текст в разных полях одной копией и публикацией."],
            "paragraph": ["Лорем ипсум долор сит амет, ут иусто бонорум яуи. Доминг яуодси садипсцинг вис те. Примис номинати губергрен вим еу. Но мутат албуциус аргументум ест, вих ад фабеллас номинати, тота вивендо ассуеверит сед ад. Ан тантас сплендиде персеяуерис про."," Это тестовый образец, который помогает дизайнерам и программистам использовать эти тестовые буквы, чтобы продемонстрировать их готовых дизайнов и дизайнов для работодателя, использование этого тестового текста может ускорить продвижение проекта. Вместо того, чтобы печатать и писать текст, дизайнеры могут заменить этот текст в разных полях одной копией и опубликовать. "," Когда выпадают большие состояния попадая в руки некоторых людей, они становятся сильными в свете этого, и в тени силы и богатства они мечтают, что они могут жить за пределами своей родины и быть счастливыми и гордыми, Вы скоро поймете, что они совершили ошибки, и величие каждого народа На руинах своей родины и прекратится! "," Каждый вздох, который мы отдаем, вернет назад смерть, которая продолжает причинять нам ... В конце концов, эта смерть нужно выиграть, потому что он был частью нашей судьбы с момента нашего рождения и незадолго до того, как пожирать свою добычу. Он играет с ней. Тем не менее, мы продолжаем жить, насколько это возможно, с большим интересом и заботой, пока мы можем дольше думать в мыльном пузыре, чтобы стать больше, хотя и с полной уверенностью. Это лопнет. "]
        }

        french = {
            "word": ["Programmeur", "Solution", "Ordinateur", "Questions", "Continu", "Technologie", "Livre", "Monde", "Texte", "Temps"],
            "sentence": [" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ", " Les crayons de couleur étaient occupés à part le crayon blanc, personne ne travaillait pour lui. ", " Néanmoins, nous continuons vivre autant que possible avec beaucoup d'intérêt et d'inquiétude, tant que nous pouvons penser plus longtemps dans une bulle de savon pour devenir plus grande, bien qu'avec une certitude totale. Cela éclatera. projet. Au lieu de taper et d'écrire du texte, les concepteurs peuvent remplacer ce texte dans différentes cases par une seule copie et publier."],
            "paragraph": ["Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "Il s'agit d'une pièce de test qui aide les concepteurs et les programmeurs à utiliser ces lettres de test pour démontrer leurs conceptions et conceptions terminées à l'employeur. L'utilisation de ce texte de test peut accélérer la progression du projet. Au lieu de taper et d'écrire du texte , les concepteurs peuvent remplacer ce texte dans différentes cases par un seul exemplaire et poster.", "Quand de grosses fortunes tombent entre les mains de certaines personnes, elles deviennent fortes à la lumière de celle-ci, et à l'ombre de la force et de la richesse, elles rêvent que ils peuvent vivre hors de leur patrie et être heureux et fiers, ils se rendront vite compte qu'ils ont commis des erreurs, et la grandeur de chaque nation Sur les ruines de sa patrie et cesser! ", "Chaque souffle que nous rendons fera reculer la mort qui continue de nous infliger... En fin de compte, cette mort est à gagner, car elle faisait partie de notre destin depuis notre naissance et peu de temps avant de dévorer sa proie, Elle joue avec. possible avec beaucoup d'intérêt et conc ern, aussi longtemps que nous pouvons penser plus longtemps dans une bulle de savon pour devenir plus grande, mais avec une certitude totale. Cela va éclater."]
        }

        german = {
            "word": ["Programmierer", "Lösung", "Computer", "Fragen", "Kontinuierlich", "Technologie", "Buch", "Welt", "Text", "Zeit"],
            "sentence": ["Deutsches Ipsum Dolor deserunt dissentias Spezi et. Tollit argumentum ius an.", "Buntstifte waren beschäftigt außer dem Weißstift, keiner hat für ihn gearbeitet.", "Trotzdem leben wir so gut es geht mit viel Interesse weiter und Besorgnis, solange wir länger in einer Seifenblase denken dürfen, um größer zu werden, wenn auch mit voller Sicherheit. Das wird platzen.", "Die Verwendung dieses Testtextes kann den Projektfortschritt beschleunigen. Designer können diesen Text in verschiedenen Feldern durch eine einzige Kopie und einen Beitrag ersetzen."],
            "paragraph": ["Deutsches Ipsum Dolor id latine Rubin auf Schienen complectitur pri, mea meliore denique Goethe id. Elitr expetenda nam an, Volkswagen ei reque euismod assentior. Odio Kindergarten iracundia ex pri. Ut vel Deutsche Mark mandamus, quas natum adversarium ei zu spät diam minim ehrlichatis eum no", "Dies ist ein Teststück, das Designern und Programmierern hilft, diese Testbriefe zu verwenden, um ihre fertigen Designs und Designs dem Arbeitgeber zu demonstrieren. Die Verwendung dieses Testtextes kann den Fortschritt des Projekts beschleunigen. Anstatt zu tippen und zu schreiben Text können Designer diesen Text in verschiedenen Kästchen durch eine einzige Kopie und einen einzigen Beitrag ersetzen.", "Wenn einigen Menschen große Vermögen in die Hände fallen, werden sie im Lichte dessen stark, und im Schatten von Stärke und Reichtum träumen sie dass sie aus ihrer Heimat leben und glücklich und stolz sein können, werden sie bald erkennen, dass sie Fehler gemacht haben, und die Größe jeder Nation Auf den Trümmern seiner Heimat und aufhören!", "Jeden Atemzug geben wir auf wird den Tod, der uns weiterhin zufügt, zurückkehren ... Letztlich ist dieser Tod zu gewinnen, denn er war seit unserer Geburt Teil unseres Schicksals und kurz bevor er seine Beute verschlingt, spielt er damit. Trotzdem leben wir so viel wie möglich mit viel Interesse und Sorge weiter, solange wir länger in einer Seifenblase denken dürfen, um größer zu werden, wenn auch mit voller Gewissheit. Das wird platzen."]
        }

        if type_l_g == "" or lang == "":
            messagebox.showerror("خطا", "لطفا تمامی قسمت ها را کامل کنید")
        elif rep != 0:
            text_r = ""
            if lang == "فارسی":
                for i in range(1, rep+1):
                    if is_reandom_g == 1:
                        num = randint(0, len(persian[type_en])-1)
                    else:
                        num = 0
                    pre_res = persian[type_en][num]
                    text_r = f"{text_r} {pre_res}"
                result.delete("1.0", END)
                result.tag_configure("right_w", justify="right")
                result.insert(END, text_r, "right_w")
            elif lang == "English":
                for i in range(1, rep+1):
                    if is_reandom_g == 1:
                        num = randint(0, len(english[type_en])-1)
                    else:
                        num = 0
                    pre_res = english[type_en][num]
                    text_r = f"{text_r} {pre_res}"
                result.delete("1.0", END)
                result.insert(END, text_r)
            elif lang == "العَرَبِيّة":
                for i in range(1, rep+1):
                    if is_reandom_g == 1:
                        num = randint(0, len(arabic[type_en])-1)
                    else:
                        num = 0
                    pre_res = arabic[type_en][num]
                    text_r = f"{text_r} {pre_res}"
                result.delete("1.0", END)
                result.tag_configure("right_w", justify="right")
                result.insert(END, text_r, "right_w")
            elif lang == "русский":
                for i in range(1, rep+1):
                    if is_reandom_g == 1:
                        num = randint(0, len(russian[type_en])-1)
                    else:
                        num = 0
                    pre_res = russian[type_en][num]
                    text_r = f"{text_r} {pre_res}"
                result.delete("1.0", END)
                result.insert(END, text_r)
            elif lang == "Deutsch":
                for i in range(1, rep+1):
                    if is_reandom_g == 1:
                        num = randint(0, len(german[type_en])-1)
                    else:
                        num = 0
                    pre_res = german[type_en][num]
                    text_r = f"{text_r} {pre_res}"
                result.delete("1.0", END)
                result.insert(END, text_r)
            elif lang == "français":
                for i in range(1, rep+1):
                    if is_reandom_g == 1:
                        num = randint(0, len(french[type_en])-1)
                    else:
                        num = 0
                    pre_res = french[type_en][num]
                    text_r = f"{text_r} {pre_res}"
                result.delete("1.0", END)
                result.insert(END, text_r)

            

    Button(cadr, text="بساز", bg="light blue", font=("Vazirmatn", 15, "bold"), width=35, command=make_lorem).place(x=50, y=105)

    result = Text(cadr, font=("Vazirmatn", 13, "bold"), height=9, width=42, bg="light yellow")
    result.place(x=35, y=170)
    scroll = Scrollbar(cadr, command=result.yview, orient='vertical')
    scroll.place(x=20, y=171, height=246)
    result["yscrollcommand"] = scroll.set

    def copy_result():
        text = result.get("1.0", END)
        copy(text)
        messagebox.showinfo("کپی", "متن کپی شد")

    Button(cadr, text="کپی", bg="light blue", font=("Vazirmatn", 10, "bold"), command=copy_result).place(x=458, y=399, width=30)

    lorem.mainloop()