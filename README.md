# Projeto Biblioteca (ASP.NET Core MVC)

Este projeto é uma aplicação web construída com **ASP.NET Core MVC** e **C#**, que funciona como um catálogo digital de uma biblioteca. Ele utiliza **Entity Framework Core** com MySQL para gerenciamento de banco de dados e foca em uma interface de usuário rica e interativa usando tecnologias web modernas.

## Recursos e Funcionalidades
- **Navegação Estilo SPA (SPA-Like):** A aplicação usa intensamente o `localStorage` do navegador e JavaScript para passar dados entre as views (ex: de Catálogo para Detalhes do Livro ou Perfil do Autor) simulando a experiência de uma Single Page Application sem recarregar a página completamente.
- **Sistema de Busca em Tempo Real:** A página inicial possui uma barra de pesquisa ("pill-shaped") que filtra os livros exibidos instantaneamente conforme o usuário digita (vinculada ao evento `oninput`), filtrando por título ou autor.
- **Sistema de Favoritos:** Os usuários podem favoritar obras na página de Detalhes do Livro. Esse sistema salva um array JSON de títulos favoritos no `localStorage` usando a chave `bibliotecaFavoritos`, alternando a aparência e o texto do botão.
- **Layout Responsivo e Design Moderno:** Utiliza flexbox, animações CSS e um design voltado para o relaxamento, com elementos elegantes como botões arredondados e capas dinâmicas geradas por cores hexadecimais no banco de dados.

## Instruções de Execução Local

1. **Pré-requisitos:** Certifique-se de ter o SDK do .NET 10.0 instalado.
2. **Construção e Execução:**
   - Para compilar o projeto:
     ```bash
     dotnet build
     ```
   - Para iniciar o servidor de desenvolvimento:
     ```bash
     dotnet run
     ```
   O servidor geralmente escutará na porta local `5239` (ex: `http://localhost:5239`).
3. **Resolução de Conflitos de Porta:**
   Se você encontrar um erro indicando que a porta 5239 já está em uso ("Address already in use"), execute o seguinte comando no terminal bash para liberar a porta antes de iniciar novamente:
   ```bash
   kill $(lsof -t -i :5239)
   ```

## Sobre o Diretório WEB3/
O repositório inclui uma pasta `WEB3/` que contém uma representação isolada em HTML, CSS e JavaScript puros da interface do usuário. Essa pasta é estritamente utilizada para **prototipação de UI** e validação visual de estilos antes de serem integrados ao projeto ASP.NET Core MVC principal. Mantenha os recursos lá sincronizados com os arquivos `.cshtml` se fizer grandes alterações de design.