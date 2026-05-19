# Biblioteca Digital

Um projeto de catálogo de livros digital e protótipo de sistema para visualização e leitura.

## Arquitetura e Tecnologias

* **ASP.NET Core MVC (C#):** O backend é uma aplicação ASP.NET Core que utiliza o padrão Model-View-Controller (MVC) para o gerenciamento e exibição de dados. A aplicação foi compilada com alvo no framework `.NET 10.0`. O sistema *não* utiliza um banco de dados real nem ferramentas como o Entity Framework. Os dados são embutidos e gerenciados de forma estática nos `Controllers`.
* **HTML/CSS/JS (Frontend):** A interface do usuário é construída com um estilo responsivo, focado em elementos elegantes (como botões arredondados e transições fluidas). O sistema emprega uma navegação SPA (Single Page Application) leve que reduz as recargas completas de página transferindo dados através do `localStorage` do navegador para exibição de detalhes e perfis dinamicamente.
* **WEB3 Prototype:** O projeto contém um diretório `/WEB3/` que funciona como um ambiente de prototipagem isolado e puramente estático (HTML, CSS e JS, sem o backend ASP.NET Core). Quaisquer alterações de layout, regras de negócios ou documentação devem manter a paridade com ambos os ambientes (o projeto principal MVC e o `WEB3/`).

## Recursos e Funcionalidades

* **Pesquisa de Obras:** Uma barra de pesquisa interativa foi implementada na tela principal do catálogo. A lógica utiliza JavaScript e `oninput` para filtrar dinamicamente as obras exibidas por título ou autor, manipulando diretamente o estilo das tags de exibição dos elementos filtrados.
* **Sistema de Favoritos:** O usuário pode favoritar obras a partir da página de detalhes do livro. O estado dos itens favoritos é gerenciado integralmente no lado do cliente, salvo no `localStorage` sob a chave `bibliotecaFavoritos` (um array JSON com os títulos dos livros favorítos).

## Execução

1. Execute `dotnet build` para compilar o projeto (nota: utilize `dotnet build --no-restore` caso haja lentidão devido ao ambiente).
2. Execute `dotnet run` para iniciar o servidor local.
3. Acesse a aplicação em `http://localhost:5239`.
