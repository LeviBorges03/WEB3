# Protótipos Estáticos - WEB3

Este diretório contém as páginas cruas (HTML + CSS Vanilla + JavaScript) que servem de prototipagem para a aplicação final em ASP.NET Core Razor Pages do diretório raiz.

## Estrutura
- `/Autor`: Protótipo da view que contém a foto e resumo das obras de um determinado autor.
- `/Livro`: Protótipo que exibe a renderização de uma página de detalhes do livro contendo: título, publicações, tags de gênero, informações do autor e um botão funcional de Favoritos.

## Como as Telas Funcionam
As funcionalidades dessas páginas foram criadas visando uma integração fluida e SPA-like.
Por meio de propriedades injetadas pelo **`localStorage`**, como `livroAtual` e a array `bibliotecaFavoritos`, é possível manipular a visibilidade da estrela de favoritismo dinamicamente em interfaces HTML puras, sem a necessidade de um backend ou compilador complexo na hora de designar ou testar componentes UI.

## Como Executar e Testar Localmente
Basta abrir o `index.html` dos respectivos subdiretórios em seu navegador ou utilizar um servidor HTTP em python para que eventuais conflitos do CORS ou protocolos em arquivos do navegador (`file://`) não ocorram:
```bash
python3 -m http.server 8000
```
Isso disponibilizará os protótipos em `http://localhost:8000/`.