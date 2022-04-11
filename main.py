from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = "#373854"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# keep track of checkmarks
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
# Function to be used when 'Reset' button is clicked
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    timer_lbl.config(text="Timer")
    check_lbl.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# Function to be used when 'Start' button is clicked
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_lbl.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_lbl.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_lbl.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sesh = math.floor(reps/2)
        for _ in range(work_sesh):
            marks += "✓"
        check_lbl.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=BLUE)

timer_lbl = Label(text="Timer", fg=GREEN, bg=BLUE, font=(FONT_NAME, 40, "bold"))
timer_lbl.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset)
reset_btn.grid(column=2, row=2)

check_lbl = Label(fg=GREEN, font=(FONT_NAME, 12, "bold"))
check_lbl.grid(column=1, row=3)


window.mainloop()
