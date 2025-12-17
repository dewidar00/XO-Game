# 🎮 XO Game - Tic Tac Toe

A classic Tic-Tac-Toe game with an **unbeatable AI** powered by the Minimax algorithm.

```
  ╔═══════════════════════════════════════════╗
  ║        ██╗  ██╗ ██████╗                   ║
  ║        ╚██╗██╔╝██╔═══██╗                  ║
  ║         ╚███╔╝ ██║   ██║                  ║
  ║         ██╔██╗ ██║   ██║                  ║
  ║        ██╔╝ ██╗╚██████╔╝                  ║
  ║        ╚═╝  ╚═╝ ╚═════╝                   ║
  ╚═══════════════════════════════════════════╝
```

## 🚀 Quick Start

```bash
python xo_game.py
```

## 📋 Requirements

- Python 3.x
- No external dependencies!

## 🎯 How to Play

1. Run the game
2. Choose your symbol: **X** (goes first) or **O**
3. Enter a position number (1-9) to place your mark:

```
     1 │ 2 │ 3
    ───┼───┼───
     4 │ 5 │ 6
    ───┼───┼───
     7 │ 8 │ 9
```

4. Try to get 3 in a row before the AI does!

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **Unbeatable AI** | Powered by Minimax algorithm |
| 🎨 **Clean UI** | ASCII art interface with box-drawing |
| ⏳ **Thinking Animation** | AI shows "thinking" feedback |
| 🔄 **Play Again** | Replay without restarting |
| ✅ **Input Validation** | Handles invalid inputs gracefully |

## 🧠 About Minimax Algorithm

The AI uses the **Minimax algorithm** - a decision-making algorithm for two-player games.

### How it works:

1. **Maximizer (AI)**: Tries to get the highest score
2. **Minimizer (Player)**: Tries to get the lowest score
3. **Scoring**:
   - AI wins: `+10`
   - Player wins: `-10`
   - Draw: `0`

The algorithm recursively explores **every possible move** and assumes both players play optimally. This makes the AI **impossible to beat** - the best outcome you can achieve is a draw!

```
        AI Move
        /  |  \
      /    |    \
   -10    0     +10
   (lose) (draw) (win)
         ↑
    AI picks this!
```
<img width="569" height="684" alt="image" src="https://github.com/user-attachments/assets/552ac19d-188e-4fea-ba53-fb440368cbc6" />


## 📁 Project Structure

```
xo_game_project/
├── xo_game.py    # Main game file
└── README.md     # This file
```

## 🎮 Game Preview

```
        ┌───────────────────────┐
        │     GAME  BOARD       │
        └───────────────────────┘

             ┌───┬───┬───┐
             │ X │ O │ 3 │
             ├───┼───┼───┤
             │ 4 │ X │ 6 │
             ├───┼───┼───┤
             │ O │ 8 │ X │
             └───┴───┴───┘
```

## 🏆 Can You Beat the AI?

**Spoiler**: No! 😄

The Minimax algorithm guarantees optimal play. If you play perfectly, you'll get a draw. Any mistake, and the AI wins!

## 📝 License

Free to use and modify. Have fun!


