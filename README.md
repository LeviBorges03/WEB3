# Biblioteca Web

Sistema de catálogo de livros digital construído usando ASP.NET Core MVC sem a utilização de banco de dados e focado em Client-Side State Management com Javascript nativo.

## Novas Funcionalidades (Atualizações Recentes)

- **Pesquisa em Tempo Real:**
  Foi adicionada uma barra de pesquisa na página inicial que permite filtrar os livros do catálogo instantaneamente (pelo título e pelo nome do autor) utilizando JavaScript e o evento de digitação `oninput`.

- **Sistema de Favoritos com `localStorage`:**
  Agora os usuários podem favoritar as obras que desejam!
  Ao entrar na página de um livro, é possível adicioná-lo ou removê-lo da sua biblioteca de favoritos.
  O sistema salva essas escolhas de forma persistente diretamente no seu navegador, manipulando um JSON Array na chave `bibliotecaFavoritos` do `localStorage`.
  Ao voltar para o catálogo, os livros que você selecionou ganham um belo destaque com uma ⭐ diretamente na capa do livro.

## Arquitetura

O projeto utiliza um paradigma Single Page Application (SPA) Like, com os dados persistindo e trafegando entre as Views do C# através de `localStorage` para economizar requisições do servidor.
