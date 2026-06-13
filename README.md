# Biblioteca - Catálogo Digital

A Biblioteca é uma aplicação web moderna que simula um catálogo digital de obras clássicas da literatura.
Ela permite visualizar livros, filtrar por títulos e acessar detalhes dos livros e dos seus respectivos autores.

## Arquitetura e Tecnologias
- **Backend:** Desenvolvido em **ASP.NET Core MVC** utilizando C# no framework **.NET 10.0**.
- **Frontend:** Views usando **Razor** (`.cshtml`), com layouts modulares, estilização puramente em CSS e comportamento via JavaScript.
- **Armazenamento de Dados:** Todo o catálogo (lista de livros) é inicializado estaticamente no `BibliotecaController`. Não requer banco de dados.
- **Navegação:** A aplicação adota um padrão de navegação SPA-Like. Embora possua múltiplas views (como Index, Livro e Autor), os dados do livro e do autor selecionados são persistidos e trafegados entre as telas utilizando a API nativa de **LocalStorage** (`livroAtual` e `autorAtual`).

## Funcionalidades
1. **Catálogo de Obras:** Lista horizontal com rolagem e opção de expansão em grade (grid) para visualizar a lista completa de clássicos disponíveis.
2. **Sistema de Pesquisa:** Filtragem em tempo real (`oninput`) pelo título da obra diretamente na Home.
3. **Página da Obra:** Apresenta dados específicos como capa, autor, gêneros, ano de publicação e total de páginas.
4. **Perfil do Autor:** Página dedicada ao autor, indicando algumas curiosidades gerais.
5. **Favoritos:** É possível adicionar obras aos favoritos. As obras favoritadas ficam salvas localmente no navegador e recebem um ícone de estrela (⭐) para fácil identificação tanto na lista principal quanto no detalhamento.

## Como rodar o projeto localmente

Pré-requisitos: Ter o .NET SDK 10.0 instalado.

1. Clone o repositório e navegue até a pasta raiz.
2. Restaure as dependências e compile o projeto (o restore pode falhar por timeout em alguns ambientes isolados, nesse caso use as flags offline se possível):
   ```bash
   dotnet build --no-restore
   ```
3. Execute o servidor de desenvolvimento:
   ```bash
   dotnet run
   ```
4. O servidor iniciará. Abra o navegador na url (por padrão: http://localhost:5239).

> **Aviso de Porta em Uso**: Se receber a mensagem "Address already in use", encerre o processo com o comando: `kill $(lsof -t -i :5239)`.
