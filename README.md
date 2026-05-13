# Biblioteca Projeto Final

Uma aplicação em ASP.NET Core MVC (e uma versão HTML estática em `WEB3/`) para explorar um catálogo de livros clássicos.

## Funcionalidades
* **Catálogo (Home):** Explore uma lista vasta de livros clássicos, role lateralmente e expanda para ver todos.
* **Barra de Pesquisa:** Na página do catálogo, digite o título de um livro na barra de pesquisa para filtrar os livros mostrados em tempo real usando Javascript e manipulação de DOM (via CSS display).
* **Detalhes da Obra (Livro):** Clique em um livro para ver mais detalhes. A navegação funciona de forma semelhante a uma Single Page Application (SPA), salvando dados em `localStorage` para transitar entre views genéricas sem recarregar dados complexos.
* **Sistema de Favoritos:** Na página de detalhes do livro, há um botão para "Adicionar aos Favoritos" ou "Remover dos Favoritos". Esse sistema salva um array JSON com os títulos dos livros favoritos no navegador do usuário utilizando a chave `bibliotecaFavoritos` no `localStorage`.
* **Perfil do Autor:** Veja detalhes sobre o autor clicando no seu nome no cartão do livro ou na página de detalhes da obra.

## Como Executar
Use o .NET CLI:
```bash
dotnet run
```
O servidor será iniciado na porta 5239 (http://localhost:5239).