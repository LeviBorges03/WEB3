# Biblioteca Clássica

A modern and fluid ASP.NET Core MVC application representing a curated digital library of classic books.

## Features

- **Dynamic Catalog**: A scrollable catalog of classic literature (from Machado de Assis to J.K. Rowling), showing covers and info dynamically.
- **Search System**: A responsive search bar on the homepage that filters titles and authors in real-time.
- **Favorites System**: Users can click the ⭐ icon on book cards or the detail pages to save books to their personal list. This state is saved across reloads using `localStorage`.
- **SPA-Like Navigation**: Transitions between the catalog, book details, and author pages are handled on the client-side via `localStorage` state management, ensuring a seamless experience without heavy server round-trips.
- **Responsive UI**: A relaxed, elegant UI leveraging modern CSS variables, flexbox, and grid layouts.

## Architecture & Technology

- **Backend**: C# 11, ASP.NET Core MVC (Targeting .NET 10.0).
- **Frontend Engine**: Razor Views (`.cshtml`).
- **Styling**: Custom CSS (`wwwroot/css/biblioteca.css`).
- **Data Layer**: Hardcoded model collections inside the Controllers (No database, no Entity Framework).

## How to Run Locally

### Requirements
- .NET SDK 10.0 (or matching your installed version).

### Running the App
1. Open a terminal in the root directory.
2. If the port 5239 is in use, kill the process first: `kill $(lsof -t -i :5239)`.
3. Run the application: `dotnet run`.
4. Open your browser and navigate to the printed local URL (e.g., `http://localhost:5239`).

## The `WEB3` Directory

The `WEB3/` folder is an isolated, static UI prototype playground (pure HTML/CSS/JS). It is used to design and test frontend changes without booting up the ASP.NET Core runtime. See `WEB3/README.md` for more details.
