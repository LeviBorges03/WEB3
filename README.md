# Biblioteca

Este projeto é um sistema de catálogo digital de livros, permitindo aos usuários pesquisar, visualizar detalhes e adicionar livros aos favoritos.

## Funcionalidades

- **Pesquisa em Tempo Real**: Na página inicial, o usuário pode buscar rapidamente livros pelo título ou pelo nome do autor. O filtro ocorre instantaneamente no lado do cliente sem necessidade de recarregar a página.
- **Navegação Estilo SPA (Single Page Application)**: O projeto utiliza `localStorage` para transitar dados de forma fluída entre a listagem e os detalhes do livro, oferecendo transições ágeis entre visualizações sem requerer requisições pesadas ao servidor.
- **Sistema de Favoritos**: Usuários podem salvar e remover seus livros favoritos. Os dados de favoritos são persistidos usando a chave `bibliotecaFavoritos` no `localStorage`.
- **UI/UX Modernos**: A interface de usuário inclui botões em estilo "pill-shape", designs relaxantes, responsividade e transições agradáveis nas interações.

## Tecnologias Utilizadas

- **ASP.NET Core MVC** (.NET 10.0)
- **Pomelo Entity Framework Core MySQL** (versão 9.0.0)
- **HTML5, CSS3, JavaScript** para construção de componentes e gestão de estado do lado cliente
- **Local Storage API** para o trânsito de dados simulando uma SPA e persistência do sistema de favoritos.

## Como Executar
1. Instale o .NET 10.0 SDK.
2. Clone o repositório.
3. Configure sua string de conexão para MySQL na variável de ambiente `ConnectionStrings__DefaultConnection` (Evite salvar credenciais no `appsettings.json`).
4. Navegue para o diretório root do repositório.
5. Execute `dotnet build` e em seguida `dotnet run`.
6. Acesse via `http://localhost:5239`.