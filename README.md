# Biblioteca

Um projeto de catálogo de biblioteca desenvolvido em ASP.NET Core MVC (C#). Este projeto foca em demonstrar uma interface de usuário moderna, rápida e responsiva usando princípios de Single Page Application (SPA) integrados diretamente nas Views do Razor, aproveitando o poder do JavaScript e LocalStorage.

## Funcionalidades

*   **Catálogo de Clássicos:** Uma vitrine exibindo diversas obras clássicas ordenadas por data de publicação.
*   **Detalhes do Livro e Autor:** Páginas dinâmicas que renderizam os detalhes com base nas seleções do usuário, simulando navegação SPA sem recarregamentos pesados de backend.
*   **Pesquisa em Tempo Real:** Barra de pesquisa elegante na página inicial para filtrar livros instantaneamente por título, autor ou gênero.
*   **Sistema de Favoritos:** Os usuários podem adicionar ou remover livros de sua lista de favoritos diretamente na página de detalhes, sendo as preferências armazenadas localmente no navegador via `localStorage`.

## Tecnologias e Arquitetura

*   **Backend:** ASP.NET Core MVC, C# (.NET 10.0). Os dados são manipulados na memória dentro dos controladores para fins de desempenho (sem banco de dados).
*   **Frontend:** HTML5, CSS3, JavaScript. A aplicação gerencia transições de estado passando dados no `localStorage` entre o catálogo e as páginas de detalhes.
*   **Estilos:** Design system limpo com bordas arredondadas e cores fluidas baseadas em variáveis CSS. Elementos de transição suaves.

## Protótipos (Diretório WEB3)

A pasta `WEB3/` contém representações puramente estáticas do frontend (apenas HTML/CSS/JS isolado do backend). Servem para design rápido e experimentação visual. Para garantir a coerência, quaisquer atualizações no código principal da Web também se aplicam aos arquivos do protótipo no `WEB3/`.

## Executando o Projeto Localmente

1.  Restaure os pacotes e compile o projeto (recomendado o uso da flag `--no-restore` caso os pacotes já estejam em cache local para evitar timeouts):
    ```bash
    dotnet build --no-restore
    ```
2.  Execute o servidor:
    ```bash
    dotnet run
    ```
3.  Acesse `http://localhost:5239` no seu navegador.
