# Biblioteca Digital Clássica

A modern, responsive ASP.NET Core MVC web application acting as a digital catalog for classic literature. It provides a fluid user experience mimicking a Single Page Application (SPA) by utilizing `localStorage` and client-side JavaScript.

## Features

- **Dynamic Catalog:** A horizontal scrolling catalog with hardcoded classic literature data injected directly from the `BibliotecaController`. No database or Entity Framework is required.
- **Real-time Search:** A search bar on the homepage allows users to instantly filter the catalog by book title, author, or genre without reloading the page.
- **Favorites System:** Users can add and remove books from their favorites. This state is persisted in the browser's `localStorage` (`bibliotecaFavoritos`).
- **SPA-like Navigation:** When a user selects a book or author, the data is pushed to `localStorage` and a generic view is loaded which dynamically displays the content.

## How to Run

Make sure you have the .NET 10.0 SDK installed. From the root directory:

```bash
# Build the project
dotnet build

# Run the project locally
dotnet run
```

The application will typically start on `http://localhost:5239`. Open that URL in your browser to explore the catalog.

## Static Prototypes

For UI development isolated from the ASP.NET Core engine, see the `WEB3/` directory which contains static HTML/CSS/JS mockups. See `WEB3/README.md` for running instructions.