# Pygame Core

## Overview

**Pygame Core** is a modular and reusable library designed to simplify the development of 2D games using the Pygame library. It provides essential components for managing game loops, scenes, input handling, and utility functions, allowing developers to focus on building their game's unique features.

## Features

- **Game Loop Management**: Simplifies the main game loop with FPS control.
- **Scene Management**: Enables seamless transitions between game scenes (e.g., menus, gameplay).
- **Input Handling**: Centralized input management for keyboards or other devices.
- **Utilities**: Provides tools like collision detection and default settings.
- **Extensibility**: Designed for easy customization and expansion.

## Installation

Install the package using `pip`:

```bash
pip install pygame-pygame_core
```

## Usage

### Setting Up Your Game

Below is an example of how to use **Pygame Core** to create a simple game:

```python
import pygame
from pygame_core import Game, Scene, SceneManager


class MainMenu(Scene):
    def update(self, input_manager):
        if input_manager.is_pressed(pygame.K_RETURN):
            return Gameplay(self.screen)

    def render(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Press Enter to Start", True, (255, 255, 255))
        self.screen.blit(text, (150, 300))


class Gameplay(Scene):
    def update(self, input_manager):
        # Game logic goes here
        pass

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

### Key Components

- **`Game`**: Manages the main game loop and FPS control.
- **`Scene`**: A base class for creating game scenes with `update` and `render` methods.
- **`SceneManager`**: Handles scene transitions.
- **`InputManager`**: Provides a clean interface for checking key states.
- **`Utils`**: Includes common utilities like collision detection.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Run a pylint `pylint core`
5. Submit a pull request.

Please ensure all tests pass before submitting your PR.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Upload

> Remember to update version number in `VERSION` file and delete the dist folder before uploading.

Build:

```bash
python -m build
```

Upload:

```bash
python -m twine upload dist/*
```
