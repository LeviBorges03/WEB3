# Biblioteca

Um projeto de vitrine de livros clássicos desenvolvido em ASP.NET Core MVC.

## Funcionalidades

*   **Catálogo de Clássicos:** Uma vitrine exibindo uma seleção de livros com rolagem horizontal e opção de expandir a visualização.
*   **Detalhes Dinâmicos (SPA-Like):** Ao clicar em um livro ou autor, a aplicação redireciona para as views `Livro.cshtml` ou `Autor.cshtml`, carregando os dados dinamicamente via `localStorage`, sem necessidade de acesso a banco de dados.
*   **Pesquisa Real-time:** Uma barra de pesquisa na tela inicial permite filtrar livros por título ou autor de forma rápida e insensível a acentos e letras maiúsculas/minúsculas.
*   **Sistema de Favoritos:** Os usuários podem marcar livros como favoritos clicando na estrela nos cards de livros ou no botão na página de detalhes. Os favoritos são salvos localmente (`localStorage`).
*   **Prototipagem WEB3:** Inclui uma pasta `WEB3/` contendo mockups HTML/CSS/JS estáticos das páginas de Detalhes do Livro e Autor, permitindo fácil prototipagem.

## Como Executar

### Ambiente ASP.NET Core
1.  Certifique-se de ter o .NET SDK 10.0 instalado.
2.  No diretório raiz do projeto, execute o comando:
    ```bash
    dotnet build
    dotnet run
    ```
3.  Acesse a aplicação no navegador (geralmente `http://localhost:5239`).

### Prototipagem WEB3 (Estático)
Para visualizar os protótipos puramente estáticos na pasta `WEB3`:
1.  Navegue até o diretório `WEB3/`:
    ```bash
    cd WEB3
    ```
2.  Inicie um servidor HTTP simples (ex: usando Python):
    ```bash
    python3 -m http.server 8000
    ```
3.  Acesse `http://localhost:8000/Livro/` ou `http://localhost:8000/Autor/` no navegador.
