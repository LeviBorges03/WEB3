# Biblioteca Digital

Este é um projeto ASP.NET Core MVC (C# / .NET 10.0) que implementa uma vitrine moderna de clássicos da literatura. O projeto destaca-se por prover uma experiência SPA (Single Page Application) fluída utilizando Vanilla JavaScript e `localStorage` para navegação entre visões, evitando o recarregamento total de página.

## Funcionalidades

*   **Catálogo Dinâmico:** Uma lista vasta de livros preenchidos a partir da Controller, com barra de busca real-time de títulos e autores na página inicial.
*   **Gestão de Favoritos:** Obras podem ser salvas em `localStorage` como favoritas através da tela de detalhes de cada livro. O ícone de ⭐ destaca as obras favoritadas diretamente no catálogo.
*   **Transição de Dados Segura:** Informações são transitadas entre Views via `localStorage` prevenidos contra XSS em JavaScript nativo.

## Como Executar

Para rodar este projeto, execute no terminal a partir do diretório raiz do projeto:

```bash
dotnet build
dotnet run
```

O servidor local normalmente iniciará em `http://localhost:5239`.

---

**Nota sobre ambiente UI/Protótipos (WEB3):**
Consulte o arquivo `WEB3/README.md` se você deseja ver e modificar apenas a base dos protótipos em HTML/CSS/JS isolados deste projeto.