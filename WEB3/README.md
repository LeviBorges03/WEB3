# WEB3 Static Prototype

The `WEB3` directory contains a purely static representation of the application's UI. It is built entirely with standard HTML, CSS, and vanilla JavaScript without any ASP.NET Core backend dependencies.

## Purpose

- **Rapid Prototyping**: Allows UI/UX designers or developers to tweak styling (e.g., modern layouts, pill-shaped buttons) without running a .NET environment.
- **Sandbox**: A place to experiment with standalone features like the `localStorage` favorites system and JavaScript interactivity.
- **Syncing**: Changes made here should act as a blueprint and must be carefully ported over to the main Razor Views (`Views/`) when finalized.

## How to View

You can run a simple HTTP server to view these prototypes in your browser:

1. Open your terminal and navigate into this directory:
   ```bash
   cd WEB3
   ```
2. Start Python's built-in HTTP server:
   ```bash
   python3 -m http.server 8000
   ```
3. Open your browser and navigate to `http://localhost:8000`. You can test out pages like `/Livro` or `/Autor`.
