from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    global marks
    global reps
    marks = ""
    reps = 0
    label_timer.config(text="Timer", bg=YELLOW, fg=RED, font=(FONT_NAME, 35, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    label_check.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    global marks

    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)


    if reps == 8:
        count_down(long_break_sec)
        label_timer.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 35, "bold"))
        marks += "✅"
        label_check.config(text=marks, fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 35, "bold"))
        marks += "✅"
        label_check.config(text=marks, fg=GREEN)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    count_min = int((count - int(count_sec)) / 60)
    if count_min<10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        # marks = ""
        # work_sessions = math.floor(reps/2)
        # for _ in range(work_sessions):
        #     marks += "✅"
        # label_check.config(text = marks, fg = GREEN)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodore")
window.config(padx=50, pady=25, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



start_button = Button(text="START", command=start)
start_button.grid(column=0, row=2)


reset_button = Button(text="RESET", command=reset)
reset_button.grid(column=2, row=2)

label_timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

label_check = Label(text="", fg=GREEN, font=(FONT_NAME, 11, "bold"))
label_check.config(padx=0, pady=10)
label_check.grid(column=1, row=3)


window.mainloop()