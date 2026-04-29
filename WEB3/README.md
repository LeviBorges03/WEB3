# Protótipo WEB3 - Biblioteca

Este diretório (`WEB3/`) contém o protótipo estático da interface de usuário da Biblioteca. Ele foi desenvolvido com puramente HTML, CSS e Vanilla JavaScript, sendo totalmente isolado do servidor ASP.NET Core MVC. Seu principal objetivo é facilitar testes de Design, UX e fluxos de interação antes de sua implementação final nas Views (`.cshtml`).

## Estrutura do Protótipo
*   **`Livro/index.html`**: Protótipo da página de detalhes do livro.
*   **`Autor/index.html`**: Protótipo da página de perfil do autor.

## Funcionalidades Simuladas
Para manter a paridade com a aplicação principal, este protótipo simula certas funcionalidades:
*   **Sistema de Favoritos:** O arquivo `WEB3/Livro/index.html` simula o estado de favorito de um livro salvando um título mockado na chave `bibliotecaFavoritos` (array JSON) dentro do `localStorage`. A interface (texto do botão) é alterada interativamente conforme o botão é clicado.

*Para rodar este protótipo, basta abrir os arquivos `.html` no navegador, nenhuma dependência de servidor (como `dotnet run`) é necessária.*