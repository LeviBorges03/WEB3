# Projeto Biblioteca - Catálogo de Clássicos

Este projeto é uma aplicação web de biblioteca focada em apresentar um catálogo de clássicos da literatura. Foi desenvolvida utilizando ASP.NET Core MVC (C#) no backend e HTML/CSS/JavaScript no frontend, focando numa experiência rica, rápida e fluida, semelhante a uma Single Page Application (SPA).

## Funcionalidades

- **Catálogo de Clássicos:** Uma lista extensa de livros clássicos disponíveis.
- **Navegação SPA-Like:** Utilização de `localStorage` para transferir dados entre as páginas sem a necessidade de recarregar informações complexas ou realizar múltiplas requisições ao servidor.
- **Busca Rápida (Em Tempo Real):** Pesquise livros instantaneamente por título, autor ou gênero, filtrando o catálogo na tela principal.
- **Sistema de Favoritos:** Adicione seus livros preferidos à lista de favoritos, armazenada localmente no navegador (`localStorage`), e filtre os favoritos diretamente na tela inicial.
- **Páginas de Detalhes:**
  - **Página do Livro:** Mostra detalhes completos da obra, sinopse, capa gerada com cor dinâmica, etc.
  - **Página do Autor:** Apresenta informações detalhadas do autor, junto com uma lista (mockada) de outras obras.

## Tecnologias

- **Backend:** C#, .NET 10.0, ASP.NET Core MVC
- **Frontend:** HTML5, CSS3, JavaScript puro
- **Design:** Responsivo, "Clean & Professional", com animações suaves e layouts em grid/flexbox.

## Como executar o projeto

Certifique-se de ter o [.NET SDK 10.0](https://dotnet.microsoft.com/download) instalado.

1. **Clone ou baixe** este repositório.
2. Abra o terminal na raiz do projeto.
3. Restaure as dependências e compile o projeto:
   ```bash
   dotnet build
   ```
4. Execute a aplicação:
   ```bash
   dotnet run
   ```
5. Abra o navegador e acesse a URL indicada (normalmente `http://localhost:5000` ou `https://localhost:5001`).

## Dicas para o Desenvolvimento

- O projeto não utiliza banco de dados para a listagem inicial e favoritos, em vez disso, as informações dos livros estão definidas no `BibliotecaController.cs` e a transferência de estado do frontend (livro atual, autor atual, livros favoritos) ocorre inteiramente pelo `localStorage` do navegador.
- Ao adicionar CSS, mantenha o padrão "Clean & Professional" detalhado no `wwwroot/css/DescricaoEstilo.txt`.
