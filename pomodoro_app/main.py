from tkinter import *
import math
# text='✔️'
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    complete_mark.config(text='')
    label_1.config(text='Timer')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    window.deiconify()
    window.lift()
    window.focus_force()

    if reps % 8 == 0:
        countdown(long_break_sec)
        label_1.config(text= "Break", fg= RED )
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_1.config(text="Break", fg=PINK)
    else:
        countdown(work_min_sec)
        label_1.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global a
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark =""
        for _ in range(math.floor(reps / 2)):
            mark += '✔️'
            if len(mark) > 8:
                mark = '✔️'
        complete_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(500, 500)
window.maxsize(500, 500)
window.config(padx=10, pady=10, bg=YELLOW)

label_1 = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
label_1.pack()

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(window, bg=YELLOW, height=250, width=224, highlightthickness=0)
canvas.create_image(100, 122, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 35, "bold"), fill='white')
canvas.pack()

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.place(x=100, y=385)
reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.place(x=350, y=385)

complete_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
complete_mark.place(x=180, y=440)

window.mainloop()
