# WEB3 Static UI Prototypes

This directory contains pure HTML, CSS, and JS static files to demonstrate the UI layout and features of the library catalog independently from the ASP.NET Core backend.

## How to Run Locally

You can serve this static directory using a simple Python HTTP server:

```bash
cd WEB3
python3 -m http.server 8000
```

Then open `http://localhost:8000/Livro/` or `http://localhost:8000/Autor/` in your browser.

## Features Modeled

* **Local Storage Mocking:** JavaScript in these files mocks the `localStorage` interactions used in the main ASP.NET Core application, including the Favorites system (`bibliotecaFavoritos`) toggle.