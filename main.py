from tkinter import *
import math
import pygame
#from random import choice
# ---------------------------- CONSTANTS ------------------------------- #
AMARILLO = "#FFF7AE"
BREAK="#E4D8DC"
WORK="#3c9d9b"
SUPER_BREAK="#FF7C7C"
GREEN = "#9bdeac"
FONT_NAME = "Open Sans"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
pygame.mixer.init()
reps = 0
timer= None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    time.config(text="00:00")
    timer_title.config(text="Timer")
    check.config(text="")
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global fondo
    reps += 1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_title.config(text="Super Break", fg=SUPER_BREAK)
        time.config(fg=SUPER_BREAK)
        fondo = PhotoImage(file="descanso6.png")
        canvas.create_image(250, 140, image=fondo)

    elif reps % 2 == 0:
        count_down(short_break)
        timer_title.config(text="Break", fg=BREAK)
        time.config(fg=BREAK)
        fondo = PhotoImage(file="descas5.png")
        canvas.create_image(250, 140, image=fondo)

    else:
        count_down(work_sec)
        timer_title.config(text="Work", fg=WORK)
        time.config(fg=WORK)
        fondo = PhotoImage(file="Trabajo1.png")
        canvas.create_image(250, 140, image=fondo)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    #minutos
    min = math.floor(count / 60)
    #segundos
    seg= count % 60

    if seg == 0 :
        seg = "00"

    elif seg < 10 :
         seg = f"0{seg}"

    if min == 0:
        min = "00"
    elif min < 10:
        min = f"0{min}"

    time.config(text=f"{min}:{seg}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)

    else:
        start_timer()
        marks=""
        work_sessions=(math.floor(reps/2))
        for _ in range(work_sessions):
            marks += "✔"
            pygame.mixer.music.load("010762485_prev.mp3")
            pygame.mixer.music.play()
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("2FV Pomodoro")
window.config(pady=100,padx=100,bg=AMARILLO)

start=PhotoImage(file="Start.png")
reset=PhotoImage(file="reset.png")


canvas = Canvas(width=500,height=300,bg=AMARILLO, highlightthicknes=0)
fondo = PhotoImage(file="tomato.png")
canvas.create_image(250,150,image=fondo)
#timer_text=canvas.create_text(250,283,text="00:00",fill="#05A19C",font=((FONT_NAME),35,"bold"))
canvas.grid(column=1,row=1)

timer_title = Label(text="Timer", font=((FONT_NAME), 40), bg=AMARILLO, fg="#05A19C")
timer_title.grid(column=1, row=0)


time= Label(text="00:00",font=((FONT_NAME),40),bg=AMARILLO,fg="#05A19C")
time.grid(column=1,row=2)

check = Label(font=((FONT_NAME),20),bg=AMARILLO,fg=GREEN)
check.grid(column=1,row=3)

#Botton Start
star_b = Button(image=start, bg=AMARILLO, borderwidth=0, command=start_timer)
star_b.grid(column=0,row=2)

reset_b = Button(image=reset, bg=AMARILLO, borderwidth=0, command=reset_timer)
reset_b.grid(column=2,row=2)





window.mainloop()