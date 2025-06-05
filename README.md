# Tic-Tac-Toe Python 🕹️

A simple console-based Tic-Tac-Toe game implemented in Python.

This project allows two players to take turns entering coordinates, with full input validation, win condition checks, and proper endgame messages.

## 📂 Project Structure

```
tic-tac-toe-python/
├── main.py
├── game/
│   ├── __init__.py
│   ├── board.py
│   ├── logic.py
│   └── input_handler.py
```

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/tu-usuario/tic-tac-toe-python.git
cd tic-tac-toe-python
```

2. Run the game:

```bash
python main.py
```

> Make sure you have Python 3 installed.

## 🎮 Features

- 3x3 game board
- Player turns with `"X"` and `"O"`
- Win detection: rows, columns, diagonals
- Draw detection
- Input validation:
  - Only numbers
  - In range (1–3)
  - Cell not occupied
- Clear board display

## ✍️ Author

Created by Angel Gama as part of the [Python Developer course](https://hyperskill.org/courses/2) on [Hyperskill](https://hyperskill.org/), a project-based learning platform powered by JetBrains. It was completed as a practice exercise for learning Python programming fundamentals.

## 📄 License

This project is open source and free to use for learning purposes.
