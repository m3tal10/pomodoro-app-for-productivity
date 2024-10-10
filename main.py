from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time_loop=None
reps=0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(time_loop)
    label.configure(text='Timer', fg=GREEN)
    canvas.itemconfig(timer,text='00:00')
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps%8 ==0:
        label.config(text='Long Break.', fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps%2 !=0:
        label.config(text='Work', fg=GREEN)
        count_down(WORK_MIN*60)
    elif reps%2 ==0:
        label.config(text='Break.', fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    global time_loop
    mins= count//60
    secs=count%60
    if mins<10:
        mins=f"0{mins}"
    if secs<10:
        secs=f"0{secs}"
    canvas.itemconfig(timer,text=f"{mins}:{secs}")
    if count>0:
        time_loop=window.after(1000,count_down,count-1)
    else:
        tick= ''
        start_timer()
        for _ in range(reps//2):
            tick+='✔'
        tick_label.config(text=tick)
        
 
# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title('Pomodoro App')
window.minsize(500,500)
window.config(bg=YELLOW)
window.config(padx=100,pady=50)

# Variables
tomato_image= PhotoImage(file='tomato.png')


# Canvas
canvas= Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112,image=tomato_image)
timer= canvas.create_text(103,130, text='00:00', fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)


# Labels
label= Label(text='Timer', font=(FONT_NAME,24, 'bold'), fg=GREEN, bg= YELLOW)
tick_label= Label(font=(FONT_NAME,20, 'bold'),fg=GREEN,bg=YELLOW)
tick_label.grid(column=1,row=3)
label.grid(column=1,row=0)

#Buttons 
start_btn= Button(text='Start', command=start_timer, bg=GREEN, padx=5,pady=5)
reset_btn= Button(text='Reset', command=reset, bg=RED,padx=5,pady=5)
start_btn.grid(column=0,row=2)
reset_btn.grid(column=2,row=2)

window.mainloop()