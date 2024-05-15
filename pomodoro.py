from tkinter import *
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
SOUND_PATH = "assets/clock-ticking-2.wav"
# -------------------------- Global Variables ----------------------------- #
reps = 0
work_complete = ""
timer_id = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, work_complete
    reps = 0
    work_complete = ""
    canvas.itemconfig(timer_text, text=format_time(0))
    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text=work_complete)
    window.after_cancel(timer_id)
    winsound.PlaySound(None, winsound.SND_PURGE)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps, work_complete
    reps += 1
    count = 60
    if reps % 8 == 0:
        count *= LONG_BREAK_MIN
        title_label.config(text="Break", fg=RED)
        work_complete += "✔"
        check_mark.config(text=work_complete)
        count_down(count)
    elif reps % 2 == 0:
        count *= SHORT_BREAK_MIN
        title_label.config(text="Break", fg=PINK)
        work_complete += "✔"
        check_mark.config(text=work_complete)
        count_down(count)
    else:
        count *= WORK_MIN
        title_label.config(text="Work", fg=GREEN)
        count_down(count)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def format_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    return '{:02d}:{:02d}'.format(minutes, seconds)


def count_down(count):
    if count > 0:
        global timer_id
        if count > 0:
            if count == 10:
                # Play ticking sound when count is less than or equal to 10
                play_sound(SOUND_PATH)
        canvas.itemconfig(timer_text, text=format_time(count))
        timer_id = window.after(1000, count_down, count - 1)
    else:
        global reps
        if reps % 8 == 0:
            reset_timer()
        else:
            start_timer()

# ---------------------------- SOUND MECHANISM ------------------------------- #


def play_sound(sound_file: str):
    winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(row=2, column=2)

check_mark = Label(text=work_complete, fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
check_mark.grid(row=3, column=1)

img = PhotoImage(file="assets/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text=format_time(0), font=(FONT_NAME, 35, "bold"), fill="#ffffff")
canvas.grid(row=1, column=1)


window.mainloop()
