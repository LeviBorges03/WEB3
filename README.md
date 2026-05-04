# Biblioteca Virtual

Este projeto é uma aplicação de vitrine digital de livros implementada em **ASP.NET Core MVC** e **C#**. Ele conta com um design moderno, usando HTML, CSS, e JavaScript, e demonstra a capacidade de renderizar componentes baseados em estado de cliente.

## Funcionalidades
*   **Catálogo de Obras**: Vitrine principal onde os usuários podem explorar os clássicos.
*   **Pesquisa**: Pesquisa em tempo real por título e autor através de uma barra de pesquisa.
*   **Sistema de Favoritos**: Funcionalidade baseada no `localStorage` do navegador para os usuários salvarem seus títulos preferidos, podendo filtrar a vitrine principal.
*   **Navegação SPA**: As páginas de Livro e Autor utilizam localStorage para transferir estado, criando uma navegação com menos requests pesados ao servidor, simulando uma Single Page Application.

## Estrutura
*   O back-end é gerido por ASP.NET Core no padrão MVC.
*   Não há conexão a banco de dados nesta versão; o catálogo em `BibliotecaController` é instanciado em memória, permitindo funcionamento isolado.
*   A pasta `/WEB3` contém uma versão estática (HTML/CSS) apenas para fins de prototipagem e design isolado do .NET.

## Como Executar
1. Certifique-se de que possui o .NET SDK 10.0 (ou compatível com a release do repositório) instalado.
2. Navegue até o diretório do projeto e execute:
   ```bash
   dotnet build
   dotnet run
   ```
3. Abra seu navegador em `http://localhost:5239` (ou na porta definida que aparecerá no terminal).
