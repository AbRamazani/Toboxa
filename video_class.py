from tkinter import *
from tkVideoPlayer import TkinterVideo

class Video:
    def __init__(self, master, path) -> None:
        self.vid_player = TkinterVideo(scaled=True, pre_load=False, master=master)
        self.vid_player.load(path)
        self.vid_player.pack(fill="both", expand=True)

        self.vid_player.play()

        self.play_pause_btn = Button(master, text="توقف", bg="light blue", font=("Vazirmatn"), command=self.play_pause)
        self.play_pause_btn.pack()

        self.progress_slider = Scale(master, from_=0, to=self.vid_player.duration(), orient="horizontal", command=self.seek, bg="light blue", font=("Vazirmatn"))
        self.progress_slider.pack(fill="x", padx=12.5)

        self.vid_player.bind("<<Duration>>", self.update_duration)
        self.vid_player.bind("<<SecondChanged>>", self.update_scale)
        self.vid_player.bind("<<Ended>>", self.video_ended)

    def update_duration(self, event):
        """ updates the duration after finding the duration """
        self.progress_slider["to"] = self.vid_player.duration()


    def update_scale(self, event):
        """ updates the scale value """
        if self.progress_slider["to"] == 0:
            self.progress_slider["to"] = self.vid_player.duration()
        if self.vid_player.current_duration() <= self.vid_player.duration():
            self.progress_slider.set(self.vid_player.current_duration())

    def seek(self, value):
        """ used to seek a specific timeframe """
        self.vid_player.seek(int(value))
        self.vid_player.play()
        if int(value) < 85:
            self.play_pause_btn["text"] = "توقف"
        else:
            self.play_pause_btn["text"] = "پخش"


    def skip(self, value: int):
        """ skip seconds """
        self.vid_player.skip_sec(value)
        self.progress_slider.set(self.progress_slider.get() + value)


    def play_pause(self):
        """ pauses and plays """
        if self.vid_player.is_paused():
            self.vid_player.play()
            self.play_pause_btn["text"] = "توقف"

        else:
            self.vid_player.pause()
            self.play_pause_btn["text"] = "پخش"


    def video_ended(self, event):
        """ handle video ended """
        self.progress_slider.set(0)
        self.play_pause_btn["text"] = "پخش"