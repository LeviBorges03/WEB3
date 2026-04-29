# Biblioteca - ASP.NET Core MVC

Este projeto é uma aplicação web construída com ASP.NET Core MVC (C#) destinada a gerenciar o catálogo de uma biblioteca. O sistema utiliza `Pomelo.EntityFrameworkCore.MySql` para se conectar ao banco de dados MySQL e conta com um sistema moderno de navegação e state management no frontend utilizando SPA-like navigation via JavaScript e `localStorage`.

## Funcionalidades Principais
*   **Catálogo de Obras:** Vitrine de livros com navegação horizontal interativa.
*   **Busca Dinâmica:** Pesquisa de obras em tempo real por título ou autor através do `oninput`, garantindo fluidez e responsividade imediata (sem refresh).
*   **Sistema de Favoritos:** Possibilidade de adicionar obras a uma lista de favoritos. O sistema de favoritos é gerenciado dinamicamente via JavaScript, salvando a lista de obras na chave `bibliotecaFavoritos` (formato JSON) no `localStorage`.
*   **SPA-Like Navigation:** A transição de dados entre a página inicial, página do livro e perfil do autor acontece de forma suave utilizando o `localStorage` para transferir informações entre as Views sem a necessidade de recarregar dados do backend de forma síncrona.

## Arquitetura
A arquitetura se divide em duas partes principais:
1.  **Back-end (`ASP.NET Core`):** Responsável pelos Controllers e Views (`.cshtml`), bem como configuração da string de conexão (gerenciada no `appsettings.json` via variáveis de ambiente `ConnectionStrings__DefaultConnection`). O banco de dados utiliza a versão do servidor MySQL especificada explicitamente (ex: `8.0.40`).
2.  **Protótipo Estático (`WEB3/`):** Diretório que contém uma representação puramente HTML/CSS/JS do projeto para fim de prototipação e testes de UI isolados (sem a necessidade do .NET Core).

## Executando o Projeto
Para executar a aplicação localmente:
```bash
dotnet build
dotnet run
```