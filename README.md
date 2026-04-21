# Sistema de Biblioteca

Este é um projeto web desenvolvido em C# com ASP.NET Core MVC focado em criar um catálogo de livros clássicos moderno e dinâmico, utilizando técnicas "SPA-like" via manipulação do `localStorage` no JavaScript.

## Funcionalidades Principais
- **Catálogo Interativo:** Exibe livros em uma grade com rolagem horizontal que pode ser expandida.
- **Barra de Pesquisa:** Localizada no topo do catálogo, permite filtrar os livros visíveis em tempo real por título ou autor usando o evento `oninput`.
- **Sistema de Favoritos:** A página de detalhes do livro possui um botão para favoritar/desfavoritar a obra. O estado é salvo persistentemente no navegador usando o `localStorage` na chave `bibliotecaFavoritos`.
- **Navegação SPA-like:** Ao invés de trafegar IDs ou dados extensos via query string do servidor, o frontend salva os dados do livro/autor selecionado no `localStorage` antes de redirecionar para views genéricas, gerando as páginas dinamicamente no cliente.

## Estrutura do Projeto
- `Controllers/BibliotecaController.cs`: Controller principal onde os dados do catálogo (mock) são injetados.
- `Views/Biblioteca/`: Views MVC (Index, Livro, Autor) que montam a interface.
- `wwwroot/css/biblioteca.css`: Estilo base fluido e relaxante de todo o projeto.
- `WEB3/`: Diretório contendo protótipos estáticos (HTML/CSS puros) do layout, sem a necessidade de rodar o servidor .NET, ótimo para designers.

## Como Executar
1. Certifique-se de ter o .NET SDK 10 instalado.
2. Navegue até a raiz do projeto (onde está o `.csproj`).
3. Execute o comando `dotnet build` para compilar.
4. Execute `dotnet run` para iniciar o servidor de desenvolvimento local.
5. Acesse a URL fornecida pelo console (geralmente `http://localhost:5239`).
