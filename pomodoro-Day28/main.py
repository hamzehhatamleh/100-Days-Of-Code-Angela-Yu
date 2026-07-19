import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
BG_COLOR = "white"
BUTTON_BG = "#2ed573"
BUTTON_FG = "white"
BUTTON_ACTIVE = "#26af5f"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    if timer is not None:
        window.after_cancel(timer)

    reps = 0
    canvas.itemconfig(timer_text, text="25:00")
    Timer_Text.config(text="Timer", fg="#2ed573")
    check_label.config(text="")
    start_btn.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    start_btn.config(state="disabled")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Timer_Text.config(text="Long Break", fg="#ff4757")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timer_Text.config(text="Break", fg="#ffa502")
    else:
        count_down(work_sec)
        Timer_Text.config(text="Work", fg="#2ed573")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    mins = math.floor(count / 60)
    secs = count % 60

    timer_format = f"{mins:02d}:{secs:02d}"
    canvas.itemconfig(timer_text, text=timer_format)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # --- Calculate checkmarks FIRST using the current session count ---
        marks = ""
        # If the session that just finished was odd, it was a WORK session!
        if reps % 2 != 0:
            work_sessions = math.ceil(reps / 2)
            for _ in range(work_sessions):
                marks += "✔"
            check_label.config(text=marks)

        # --- Move to the next session ---
        start_btn.config(state="normal")
        start_timer()


# ---------------------------- WINDOWS SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=BG_COLOR)

# Title Label
Timer_Text = tk.Label(text="Timer", fg="#2ed573", bg=BG_COLOR, font=("Arial", 40, "bold"))
Timer_Text.grid(column=1, row=0, pady=(0, 20))

# Canvas Setup
canvas = tk.Canvas(width=526, height=582, highlightthickness=0, bg=BG_COLOR)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(263, 291, image=tomato_img)
canvas.image = tomato_img  # Explicit memory reference for GitHub best practices
timer_text = canvas.create_text(263, 340, text="25:00", fill="white", font=("Arial", 50, "bold"))
canvas.grid(column=1, row=1)

# Control Buttons
start_btn = tk.Button(
    text="Start",
    font=("Arial", 14, "bold"),
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground=BUTTON_FG,
    bd=0,
    padx=25,
    pady=10,
    cursor="hand2",
    command=start_timer
)
start_btn.grid(column=0, row=2)

reset_btn = tk.Button(
    text="Reset",
    font=("Arial", 14, "bold"),
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground=BUTTON_FG,
    bd=0,
    padx=25,
    pady=10,
    cursor="hand2",
    command=reset_timer
)
reset_btn.grid(column=2, row=2)

# Checkmark Progress Label
check_label = tk.Label(text="", fg="#2ed573", bg=BG_COLOR, font=("Arial", 28, "bold"))
check_label.grid(column=1, row=3, pady=20)

window.mainloop()
