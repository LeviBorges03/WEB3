# Biblioteca App (ASP.NET Core)

Bem-vindo ao projeto **Biblioteca App**. Trata-se de uma aplicação ASP.NET Core que implementa um catálogo digital de livros com uma interface responsiva, animada e fluida. O projeto adota algumas estratégias modernas, como o conceito de SPA (Single Page Application) sem usar frameworks JS complexos, baseando-se apenas em Vanilla JS e o cache no `localStorage`.

## Estrutura do Projeto

O projeto é dividido em duas grandes áreas:
- **Projeto Principal (.NET Core MVC):** Controladores (como o `BibliotecaController.cs`) e as páginas Razor (`Views/Biblioteca/`) formam o escopo da aplicação. Os modelos da base de dados são injetados sob demanda.
- **Protótipos de Design (`WEB3/`):** Diretório que mantém as páginas HTML/CSS estáticas com dados mocados que servem como guia para implementar features da interface do usuário antes da integração com o backend C#.

## Funcionalidades Principais

- **Catálogo de Livros e Navegação Lateral (Carrossel):** Todos os livros são mostrados usando CSS grid e flexbox com o suporte de setas que permitem rolar lateralmente. Se o usuário quiser, um botão permite "Expandir o Catálogo" para visualização em grid inteiro.
- **Navegação SPA (SPA-like):** Em vez de enviar id's para o backend por meio da URL a cada clique, a aplicação serializa o livro clicado no `localStorage` usando as chaves `livroAtual` e `autorAtual`. A view genérica do `Livro.cshtml` apenas renderiza esses dados via JS, o que traz uma performance instantânea na visualização de conteúdo.
- **Pesquisa em Tempo Real:** Uma elegante barra de pesquisa na página inicial permite filtrar livros por Autor, Gênero ou Título sem recarregar a página, expandindo os resultados automaticamente.
- **Sistema de Favoritos:** A aplicação permite aos usuários adicionarem seus títulos preferidos na sua lista de leitura. Os dados são salvos persistemente no browser via `localStorage` (Chave `bibliotecaFavoritos`) e um indicativo visual de estrela (⭐) aparece nos itens selecionados no catálogo e nas descrições da obra.

## Como Executar Localmente

### Pré-requisitos
- .NET SDK (10.0 recomendado)

### Passos
1. Faça o clone do repositório.
2. Certifique-se de que os pacotes essenciais estejam instalados executando `dotnet build`. Para desenvolvimento local onde a restauração timeout, pode usar `dotnet build --no-restore`.
3. Caso você receba um erro de que a porta `5239` já está em uso, mate o processo em background usando:
   ```bash
   kill $(lsof -t -i :5239)
   ```
4. Suba o servidor com:
   ```bash
   dotnet run
   ```
5. Acesse http://localhost:5239 no navegador para ver o sistema.
