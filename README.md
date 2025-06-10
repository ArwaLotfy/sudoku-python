# sudoku-python

A console-based Sudoku puzzle game built in Python that allows users to play, save, and resume games with real-time validation and user interaction. Designed with a focus on logic, file handling, and clean console UI.

## 🎮 Features
- Text-based interface with a visually structured Sudoku board
- Validates player moves according to Sudoku rules (row, column, subgrid)
- Random cell filling for each new game
- Save and resume game functionality using local text files
- Tracks reserved (pre-filled) cells to prevent modification
- Graceful exit options with game state preservation

## 🧠 Concepts Used
- File handling
- 2D arrays and matrix manipulation
- Input validation and exception handling
- Game state saving/loading
- Randomized board generation

## 📂 File Structure
- `sudoku.py`: Main Python file
- `sudukoo.txt`: Text file with the base empty Sudoku board
- `yourname.txt`: Auto-generated save file for the player’s game

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Place a valid `sudukoo.txt` file (9x9 matrix of 0s and starting numbers) in the same directory.
3. Run the game:


