# 🌌 Stranger Things: Battle for Hawkins

<div align="center">

![Stranger Things](https://img.shields.io/badge/Stranger%20Things-Battle%20Game-purple?style=for-the-badge&logo=netflix)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.5+-green?style=for-the-badge)

**A dramatic, turn-by-turn battle simulation game inspired by the world of Stranger Things**  
*Built using Python and the principles of Object-Oriented Programming (OOP)*

[🎮 **PLAY NOW**](#-how-to-play) • [📖 **FEATURES**](#-game-features) • [👥 **CHARACTERS**](#-characters) • [🏗️ **ARCHITECTURE**](#-architecture)

---

</div>

## 🎯 Game Overview

In the quiet town of **Hawkins, Indiana**, strange portals have opened to the **Upside Down**, a terrifying alternate dimension. This rift has unleashed powerful and terrifying entities—**Demogorgon**, **Mind Flayer**, and **Vecna**—into the real world.

A group of young **heroes**—**Eleven**, **Dustin**, **Mike**, and others—have taken it upon themselves to protect Hawkins. With their unique powers and teamwork, they must fight to close the rift and defeat these supernatural **enemies** once and for all.

<div align="center">

### 🌟 **Choose Your Battle Experience** 🌟

</div>

---

## 🎮 How to Play

### 🚀 **Quick Start**

1. **Install Dependencies:**
   ```bash
   pip install pygame
   ```

2. **Launch the Game:**
   ```bash
   python run_game.py
   ```

3. **Choose Your Version:**
   - 🎯 **Basic Version**: Simple graphics with character sprites and health bars
   - ✨ **Aesthetic Version**: Beautiful design with custom starry background, smooth animations, and modern UI

---

## 🎨 Game Features

<div align="center">

| Feature | Basic Version | Aesthetic Version |
|---------|---------------|-------------------|
| 🎮 **Interactive UI** | ✅ | ✅ |
| 🖼️ **Character Sprites** | ✅ | ✅ |
| ❤️ **Health Bars** | ✅ | ✅ |
| 📜 **Battle Log** | ✅ | ✅ |
| 🎵 **Sound Effects** | ✅ | ✅ |
| 🌟 **Custom Background** | ❌ | ✅ |
| ✨ **Animations** | ❌ | ✅ |
| 🎨 **Modern UI** | ❌ | ✅ |

</div>

### 🎯 **Core Gameplay**
- **Turn-based combat** between heroes and enemies
- **Real-time health tracking** with visual health bars
- **Dynamic battle log** showing all combat events
- **Character-specific abilities** and special moves
- **Victory/defeat conditions** - heroes vs enemies

---

## 👥 Characters

### 🛡️ **Heroes**

| Character | Power | Special Move | Emoji |
|-----------|-------|--------------|-------|
| **Eleven** | 30 | Telekinesis | 👩‍🔬 |
| **Dustin** | 25 | Sonic Boom Gadget | 🧢 |
| **Mike** | 22 | Sword Strike | ⚔️ |

### 👹 **Enemies**

| Character | Power | Special Move | Emoji |
|-----------|-------|--------------|-------|
| **Demogorgon** | 20 | Claw Slash | 👹 |
| **Mind Flayer** | 28 | Shadow Tentacles | 🕷️ |
| **Vecna** | 26 | Psychic Blast | 🧠 |

---

## 🏗️ Architecture

### 🧠 **OOP Concepts Used**

<div align="center">

| Concept | Implementation | Description |
|---------|---------------|-------------|
| **🔄 Abstraction** | Base `Character` class | Abstract methods for common behavior |
| **📦 Encapsulation** | Protected attributes | Health, name, and power are protected |
| **🧬 Inheritance** | Hero/Enemy classes | Inherit from Character base class |
| **🎭 Polymorphism** | Custom `attack()` methods | Each character has unique attack behavior |

</div>

### 📁 **Project Structure**
```
Stranger Things Battle Game/
├── 🎮 main.py                 # Console version
├── 🎯 game_frontend.py        # Basic graphical version
├── ✨ game_simple_aesthetic.py # Aesthetic version
├── 🚀 run_game.py            # Game launcher
├── 📦 Characters/
│   ├── heroes.py             # Hero character classes
│   └── enemies.py            # Enemy character classes
├── ⚔️ battle_manager.py      # Battle logic controller
├── 🎨 Assets/                # Images, sounds, music
└── 📖 readme.md              # This file
```

---

## 🎯 Assignment Objectives

This project demonstrates mastery of:

- ✅ **Clear OOP design** using abstract base classes, method overriding, and private state
- ✅ **Multiple character types** - heroes and enemies with specialized powers
- ✅ **Centralized battle manager** controlling turn-by-turn logic
- ✅ **Dynamic storytelling** with console-based battle logs
- ✅ **Graphical user interface** with Pygame integration
- ✅ **Multiple game versions** with different visual styles

---

## 🛠️ Technical Details

### **Dependencies**
- **Python 3.8+**
- **Pygame 2.5+**

### **Installation**
```bash
# Clone the repository
git clone <repository-url>
cd Stranger-Things-Battle-Game

# Install dependencies
pip install -r requirements.txt

# Run the game
python run_game.py
```

### **Controls**
- **Mouse**: Click buttons to interact
- **Start Battle**: Begin a new game
- **Next Turn**: Process the next round of attacks
- **Reset Game**: Return to main menu

---

## 🌟 Screenshots

<div align="center">

### 🎮 Basic Version
*Simple and clean interface with character sprites*

### ✨ Aesthetic Version  
*Beautiful starry background with modern UI*

</div>

---

## 🤝 Contributing

Feel free to contribute to this project! Some ideas:
- 🎨 Add new character designs
- 🎵 Include more sound effects
- 🎮 Create new game modes
- 🖼️ Improve visual effects

---

## 📄 License

This project is created for educational purposes to demonstrate Object-Oriented Programming concepts in Python.

---

<div align="center">

### 🏆 **Ready to Battle for Hawkins?** 🏆

**Join the heroes in their fight against the enemies!**

[🎮 **START PLAYING NOW**](#-how-to-play)

---

*Made with ❤️ for Stranger Things fans and Python developers*

</div>

