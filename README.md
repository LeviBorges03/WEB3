# Biblioteca Web

A Biblioteca Web is a modern ASP.NET Core MVC application designed to showcase a digital catalog of classic literature.

## Features

- **Dynamic Catalog**: A visual grid of classic books with cover colors automatically matching their theme.
- **Client-Side Navigation**: Utilizes a SPA-like feel by transferring data between pages (`Index`, `Livro`, `Autor`) via HTML5 `localStorage` without requiring full database roundtrips for details.
- **Real-Time Search**: Users can instantly filter the catalog by book title or author name directly on the home page.
- **Favorites System**: Users can save their favorite books to a personalized list. Favorited books are visibly marked with a ⭐ in the catalog, and their state persists across browsing sessions via `localStorage`.

## Technologies

- **Backend**: C# with ASP.NET Core MVC (net10.0 target)
- **Frontend**: HTML5, CSS3 (Custom properties, Flexbox/Grid), Vanilla JavaScript
- **State Management**: Browser `localStorage`

## How to Run Locally

1. Ensure you have the .NET 10 SDK installed.
2. Clone this repository.
3. Open a terminal in the project root.
4. Run the build command to restore dependencies and compile the code:
   ```bash
   dotnet build
   ```
5. Start the development server:
   ```bash
   dotnet run
   ```
6. Open your web browser and navigate to the URL provided in the console output (typically `http://localhost:5239`).

### Troubleshooting

- If you encounter an "Address already in use" error for port 5239, kill the blocking process by running: `kill $(lsof -t -i :5239)`
- The project currently does not use a database (Entity Framework has been removed). All model data is hardcoded within `BibliotecaController.cs` for demonstrative purposes.
