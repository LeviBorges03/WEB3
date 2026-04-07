# Biblioteca Clássicos 📚

Uma aplicação Web de catálogo de livros construída com **ASP.NET Core MVC**. A Biblioteca apresenta um design moderno, fluido e relaxante, focado em uma excelente experiência de usuário e carregamento rápido de conteúdos usando princípios *SPA-like*.

## Funcionalidades Principais 🌟

- **Catálogo de Clássicos**: Navegação em carrossel horizontal por diversas obras clássicas da literatura.
- **Navegação SPA-Like**: Detalhes dos livros e dos autores são abertos quase instantaneamente graças ao uso avançado de transferência de dados *client-side* via `localStorage`, sem recarregamentos completos entre as páginas do catálogo.
- **Pesquisa Avançada**: Filtre os livros no catálogo instantaneamente por título, autor ou gênero usando a barra de busca dinâmica.
- **Sistema de Favoritos**: Salve suas obras favoritas no navegador (através de `localStorage`). Você pode adicionar/remover favoritos na página do livro e filtrar o catálogo para exibir apenas seus itens preferidos.

## Tecnologias e Arquitetura 🛠️

- **Backend**: C# 10 / ASP.NET Core MVC (.NET 10.0)
- **Banco de Dados**: Configurado para Entity Framework Core com MySQL (Pomelo 9.0.0). *A vitrine usa atualmente dados mockados persistentes enquanto a integração completa do BD é concluída.*
- **Frontend**: HTML5, CSS3 Customizado (Variáveis CSS, CSS Grid, Flexbox), Vanilla JavaScript.
- **Estilo**: As capas dos livros não dependem de arquivos estáticos pesados; elas são desenhadas via `background-color` dinâmicos a partir de propriedades HEX armazenadas no banco/código para performance máxima.

## Como Executar o Projeto 🚀

### Pré-requisitos
- .NET 10 SDK
- Servidor MySQL (opcional para a vitrine mockada, mas necessário para fluxos EF Core)

### Passos

1. No terminal, navegue até o diretório raiz do projeto.
2. Restaure as dependências e faça o build do projeto:
   ```bash
   dotnet build
   ```
3. Execute o servidor de desenvolvimento:
   ```bash
   dotnet run
   ```
4. O terminal exibirá as URLs (ex: `http://localhost:5xxx`). Abra o navegador e acesse para começar a navegar no catálogo.

## Organização do Código 📁

- `Controllers/BibliotecaController.cs`: Controla o fluxo de telas (`Index`, `Livro`, `Autor`) e entrega o mock de dados iniciais.
- `Models/`: Contém o contexto do banco de dados e as classes (ex: `Livro.cs`).
- `Views/Biblioteca/`:
  - `Index.cshtml`: Catálogo principal, carrossel, pesquisa e filtro de favoritos.
  - `Livro.cshtml`: View genérica para exibir detalhes de um livro selecionado.
  - `Autor.cshtml`: View genérica para exibir o perfil de um autor selecionado.
- `wwwroot/css/biblioteca.css`: Estilização dedicada à experiência moderna da biblioteca.