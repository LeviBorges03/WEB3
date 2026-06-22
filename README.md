# Projeto Biblioteca Clássica

Este é um projeto de uma aplicação web desenvolvida em **ASP.NET Core MVC** (.NET 10.0), projetado para funcionar como um catálogo visual de obras literárias clássicas.

## Visão Geral

A aplicação funciona com um catálogo hardcoded de livros. Ela evita depender de bancos de dados ou de retornos frequentes ao backend, empregando técnicas de um comportamento SPA (Single Page Application) graças a transferências de dados via `localStorage` e renderização de views genéricas a partir de JavaScript.

### Funcionalidades

1. **Catálogo de Clássicos:** Um slider horizontal contendo as obras disponíveis. É possível expandir o slider em um layout grid clicando no botão "Ver todo o catálogo".
2. **Navegação SPA-Like:** Ao clicar em um livro ou em um autor no catálogo, o sistema salva os dados necessários localmente no navegador (via `localStorage`) e redireciona para as views `Livro.cshtml` ou `Autor.cshtml` genéricas. Essas views leem as informações locais e as apresentam dinamicamente, sem necessidade de consultas a IDs de banco de dados.
3. **Barra de Pesquisa de Autores e Livros:** Possui busca integrada no lado do cliente que filtra por Título, Autor e Gênero dinamicamente durante a digitação.
4. **Sistema de Favoritos:** Os usuários podem adicionar ou remover livros aos favoritos clicando na estrela (⭐) em cada card no catálogo, ou utilizando o botão de favoritos presente na página de detalhes do livro. Este dado é salvo como um array JSON (`bibliotecaFavoritos`) no `localStorage`, persistindo no lado do cliente.

## Estrutura

* **Raiz do Repositório**: Contém a aplicação .NET, os controladores (com o modelo em memória no `BibliotecaController`), Views Razor, e assets estáticos (`wwwroot/`).
* **Diretório `WEB3/`**: Contém versões inteiramente estáticas e isoladas da interface para a prototipação rápida. É possível visualizar os protótipos em HTML, JS e CSS independentemente do servidor C#.

## Instruções de Execução

### Para rodar a Aplicação MVC (.NET Core)
1. Abra um terminal na raiz do projeto.
2. Certifique-se de ter o .NET 10.0 SDK instalado.
3. Execute `dotnet build` para compilar.
4. Execute `dotnet run` para rodar a aplicação localmente.
5. O servidor web local será iniciado na porta informada (ex: `http://localhost:5239`).

### Para rodar e visualizar o Protótipo `WEB3/`
Se precisar testar apenas as versões isoladas sem backend:
1. Abra um terminal apontando para a pasta `WEB3/` no projeto (`cd WEB3`).
2. Utilize um servidor estático local. Por exemplo, no Python:
   `python3 -m http.server 8000`
3. Acesse em seu navegador via `http://localhost:8000`.

## Boas Práticas (Guia)
* Se houver necessidade de interagir com o DOM por scripts, usar atributos HTML (`data-titulo`, `data-autor`) garante melhor isolamento contra quebras caso o texto base visual mude.
* Ao construir listas em C#, é sugerido ordenação no nível do `Controller` antes de passar a model para a View, e usar campos `.ReadOnly` se estáticos.
* Ao atualizar as Views do ASP.NET Core MVC, garanta que suas contrapartes e lógica em `WEB3/` (protótipo) também sejam espelhadas (e vice-versa).