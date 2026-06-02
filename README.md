# Biblioteca (ASP.NET Core MVC & Vanilla JS)

Este projeto consiste em uma vitrine de biblioteca moderna, utilizando ASP.NET Core MVC para o backend (fornecendo os modelos e controllers) e vanilla JavaScript com `localStorage` no frontend para simular uma experiência de *Single Page Application* (SPA) sem a necessidade de uma base de dados complexa, mantendo a navegação e estados eficientes.

## Arquitetura e Fluxo de Dados (SPA-Like)

O fluxo da aplicação funciona interceptando cliques nos cards dos livros no catálogo principal (`Index.cshtml`). Quando o usuário seleciona um livro, uma função JavaScript (`abrirLivro`) é acionada:
1. Em vez de enviar o ID para o servidor buscar os dados no banco, ela empacota as propriedades visíveis do livro em um objeto JSON.
2. Salva este objeto no `localStorage` do navegador com a chave `livroAtual`.
3. Redireciona para a view genérica do Livro (`Livro.cshtml`).
4. Ao carregar, a página lê o `localStorage` e preenche dinamicamente o título, autor, ano de publicação, etc., no DOM.
Este método minimiza o tráfego no servidor e permite rápida transição.

O mesmo princípio foi utilizado para gerenciar a visão do `Autor.cshtml`, armazenando o nome na chave `autorAtual`.

## Funcionalidades Implementadas

*   **Catálogo Responsivo e Carrossel:** Uma grade horizontal exibe os livros (ou vertical em dispositivos móveis). O botão "Ver todo o catálogo" permite expandir todos os livros em uma visão de grid multi-colunas.
*   **Pesquisa Dinâmica:** Uma barra de busca no `Index.cshtml` filtra instantaneamente a lista visível de livros baseada em correspondências no título e nome do autor usando JavaScript (`oninput`).
*   **Sistema de Favoritos:**
    * Na view detalhada do livro, é possível clicar em "Adicionar aos Favoritos", gravando o título num array JSON persistido no `localStorage` sob a chave `bibliotecaFavoritos`.
    * Na página inicial (`Index.cshtml`), os livros marcados como favoritos recebem destaque visual (uma estrela "⭐") que é injetada na renderização ao inspecionar a chave do localStorage.
*   **Aparência:** Capas de livro baseadas em cores sólidas HEX em vez de imagens pesadas, acompanhadas por design de botões em pílula, transições suaves (CSS transitions/hover) de acordo com padrões visuais relaxantes e modernos.

## Estrutura do Projeto e Execução

O projeto em C# (`.NET 10`) não utiliza bibliotecas pesadas de ORM (como Entity Framework), usando uma abordagem *in-memory* com uma lista estática.

*   `Controllers/BibliotecaController.cs`: Controller primário fornecendo os Models hardcoded e devolvendo views;
*   `Views/Biblioteca/`:
    *   `Index.cshtml`: Catálogo, campo de pesquisa, exibição de estrelas de favoritos.
    *   `Livro.cshtml`: View detalhada populada via LocalStorage; contém botão de Favoritos.
    *   `Autor.cshtml`: View de perfil do autor populada via LocalStorage.
*   `wwwroot/css/biblioteca.css`: Estilização dedicada dos componentes.
*   `WEB3/`: Diretório contendo um espelho das views puramente em HTML, CSS e JS (prototipação).

### Como rodar
`dotnet build`
`dotnet run`

Para testar o layout estático:
Acesse o diretório `WEB3/` e inicie um servidor python com `python3 -m http.server 8000`.
