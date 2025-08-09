
# ⏰ Simple Alarm Clock (Python + Tkinter)

A beginner-friendly alarm clock application built with Python's Tkinter library.  
It displays the current time, allows users to set an alarm, and plays a beep sound when the alarm goes off.  
The interface also flashes to visually notify the user.

---

## ✨ Features

- 🕒 **Live Clock** — Displays the current time and updates every second.
- ⏰ **Set Alarm** — Choose an alarm time in `HH:MM:SS` format.
- 🔔 **Ringing Alert** — Beep sound and flashing background when alarm triggers.
- 🛑 **Stop Alarm** — Cancel the alarm at any time.
- ✅ **Input Validation** — Ensures correct time format before setting the alarm.

---

## 📦 Requirements

- Python **3.x**
- `tkinter` (comes pre-installed with Python)
- `winsound` (built-in module for Windows; alarm sound works only on Windows)

---

## ▶️ How to Run

1. **Clone or Download** the repository:
    ```bash
    git clone https://github.com/yourusername/alarm-clock.git
    cd alarm-clock
    ```

2. **Run the script**:
    ```bash
    python alarm_clock.py
    ```

3. **Usage**:
   - Enter the alarm time in the format `HH:MM:SS` (e.g., `14:30:00`).
   - Click **Set Alarm**.
   - The clock will monitor and ring at the set time.
   - Click **Stop Alarm** to turn off the ringing.

---

## 🖼️ Screenshot

![Alarm Clock Screenshot](screenshot.png)  
*(Optional: Add your own screenshot here)*

---

## 📌 Notes

- Alarm sound works only on **Windows** because it uses the `winsound` module.
- On Linux/Mac, you can replace the `winsound.Beep()` function with another sound library like `playsound` or `pygame`.

---

## 🛠️ Code Structure

````

alarm\_clock.py
├── update\_clock()  # Updates clock and checks alarm
├── start\_alarm()   # Starts alarm sound and flashing
├── flash\_bg()      # Alternates window background color
├── play\_beep()     # Plays beep sound repeatedly
├── set\_alarm()     # Validates and sets alarm time
├── stop\_alarm()    # Stops alarm and resets UI

```


🙌 Author

Made by **Robin Arulmanikam**

**Department** : Computer Engineering
