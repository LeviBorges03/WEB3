# Projeto Final Biblioteca - ASP.NET Core MVC

Este é um projeto de uma aplicação web desenvolvida utilizando **ASP.NET Core MVC** em **C#** focada em gerenciar e exibir um catálogo de livros em uma biblioteca virtual.

## Tecnologias e Arquitetura
* **ASP.NET Core MVC (.NET 10)**: Framework principal da aplicação. A lógica de roteamento está configurada no `Program.cs` e `Controllers/BibliotecaController.cs`. As visualizações estão em `Views/Biblioteca`.
* **Entity Framework Core (Pomelo MySQL)**: Mapeamento objeto-relacional para banco de dados MySQL, utilizado para alimentar os dados que trafegam entre os Controllers e as Views.
* **HTML5, CSS3, JavaScript**: A camada de visualização é construída utilizando boas práticas modernas de UI/UX, preferindo designs fluídos e limpos.

## Como rodar o projeto localmente

Para iniciar a aplicação, você precisará do `.NET SDK 10` instalado.

1. Certifique-se de que não haja outros processos travando as portas (ex: `kill $(lsof -t -i :5239)`).
2. Na raiz do projeto, execute o comando:
   ```bash
   dotnet run
   ```
3. A aplicação estará disponível em `http://localhost:5239`.

> **Nota sobre o Banco de Dados:** Configure a variável de ambiente `ConnectionStrings__DefaultConnection` com suas credenciais do MySQL para evitar a necessidade de mantê-las em hardcode no arquivo `appsettings.json`.

## Principais Funcionalidades Frontend

Esta aplicação busca se comportar semelhante a um Single Page Application (SPA) utilizando recursos nativos de navegadores para otimizar o tempo e a experiência:

* **Busca Dinâmica**: Localizada na aba principal (Home - Catálogo), permite buscar em tempo real os títulos, autores e gêneros usando `JavaScript` sem a necessidade de recarregar a página (comunicando com `oninput`).
* **Gerenciamento de Estado do Cliente**: Quando o usuário clica em um Livro ou Autor no catálogo principal, os detalhes e informações são passadas do MVC (Razor) para a visualização final de forma rápida, interceptadas e armazenadas de forma estática no `localStorage`.
* **Sistema de Favoritos**: Implementado exclusivamente no lado do cliente (via `localStorage` usando a chave `bibliotecaFavoritos`), possibilitando a persistência e adição/remoção de livros à lista de favoritos do usuário com um botão elegante nas Views de "Livro Atual".

## Diretório WEB3

Há uma sub-pasta chamada `WEB3/` neste projeto. Esta pasta atua como uma versão estática e de prototipagem para os designs HTML/CSS e JavaScript que eventualmente alimentam e dão as diretrizes para a aplicação principal (em ASP.NET MVC). Quando atualizar lógicas estáticas no repositório principal, certifique-se de atualizar o `WEB3/` também.
