# WEB3 - Biblioteca Digital

Bem-vindo ao projeto **Biblioteca Digital**, uma aplicação web desenvolvida em C# utilizando o ASP.NET Core MVC (Target Framework .NET 10.0).

Este projeto tem como objetivo principal oferecer um catálogo interativo de obras clássicas, permitindo aos usuários explorar os livros e autores disponíveis de maneira intuitiva e moderna.

## Funcionalidades Principais

*   **Catálogo Interativo:** Uma vitrine de livros com rolagem horizontal e opção de expansão em grade, tudo desenvolvido com CSS fluido e moderno.
*   **Arquitetura SPA-Like:** A aplicação utiliza `localStorage` para transitar dados de forma otimizada entre o catálogo principal (Home), a página de detalhes da obra (Livro) e a página de perfil (Autor) sem necessitar de requisições pesadas ao servidor para exibição de detalhes, proporcionando uma navegação extremamente rápida.
*   **Busca em Tempo Real:** Uma barra de pesquisa na página inicial que filtra os livros pelo título, autor ou gênero instantaneamente, usando JavaScript (`oninput`).
*   **Sistema de Favoritos:** Os usuários podem marcar livros como favoritos na página de detalhes da obra. Esses dados são salvos no navegador (`localStorage`). O catálogo principal permite alternar a visualização para mostrar apenas as obras favoritadas, perfeitamente integrado com a busca.
*   **Design Responsivo:** A interface se adapta para oferecer uma boa experiência em desktops, tablets e smartphones.

## Tecnologias Utilizadas

*   **Backend:** ASP.NET Core MVC (C#)
*   **Frontend:** HTML5, CSS3, JavaScript puro (Vanilla JS), Razor Pages.
*   **Banco de Dados:** Entity Framework Core integrado com MySQL (`Pomelo.EntityFrameworkCore.MySql` versão 9.0.0).

## Como Executar o Projeto

1.  **Pré-requisitos:** Certifique-se de ter o .NET SDK 10 instalado na sua máquina.
2.  **Configuração do Banco de Dados:**
    *   Este projeto espera uma string de conexão ao banco de dados injetada via variáveis de ambiente para fins de segurança (não guarde credenciais sensíveis no `appsettings.json`).
    *   Defina a variável `ConnectionStrings__DefaultConnection` no seu ambiente antes de rodar o projeto. Exemplo no terminal (Linux/macOS):
        `export ConnectionStrings__DefaultConnection="Server=localhost;Port=3306;Database=Biblioteca;User=root;Password=sua_senha;"`
3.  **Restaurar e Compilar:**
    Abra um terminal na raiz do projeto e execute:
    ```bash
    dotnet build
    ```
4.  **Executar:**
    Inicie a aplicação utilizando o comando:
    ```bash
    dotnet run
    ```
    O terminal informará a URL local onde o servidor está rodando (geralmente `http://localhost:5000` ou similar).

## Documentação Técnica Adicional

Para mais detalhes sobre as Views de Livro e Autor, ou sobre a estrutura de pastas do frontend, consulte os arquivos `README.md` específicos presentes dentro da pasta `WEB3/`.