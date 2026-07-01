# Protótipos Estáticos da Biblioteca (WEB3)

Esta pasta contém o protótipo puro em HTML, CSS e JS (sem depender do framework ASP.NET MVC).

Ele serve como o ponto de partida do design da nossa biblioteca.
Para executar, use um servidor HTTP simples na raiz deste diretório (ex: `python3 -m http.server 8000`).

## Sobre o Sistema SPA e Favoritos
- Nossos protótipos tentam emular o comportamento final da aplicação (encontrada na pasta raiz).
- Para persistir qual livro deve aparecer na tela, usamos a chave `livroAtual` e `autorAtual` no `localStorage`.
- Foi adicionada lógica para gerenciar favoritos (`bibliotecaFavoritos`), integrando o botão "Adicionar aos Favoritos" com o storage local.
