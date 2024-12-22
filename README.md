# Pygame Core

## Overview

**Pygame Core** is a reusable module designed to streamline the development of 2D games using the Pygame library. It provides foundational components such as game loops, scene management, input handling, and reusable entity logic to simplify and accelerate game development.

---

## Features

- **Game Loop Management**: Easily manage the game loop and FPS.
- **Scene Management**: Transition between scenes (e.g., menus, gameplay, game over).
- **Entity System**: Base class for game objects with built-in movement and rendering support.
- **Input Handling**: Centralized input management for keyboard, mouse, or gamepad.
- **Asset Management**: Efficient loading and caching of images, sounds, and other resources.
- **Utility Functions**: Common tools like collision detection and screen wrapping.

---

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/pygame-core.git
cd pygame-core
pip install -r requirements.txt
```

---

## Usage

To use the Pygame Core module in your game project:

1. Include the `core/` directory in your game project.
2. Import the required modules from `core`.

### Example: Initializing a Game

Here’s an example of how to create a game using Pygame Core:

```python
import pygame
from core import Game, Scene, SceneManager

class MainMenu(Scene):
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return Gameplay(self.screen)

    def render(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Press Enter to Start", True, (255, 255, 255))
        self.screen.blit(text, (150, 300))

class Gameplay(Scene):
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.screen.fill((30, 30, 30))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Core Example")

    manager = SceneManager(MainMenu(screen))
    game = Game(screen)
    game.run(manager)
    pygame.quit()
```

---

## Project Structure

```plaintext
pygame-core/
│
├── core/                   # Core reusable module
│   ├── game.py             # Game loop management
│   ├── scene.py            # Scene management
│   ├── input_manager.py    # Input handling
│   ├── entity.py           # Base entity class
│   ├── asset_manager.py    # Asset loading and caching
│   ├── settings.py         # Default settings
│   ├── utils.py            # Utility functions
│   └── __init__.py         # Module initialization
│
├── tests/                  # Unit tests
│   ├── test_game.py        # Tests for game.py
│   ├── test_scene.py       # Tests for scene.py
│   ├── test_entity.py      # Tests for entity.py
│   └── conftest.py         # Test setup and fixtures
│
├── assets/                 # Placeholder for assets (images, sounds, etc.)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## Testing

Run the tests to ensure the core module works as expected:

```bash
pytest
```

Also run a Pylint score command so we make sure to follow some great guidelines

```bash
pylint score
```

---

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

Please ensure all tests pass before submitting.
