import tkinter as tk
import time
import winsound  # Works only on Windows

# Tkinter setup
window = tk.Tk()
window.title("Simple Alarm Clock")
window.geometry("400x300")
window.config(bg="#f0f0f0")

# Global alarm state
alarm_time = ""
is_ringing = False

# Update current time every second
def update_clock():
    current = time.strftime("%H:%M:%S")
    clock_label.config(text=f"Time: {current}")

    if alarm_time and current == alarm_time and not is_ringing:
        start_alarm()
    window.after(1000, update_clock)

# Start alarm ring
def start_alarm():
    global is_ringing
    is_ringing = True
    status_label.config(text="Alarm Ringing!", fg="red")
    flash_bg()
    play_beep()

# Flashing background loop
def flash_bg():
    if is_ringing:
        current_color = window.cget("bg")
        new_color = "yellow" if current_color == "#f0f0f0" else "#f0f0f0"
        window.config(bg=new_color)
        window.after(500, flash_bg)
    else:
        window.config(bg="#f0f0f0")  # Reset color

# Beep sound
def play_beep():
    if is_ringing:
        winsound.Beep(1000, 500)  # 1000Hz for 0.5 sec
        window.after(1000, play_beep)

# Set alarm
def set_alarm():
    global alarm_time, is_ringing
    input_time = alarm_entry.get().strip()
    try:
        time.strptime(input_time, "%H:%M:%S")  # Validates format
        alarm_time = input_time
        is_ringing = False
        status_label.config(text=f"Alarm Set for {alarm_time}", fg="green")
    except ValueError:
        status_label.config(text="Invalid format! Use HH:MM:SS", fg="red")

# Stop alarm
def stop_alarm():
    global alarm_time, is_ringing
    alarm_time = ""
    is_ringing = False
    status_label.config(text="Alarm Stopped", fg="blue")
    window.config(bg="#f0f0f0")

# GUI Elements
tk.Label(window, text="Set Alarm (HH:MM:SS)", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

alarm_entry = tk.Entry(window, font=("Arial", 14), justify="center")
alarm_entry.pack(pady=5)

tk.Button(window, text="Set Alarm", font=("Arial", 12), bg="#4CAF50", fg="white", command=set_alarm).pack(pady=10)
tk.Button(window, text="Stop Alarm", font=("Arial", 12), bg="red", fg="white", command=stop_alarm).pack(pady=5)

clock_label = tk.Label(window, text="Time: --:--:--", font=("Arial", 16, "bold"), bg="#f0f0f0")
clock_label.pack(pady=10)

status_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
status_label.pack()

# Start clock
update_clock()

window.mainloop()
