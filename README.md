# Projeto Biblioteca

Este projeto é uma aplicação web clássica voltada para atuar como vitrine e catálogo de uma biblioteca. O foco principal está na interface moderna e no fluxo de navegação que se assemelha a uma Single Page Application (SPA), usando tecnologias web do lado do cliente para a passagem de estado, mesmo sendo um projeto MVC.

## Arquitetura

- **Framework**: ASP.NET Core MVC (C# / .NET 10.0).
- **Dados**: A aplicação **não** utiliza um banco de dados (Entity Framework foi removido do projeto). Toda a base de dados de livros é "hardcoded" de forma estática nos `Controllers`, simulando o envio inicial do catálogo via modelo para as Views.
- **Passagem de Estado**: Para manter a performance e a fluidez sem recarregamento desnecessário de páginas no servidor para cada consulta detalhada, o projeto faz uso extensivo da API `localStorage` do navegador. Ao clicar em um Livro ou Autor no catálogo principal (`Index`), as informações são salvas no armazenamento local do usuário e as Views Genéricas (`Livro.cshtml`, `Autor.cshtml`) leem esse `localStorage` via JavaScript no `DOMContentLoaded` para renderizar o conteúdo adequado de forma dinâmica.

## Funcionalidades e Recursos Locais

1. **Barra de Pesquisa Dinâmica**: No catálogo (`Index`), uma barra de pesquisa filtra os livros listados em tempo real (on input). Esse filtro atua no lado do cliente (via JavaScript), modificando o `display` dos cards caso contenham o título, o autor ou o gênero inseridos.
2. **Sistema de Favoritos**: Os usuários podem marcar livros como favoritos na página de detalhes da obra. Esses livros são salvos no `localStorage` sob a chave `bibliotecaFavoritos` (um array JSON com os títulos). Na tela principal do catálogo, as obras favoritadas recebem automaticamente um ícone especial de estrela (⭐).

## Como Executar o Projeto

Certifique-se de ter o SDK do .NET 10.0 instalado. O projeto foi configurado para resolver rapidamente suas dependências em build.

Para compilar a aplicação:
```bash
dotnet build
```

Para rodar o servidor local (rodará tipicamente em `http://localhost:5239`):
```bash
dotnet run
```
**Nota:** Em ambientes de sandbox, lembre-se de rodar em plano de fundo ou monitorar o timeout do servidor: `dotnet run > dotnet_run.log 2>&1 &`.

## Protótipos Estáticos (WEB3)

A pasta `WEB3/` na raiz do projeto contém versões puramente estáticas (HTML/CSS/JS isolados) das telas, utilizadas para prototipação UI/UX de forma autônoma sem o motor ASP.NET. Mais informações no README lá contido.
