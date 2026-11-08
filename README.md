# Deep Space Navigation

**A browser-based game developed for the IFSC Game Fair 2026.**

Deep Space Navigation is a game project developed for the 2026 Game Fair at the Federal Institute of Santa Catarina (IFSC).

The project combines browser-based gameplay with a custom physical controller built using Arduino and Python, providing an alternative way to interact with the game.

**English** | [Português](README.pt-BR.md)

---

## About the Project

### Story

Humanity's future is at risk. After centuries of environmental destruction caused by human activity, Earth has become increasingly hostile to life, threatening the survival of civilization.

With humanity facing an uncertain future, an astronaut is sent on a deep-space mission with a critical objective: explore the unknown and search for new sources of life that could offer humanity a chance to survive.

In Deep Space Navigation, the player takes on the role of this astronaut, embarking on a journey through the vastness of space in search of hope for the future of humanity.

### Project Overview

The project was presented to the public during the IFSC Game Fair 2026, bringing together game development, programming, electronics, and interactive entertainment.

## Features

- Browser-based gameplay.
- Custom physical controller built with Arduino.
- Serial communication between Arduino and Python.
- Keyboard input simulation using PyAutoGUI.
- Six physical button inputs.
- Integration between hardware and software.

## Controls

The physical controller communicates with the game through the following keyboard inputs:

| Key | Action     |
| :-: | ---------- |
| `W` | Move Up    |
| `S` | Move Down  |
| `A` | Move Left  |
| `D` | Move Right |
| `F` | Take Photo |
| `Q` | Start      |

*These mappings correspond to the commands implemented in the controller software.*

## Technologies Used

### Game

- [Add the programming languages, frameworks, or game engines used]

### Hardware

- Arduino
- Physical push buttons
- USB Serial Communication

### Software

- Python
- PySerial
- PyAutoGUI
- Arduino IDE

## How the Controller Works

The project uses a physical controller connected to an Arduino board. The Arduino monitors six digital inputs and sends button events through USB serial communication.

A Python script receives these events and translates them into keyboard inputs, allowing the browser game to recognize commands from the physical controller.

### Communication Flow

```text
Physical Buttons
       |
       v
    Arduino
       |
       | Serial Communication (9600 baud)
       v
 Python Controller
       |
       | PyAutoGUI
       v
 Browser Game
```

### Arduino

The Arduino firmware monitors digital pins 2 through 7 using the `INPUT_PULLUP` configuration.

Whenever a button is pressed or released, the Arduino sends a corresponding message through Serial:

- `P:<key>` — Key pressed.
- `R:<key>` — Key released.

### Python Controller

The Python script performs the following operations:

1. Automatically searches for the connected Arduino serial port.
2. Establishes communication at 9600 baud.
3. Receives and interprets commands sent by the Arduino.
4. Simulates keyboard presses and releases using PyAutoGUI.
5. Releases all active keys when the program is terminated.

## Running the Project

### Requirements

- Python 3
- Arduino board
- Arduino IDE
- Six physical buttons
- A modern web browser

### 1. Install Dependencies

Install the required Python libraries:

```bash
pip install pyserial pyautogui
```

### 2. Upload the Arduino Firmware

Open the Arduino sketch in the Arduino IDE and upload the program to the board.

### 3. Connect the Controller

Connect the Arduino to your computer using a USB cable.

### 4. Run the Python Controller

Execute the following command in the terminal:

```bash
python Controle_do_jogo.py
```

The script will attempt to automatically identify the Arduino's serial port.

### 5. Start Playing

Open the game in your browser and click on the game screen to ensure it has keyboard focus. You can then start playing using the physical controller.

To terminate the controller, press `CTRL + C` in the terminal.

## Project Context

**Event:** IFSC Game Fair 2026
**Institution:** Instituto Federal de Santa Catarina (IFSC)
**Project:** Deep Space Navigation

The project was developed and presented as part of an academic game fair, combining programming, electronics, and interactive game development.

## ![Gameplay](Assets/Screenshots/gameplay.png) 
## ![photo](Assets/Screenshots/gameplay.png)
## ![menu](Assets/Screenshots/gameplay.png)

## License
## License

This project is licensed under the [MIT License](LICENSE).
