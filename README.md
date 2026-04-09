# Biblioteca WEB3

Este é um projeto de estudo em ASP.NET Core MVC (C#) voltado para o desenvolvimento web moderno. O objetivo principal do projeto é a implementação de um catálogo interativo de livros clássicos, utilizando tecnologias frontend como `localStorage` do HTML5 para proporcionar uma experiência de "Single Page Application" (SPA) sem a necessidade de frameworks pesados no lado cliente.

## Funcionalidades Implementadas

*   **Catálogo Dinâmico:** Visualização de obras literárias a partir de dados em memória.
*   **Barra de Pesquisa:** Filtragem instantânea e dinâmica do catálogo usando JavaScript puro.
*   **Sistema de Favoritos:** Persistência de obras favoritas do usuário através de `localStorage`, mantendo estado entre abas e recarregamentos sem bater no servidor.
*   **Transferência de Dados via JS:** Navegação entre as visualizações ("Detalhes do Livro" e "Perfil do Autor") usando dados locais, reduzindo requisições ao servidor para obter dados puramente de interface.
*   **Interface Fluida e Moderna:** CSS responsivo com navegações e expansões de catálogo suaves.

## Tecnologias

*   C# e ASP.NET Core 10.0 MVC
*   Entity Framework Core e MySQL (via Pomelo) - Preparado para uso, mas atualmente usando dados estáticos (em memória).
*   HTML5, CSS3 Custom Properties (Variáveis) e Flexbox/Grid
*   Vanilla JavaScript (ES6+)
*   API `localStorage` para persistência no navegador

## Como Rodar o Projeto

1.  Certifique-se de ter o [.NET SDK 10.0](https://dotnet.microsoft.com/download) instalado.
2.  Abra um terminal na raiz do projeto (onde está o arquivo `Biblioteca.csproj`).
3.  (Opcional) Restaure as dependências com o comando `dotnet restore`.
4.  Execute o projeto com o comando `dotnet run`.
5.  O console indicará a URL onde o servidor local estará rodando (geralmente `http://localhost:5000` ou `https://localhost:5001`). Acesse essa URL pelo seu navegador para usar a aplicação.
6.  *Aviso de Conexão com o Banco de Dados*: No momento, as listagens não dependem diretamente de uma conexão de banco de dados ativa, a não ser que uma migração e persistência explícita via Model seja implementada. No entanto, para configurar o ambiente do Entity Framework (caso deseje utilizá-lo), defina a variável de ambiente `ConnectionStrings__DefaultConnection` e evite preenchê-la diretamente no `appsettings.json`.
