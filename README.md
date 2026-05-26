# Catálogo Digital de Clássicos da Biblioteca

## Visão Geral

Este projeto é uma aplicação web desenvolvida em **ASP.NET Core MVC (C#)** que serve como um catálogo digital interativo para uma biblioteca. O sistema foca em exibir uma ampla seleção de obras literárias clássicas de forma organizada, proporcionando uma experiência de usuário rica com navegação fluida similar a uma Single Page Application (SPA), através do uso eficiente do LocalStorage e de Javascript do lado do cliente.

## Funcionalidades

*   **Vitrine de Livros:** Exibição elegante das obras em um carrossel horizontal ou grade expandida, com capas geradas via código de cores HEX associadas aos gêneros.
*   **Barra de Pesquisa em Tempo Real:** Permite aos usuários filtrar o catálogo rapidamente digitando o título, autor ou gênero literário da obra desejada.
*   **Sistema de Favoritos:** Os usuários podem favoritar livros na página de detalhes da obra. As seleções persistem localmente (`localStorage`), e é possível aplicar um filtro no catálogo principal para exibir apenas os favoritos do usuário.
*   **Navegação SPA-Like:** A transição entre o catálogo principal, detalhes da obra e o perfil do autor é gerenciada repassando o estado via `localStorage` e renderizando uma view genérica por trás, reduzindo consideravelmente requisições pesadas no backend e idas/vindas de banco de dados.

## Como Rodar a Aplicação

A aplicação não utiliza Entity Framework ou instâncias de Banco de Dados. Todo o conteúdo catalogado encontra-se diretamente nos *Controllers* do MVC.

1.  Certifique-se de ter o **.NET 10.0 SDK** (ou compatível com a versão do projeto) instalado.
2.  Abra o terminal na pasta raiz do projeto.
3.  Compile a aplicação ignorando o restore, caso esteja em um ambiente de desenvolvimento sem pacotes externos para recuperar:
    ```bash
    dotnet build --no-restore
    ```
4.  Execute a aplicação:
    ```bash
    dotnet run
    ```
5.  Acesse `http://localhost:5239` no seu navegador. (Em caso de erro "Address already in use", encerre o processo rodando `kill $(lsof -t -i :5239)` e tente novamente).

## Protótipos Estáticos (WEB3)

Dentro da pasta `/WEB3`, encontra-se uma versão puramente estática de prototipagem do Front-End (apenas HTML, CSS e JS, sem o backend C# ASP.NET Core).
A manutenção de estilos ou funcionalidades no Frontend geralmente reflete também nas atualizações dentro deste diretório para manter consistência no processo de design e documentação.

Para rodar os protótipos visuais isoladamente:
1.  Navegue até o diretório WEB3: `cd WEB3`
2.  Inicie um servidor local HTTP rápido através do Python:
    ```bash
    python3 -m http.server 8000
    ```
3.  Acesse `http://localhost:8000` em seu navegador.
