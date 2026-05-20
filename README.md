# Biblioteca - ASP.NET Core MVC

Este projeto é uma aplicação de catálogo de livros baseada em ASP.NET Core MVC, que simula uma experiência de Single Page Application (SPA) utilizando recursos nativos do navegador e JavaScript.

## Funcionalidades

- **Catálogo de Clássicos**: Uma vitrine de livros com navegação em carrossel e um grid responsivo que pode ser expandido.
- **Pesquisa em Tempo Real**: Uma barra de pesquisa na página principal (`Index`) que permite filtrar o catálogo instantaneamente por título ou autor. A pesquisa é tratada localmente sem recarregar a página.
- **Navegação SPA-Like**: A aplicação evita recarregamentos completos de página transmitindo dados de livros e autores via `localStorage`, criando uma experiência fluida para o usuário.
- **Sistema de Favoritos (Client-Side)**: Os usuários podem adicionar ou remover livros de sua lista de favoritos na página de detalhes do livro. Este estado é preservado no `localStorage` sob a chave `bibliotecaFavoritos`.
- **UI Moderna**: Design responsivo com CSS Flexbox/Grid, animações suaves, e componentes elegantes.

## Arquitetura e Decisões Técnicas

- **Frontend sem Frameworks**: Todo o comportamento interativo (carrossel, filtros, favoritos, roteamento SPA) é feito usando **Vanilla JavaScript** e `localStorage`.
- **Armazenamento Hardcoded**: Por ser um projeto de demonstração e focado em UI/UX, os dados são gerenciados em listas estáticas no controlador (`BibliotecaController.cs`) para alta performance e rápida inicialização, sem necessidade de configurar um banco de dados relacional.
- **Componentes Visuais**: As capas dos livros não dependem de arquivos de imagem. Elas utilizam cores em código HEX associadas ao tema da obra (`CorCapa`) combinadas com CSS para criar uma estética limpa.
