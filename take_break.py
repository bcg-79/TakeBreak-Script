#!usr/bin/python3

import os
import time

sound_file = "sound_files/file6.mp3"

class TakeBreak():
    def __init__(self):
        self._message = "-----> Welcome to TakeBreak System <-----"


    def play_sound(self, s_file=sound_file):
        os.system("mpg123 -o alsa " + s_file)

    def set_time(self, w_time=15, b_time=5):
        self.work_time = w_time * 60 
        self.break_time = b_time * 60

    def start_script(self):
        print(self._message)
        
        count = 1
        while True:
            print("Work Time Start...")
            time.sleep(self.work_time)
            self.play_sound()

            print("Now its break time.....")
            time.sleep(self.break_time)
            self.play_sound()


t_break = TakeBreak()

t_break.set_time(15, 5)

t_break.start_script()

