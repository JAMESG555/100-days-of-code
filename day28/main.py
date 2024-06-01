from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
check =  "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    # #If it's the 1st/3rd/5th/7th rep:
    # if reps in [1, 3, 5, 7]:
    #     count_down(work_sec)
    # # If it's the 2nd/4th/6th rep:
    # if reps in [2, 4, 6]:
    #     count_down(short_break_sec)
    # #If it's the 8th rep:
    # if reps == 8:
    #     count_down(long_break_sec)
    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_sec == 0:
        count_sec = '00'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

fg = GREEN

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
#Title
title = Label(text="Timer", font=(FONT_NAME, 24, "bold"),fg=GREEN, bg=YELLOW, highlightthickness=0)
title.grid(column=1, row=0)
#Start Button
start_button = Button(text="Start", font=("Arial", 10, "bold"), command=start_timer)
start_button.grid(column=0, row=2)
#Reset Button
reset_button = Button(text="Reset", font=("Arial", 10, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)
#Check Mark
check_marks = Label(text=check, fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()