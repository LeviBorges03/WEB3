# Projeto Biblioteca Clássica 📚

Uma aplicação moderna desenvolvida em **ASP.NET Core MVC** (.NET 10) simulando um catálogo dinâmico de literatura clássica.

## Tecnologias Utilizadas
- C# & ASP.NET Core MVC
- Entity Framework Core (MySQL Pomelo 9.0.0)
- HTML5, CSS3, Vanilla JavaScript
- LocalStorage para gerenciamento de estado client-side

## Funcionalidades
- **Catálogo Principal:** Exibição de um acervo robusto de clássicos com design responsivo, scroll lateral suave e expansão em grid.
- **Busca em Tempo Real:** Campo de pesquisa integrado na Index para filtrar obras por Título ou Autor, de forma rápida sem recarregamento.
- **Navegação SPA-Like:** Utilização de `localStorage` para transferir dados dinâmicos do catálogo para as Views genéricas de "Livro" e "Autor".
- **Sistema de Favoritos:** Persistência no navegador permitindo adicionar e remover títulos dos favoritos.

## Como Executar
1. Certifique-se de ter o .NET 10 SDK e o MySQL configurados.
2. Defina a connection string `ConnectionStrings__DefaultConnection` via variável de ambiente (por segurança, credenciais não estão no appsettings).
3. Execute `dotnet build` e `dotnet run` na raiz do projeto.
4. Acesse via `http://localhost:5239`.

## Estrutura `WEB3/`
Existe uma pasta `WEB3/` na raiz contendo versões estáticas em HTML/CSS/JS puros usadas como protótipo e design guide para a UI do sistema.