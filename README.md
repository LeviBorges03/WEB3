# Biblioteca de Clássicos (WEB3 Project)

Bem-vindo ao projeto **Biblioteca de Clássicos**! Este projeto é uma aplicação ASP.NET Core MVC (C#) moderna, focada em fornecer uma interface de usuário fluida que funciona de maneira semelhante a uma Single Page Application (SPA), garantindo alto desempenho sem recarregamentos completos de página a cada navegação.

## Funcionalidades Principais

*   **Catálogo Dinâmico:** Um carrossel interativo e elegante para exibir clássicos da literatura.
*   **Barra de Pesquisa em Tempo Real:** Uma barra de pesquisa moderna com formato de pílula (pill-shaped) foi implementada. Ela funciona em tempo real (utilizando o evento `oninput`) para buscar obras pelo **título** ou **autor**, filtrando imediatamente o conteúdo visível sem recarregar a página.
*   **Sistema de Favoritos:** Os usuários podem favoritar as suas obras preferidas! Na página de cada Livro, o botão de "Adicionar aos Favoritos" gerencia a sua seleção via `localStorage`. A barra de pesquisa inicial conta também com um botão dedicado (pill-shaped) para filtrar a lista e mostrar apenas os seus favoritos.
*   **Navegação SPA-Like:** A aplicação utiliza massivamente o `localStorage` do navegador para transferir estados entre páginas (como o "Livro Atual" ou "Autor Atual") e manipular o DOM. Isso simula o comportamento de uma SPA de alta eficiência.
*   **Design Fluido:** Animações e transições focadas em UX relaxante.

## Como Executar o Projeto

1.  Certifique-se de que o **.NET SDK 10.0** ou superior está instalado.
2.  Navegue até a raiz do projeto (onde está o arquivo `Biblioteca.csproj`).
3.  Utilize o seguinte comando para construir o projeto:
    ```bash
    dotnet build
    ```
4.  Para executar o projeto, utilize:
    ```bash
    dotnet run
    ```
5.  Acesse o servidor local (geralmente em `http://localhost:5239`) via seu navegador web e desfrute da aplicação.
