# Biblioteca App

Uma aplicação web moderna para exploração de catálogo de livros, construída com ASP.NET Core MVC e C#.

## Características (Features)
- **Catálogo de Obras:** Explore os clássicos da literatura com uma interface de carrossel estilizada.
- **Detalhes Dinâmicos:** As páginas de Livro e Autor são populadas dinamicamente sem recarregar a página, proporcionando uma experiência de SPA (Single Page Application) usando `localStorage`.
- **Pesquisa em Tempo Real:** Filtre os livros pelo título ou nome do autor diretamente no catálogo usando a barra de busca (filtragem por `oninput`).
- **Sistema de Favoritos:** Salve os livros que você mais gosta no seu navegador usando `localStorage` e filtre o catálogo para mostrar apenas seus favoritos.

## Tecnologias e Arquitetura
- **Backend:** C#, ASP.NET Core 10.0 MVC
- **Banco de Dados:** MySQL (Pomelo.EntityFrameworkCore.MySql) com injeção de dependências e `BibliotecaContext`.
- **Frontend:** HTML5, CSS3, JavaScript puro. Design responsivo usando CSS Grid e Flexbox.

## Como rodar o projeto localmente

1. Certifique-se de que o .NET 10 SDK e um servidor MySQL estão instalados na sua máquina.
2. Clone o repositório.
3. Defina a string de conexão do seu banco de dados na variável de ambiente `ConnectionStrings__DefaultConnection` (nunca no `appsettings.json`!).
4. Execute os seguintes comandos no terminal, na pasta raiz do projeto:

```bash
dotnet build
dotnet run
```
5. Acesse a aplicação no seu navegador pelo endereço fornecido no terminal (ex: `http://localhost:5239`).
