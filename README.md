# Projeto Biblioteca

O Projeto Biblioteca é uma aplicação web desenvolvida em C# utilizando o framework **ASP.NET Core MVC**. Este projeto não utiliza o Entity Framework nem possui dependências diretas de banco de dados, sendo todas as informações (como o catálogo de livros) instanciadas em memória nos controllers ou gerenciadas no lado do cliente.

## Funcionalidades Principais

- **Catálogo Principal (SPA-like):** O carregamento de diferentes livros ocorre de forma muito dinâmica, assemelhando-se a uma *Single Page Application* (SPA). Quando você clica em um livro na Home, os dados do livro são codificados e transferidos usando o `localStorage` do navegador para serem exibidos na página de Detalhes.
- **Barra de Pesquisa Instantânea:** No catálogo de clássicos, você pode usar a nova barra de pesquisa para filtrar em tempo real os títulos ou os autores da biblioteca usando JavaScript (`oninput`).
- **Sistema de Favoritos:** Ao abrir um livro, você pode marcá-lo como favorito. A persistência é realizada exclusivamente pelo lado do cliente usando o `localStorage` (na chave `bibliotecaFavoritos`), possibilitando salvar essas preferências sem a necessidade de contas de usuário ou de um banco de dados relacional.
- **Visualização de Perfil do Autor:** Cada autor tem um perfil que lista informações dinâmicas relacionadas ao seu nome, com navegação contextual semelhante.

## Executando o Projeto Localmente

1. Tenha o [.NET SDK 10.0](https://dotnet.microsoft.com/download) (ou compatível) instalado na sua máquina.
2. Navegue até a raiz do projeto (onde está localizado este `README.md` e o `Biblioteca.csproj`).
3. Compile o projeto rodando o comando:
   ```bash
   dotnet build
   ```
4. Em seguida, inicie o servidor:
   ```bash
   dotnet run
   ```
5. Acesse `http://localhost:5239` no seu navegador (a porta exata será impressa no terminal).

## Sobre a Pasta WEB3

Dentro da raiz do repositório, existe um diretório isolado chamado `WEB3/`. Esta pasta contém uma representação puramente estática (HTML, CSS, JS puros, sem C#) dos componentes visuais do projeto. Ela é utilizada para **prototipação de UI** e design, possibilitando que a equipe de front-end desenvolva e valide os componentes isoladamente antes de serem integrados ao ASP.NET Core MVC.
