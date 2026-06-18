# WEB3 Prototypes

This directory contains pure HTML, CSS, and JavaScript files that serve as static UI prototypes for the main ASP.NET Core MVC Biblioteca application.

## Purpose

The files here are used to design, test, and iterate on the user interface and client-side logic (such as the SPA navigation using `localStorage` and the Favorites system) independently of the C# backend.

Changes to the application's layout, styles, or core frontend scripts should be tested here first or mirrored here from the main Views to ensure consistency.

## How to View

You do not need .NET to view these files. You can serve them using any standard web server.

If you have Python installed, you can quickly spin up a local server by running the following command from within this `WEB3` directory:

```bash
python3 -m http.server 8000
```

Then, navigate to `http://localhost:8000` in your web browser.