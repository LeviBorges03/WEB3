# Biblioteca Virtual

Este projeto é uma aplicação web para gerenciamento e visualização de um catálogo de livros. Ele foi construído usando **ASP.NET Core MVC** (em C#) para a estrutura principal e utiliza **HTML, CSS e JavaScript puros** no frontend para criar uma experiência ágil semelhante a um SPA (Single Page Application).

## Arquitetura e Estado

### Sem Banco de Dados
A aplicação atualmente **não utiliza um banco de dados**. Todos os dados dos livros (título, autor, gênero, páginas, capa, etc.) estão mockados na `BibliotecaController`.

### Gerenciamento de Estado no Cliente (SPA-Like)
Para navegar entre o Catálogo (Index), a visão do Livro e a visão do Autor sem precisar recarregar todos os dados do backend, a aplicação faz um uso forte do `localStorage` do navegador.

*   Quando um usuário clica em um livro, o objeto do livro é salvo no `localStorage` sob a chave `livroAtual`.
*   Quando o usuário navega para a visão do Livro (`Livro.cshtml`), o JavaScript lê o `livroAtual` e injeta os detalhes no DOM.
*   O mesmo ocorre para o autor, usando a chave `autorAtual`.
*   O sistema de "Favoritos" também utiliza o `localStorage`, salvando uma lista de títulos de livros em um array JSON sob a chave `bibliotecaFavoritos`.

### Capas dos Livros
As capas dos livros não são arquivos de imagem (`.jpg`, `.png`). Por simplicidade e performance visual, cada livro tem uma propriedade `CorCapa` que armazena um código hexadecimal (ex: `#3498db`), e esta cor é aplicada via CSS (`background-color`) para simular a capa do livro.

---

## Como Executar o Projeto Principal (ASP.NET Core)

Certifique-se de ter o **.NET SDK** instalado na sua máquina (o projeto usa a versão mais recente).

1. Abra um terminal na raiz do repositório (onde o arquivo `.csproj` está localizado).
2. Para compilar o projeto e garantir que não há erros:
   ```bash
   dotnet build
   ```
3. Para iniciar a aplicação:
   ```bash
   dotnet run
   ```
4. A aplicação geralmente estará disponível em `http://localhost:5239` (verifique a saída do terminal para confirmar a porta exata).

> **Aviso de Timeout em Ambientes Remotos:** Se a execução do `dotnet build` ou `dotnet run` demorar muito e causar timeout, você pode executar em background redirecionando os logs:
> `dotnet run > dotnet_run.log 2>&1 &`

---

## Como Visualizar os Protótipos Estáticos (WEB3)

A pasta `WEB3` contém uma versão puramente estática das páginas (apenas HTML, CSS e JS, sem o C#). Estes arquivos são utilizados para desenhar as interfaces de usuário e testar estilos isoladamente antes de integrá-los à aplicação ASP.NET.

Qualquer alteração na UI do projeto principal também deve ser testada e replicada nos protótipos da pasta `WEB3`.

Para servir os arquivos da pasta `WEB3` localmente:

1. Navegue até a pasta WEB3:
   ```bash
   cd WEB3
   ```
2. Utilize o Python para levantar um servidor web simples:
   ```bash
   python3 -m http.server 8000
   ```
3. Abra o navegador e acesse `http://localhost:8000/Livro/` ou `http://localhost:8000/Autor/`.

---

## Funcionalidades Recentes

*   **Barra de Pesquisa:** Foi adicionada uma barra de pesquisa responsiva no catálogo (`Index.cshtml`). Ela filtra os livros instantaneamente usando o evento `oninput`, comparando o termo buscado contra o título, o autor e o gênero.
*   **Favoritos:** Na tela de detalhes do livro, há agora a funcionalidade de adicionar a obra aos "Favoritos". O estado é mantido pelo `localStorage` no próprio navegador, garantindo que o livro continue marcado mesmo ao retornar.
*   **Segurança:** A aplicação foi configurada para responder estritamente a `localhost` (`AllowedHosts: "localhost"` em `appsettings.json`), prevenindo ataques de HTTP Host Header.
