# Biblioteca

Este projeto é uma aplicação de vitrine de livros clássicos em ASP.NET Core MVC (C#).
A principal funcionalidade é gerenciar informações de obras e autores localmente de forma semelhante a uma Single Page Application (SPA), usando cache e armazenamento local em vez de backend redondo em todas as requisições.

## Principais Funcionalidades

- **Catálogo Principal (Home):** Onde são mostrados todos os livros.
- **Barra de Pesquisa:** Permite filtrar instantaneamente os livros exibidos por título, autor ou gênero. O script utiliza `innerText` na busca e o evento `oninput` para maior reatividade.
- **Sistema de Favoritos (`localStorage`):** Os usuários podem marcar livros como favoritos (⭐). Os títulos favoritos são salvos em formato JSON (`bibliotecaFavoritos`) no `localStorage` do navegador para manter persistência no front-end.
- **Transição de Dados SPA-Like:** A aplicação guarda dados transientes no `localStorage` sob chaves como `livroAtual` e `autorAtual` para navegar entre a visualização de detalhes do Livro ou do Autor sem recarregar esses dados do banco de dados/backend.

## Como Executar (Ambiente Local)

1. Certifique-se de ter o .NET 10.0 (ou versão correspondente descrita nos projetos/memórias) instalado.
2. Navegue para o diretório raiz do repositório onde encontra-se o arquivo `.csproj`.
3. Se estiver em um ambiente local normal, você pode rodar o comando abaixo para compilar e iniciar a aplicação localmente:
   ```bash
   dotnet run
   ```
4. Em caso de bloqueio da porta padrão de execução (ex: 5239), verifique o PID no seu log ou utilize o comando `kill $(lsof -t -i :5239)` e rode novamente.

## Estrutura Extra (`WEB3`)
Existe no diretório `WEB3` uma representação de protótipo estático de algumas destas páginas (HTML/CSS/JS isolado). Ele é usado para referenciar o layout visual fora do ASP.NET. Veja o `WEB3/README.md` para mais informações.
