# Turtle Crossing Game

A classic arcade-style crossing game built in Python using the `turtle` graphics module. Navigate your turtle safely across a busy, multi-lane highway packed with randomly generated traffic. Each successful crossing advances you to the next level, increasing the speed of the oncoming vehicles!

---

## Features

* **Object-Oriented Architecture:** Programmed using highly structured, modular Python classes (`Player`, `Cars`, `Level`) ensuring clean separation of concerns.
* **Precise Rectangular Collision Detection:** Outperformed standard circular radius detection by building a custom coordinate-based hitbox ($X$ and $Y$ dimensions handled independently) to map perfectly to the dimensions of the rectangular cars.
* **Memory Optimization (Object Pooling):** Instead of continuously instantiating and destroying car objects in memory, the game initializes a static pool of 20 vehicles and loops them seamlessly using an efficient teleportation/recycling technique.
* **Configurable Setup:** Fully refactored to eliminate "magic numbers," centralizing game configurations (screen scaling, boundary thresholds, speed increments) into clean uppercase constants for rapid balancing.

---

## Installation & Execution

### Prerequisites
Make sure you have Python 3 installed on your machine. The `turtle` module comes pre-installed with the standard Python library.

### Steps to Run
1. Clone this repository or download the source code files.
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the following command:

```bash
python main.py
