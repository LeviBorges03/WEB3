# Projeto Biblioteca (ASP.NET Core MVC)

Este projeto é uma aplicação de catálogo de livros, construída utilizando ASP.NET Core MVC. Ele simula uma biblioteca virtual, permitíndo aos usuários visualizarem um catálogo de obras clássicas.

## Arquitetura
O sistema segue o padrão MVC (Model-View-Controller) suportado pelo ASP.NET Core.
Os dados dos livros são gerenciados de forma *in-memory* na camada Controller (`BibliotecaController`).
As Views (`Index`, `Livro`, e `Autor`) utilizam uma abordagem SPA-like usando `localStorage` para a passagem de dados sem a necessidade de banco de dados ou sessões complexas.

### WEB3
O diretório `WEB3/` na raiz do repositório contém uma cópia puramente estática das páginas, útil para prototipação e validações de design sem a necessidade de inicializar o servidor ASP.NET Core.

## Funcionalidades
- **Navegação de Catálogo:** Lista todos os livros disponíveis com seus respectivos detalhes.
- **Barra de Pesquisa:** Localizada no catálogo principal (Index), permite filtrar livros dinamicamente por título, autor ou gênero literário em tempo real utilizando JavaScript.
- **Sistema de Favoritos:** Integrado diretamente no armazenamento do navegador (`localStorage`) através da chave `bibliotecaFavoritos`. O sistema permite que o usuário favorite e desfavorite obras na página do Livro (`Livro.cshtml` e `WEB3/Livro/index.html`). O botão se altera dinamicamente com o estado.

## Como Executar
1. Instale o [.NET 10.0 SDK](https://dotnet.microsoft.com/).
2. Abra o terminal na raiz do projeto.
3. Para compilar, utilize:
   `dotnet build`
4. Para executar o servidor de desenvolvimento, utilize:
   `dotnet run`
5. Acesse no navegador o link fornecido pelo console (tipicamente `http://localhost:5239`).

> *Nota de Segurança*: A propriedade `AllowedHosts` no `appsettings.json` está configurada como `localhost` para evitar problemas com ataques via cabeçalho de host.