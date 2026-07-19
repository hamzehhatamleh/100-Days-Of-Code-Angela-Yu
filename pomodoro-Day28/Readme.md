# Pomodoro Timer 

Hey there! This is a clean, simple desktop Pomodoro Timer I built using Python and Tkinter to help stay focused and crush daily goals. It breaks your day into standard 25-minute focus blocks separated by quick breaks to keep your brain fresh.

## Why use it?
- **Zero Stress Tracking**: It handles the timing logic for you, automatically switching between your deep-work sessions, short breaks, and long breaks.
- **Visual Milestones**: Every time you finish a work session, a green checkmark (`✔`) pops up so you can see your progress build up over the day.
- **Accident Proof**: The Start button safely locks while a session is running, so you won't accidentally double-click it and break the countdown.

## The Workflow
1. **Focus**: 25 mins
2. **Short Break**: 5 mins
*(Repeat this loop 4 times)*
3. **Long Break**: 20 mins (Time to stretch or get a coffee!)

---

## Quick Setup

### 1. What you need
Just make sure you have Python 3 installed on your computer. You can check by opening your terminal and typing:
```bash
python --version
```

### 2. File Layout
Keep things organized! Make sure your folder looks like this before running the code, otherwise the canvas won't know where to find the graphics:
```text
├── main.py          # The script file
└── tomato.png       # The asset image file
```

### 3. Let's Run It
Open up your terminal inside the project directory and type:
```bash
python main.py
```

---

## How to use it

- **Start**: Kicks off the timer and changes colors depending on whether it's work or break time.
- **Reset**: Instantly kills the background timer, wipes your checkmarks, and brings you right back to square one (`25:00`).
