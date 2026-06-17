# Biblioteca - Projeto Web MVC e SPA-Like

Este projeto é uma aplicação web de biblioteca virtual desenvolvida em ASP.NET Core MVC (C#), utilizando HTML, CSS, e JavaScript no frontend. Ele implementa um padrão híbrido: o roteamento inicial e os dados são fornecidos pelo backend (MVC), mas a navegação e o estado são gerenciados no lado do cliente como uma SPA (Single Page Application).

## Arquitetura e Decisões de Design

- **Sem Banco de Dados (Hardcoded):** Para facilitar a prototipação e focar na construção da interface e lógica de estado do cliente, o catálogo de livros é codificado de forma estática dentro do `BibliotecaController`. Entity Framework não é utilizado.
- **Client-Side State Management:** A navegação entre as páginas do Catálogo, Detalhes do Livro e Perfil do Autor utiliza a API do `localStorage` do navegador para evitar viagens desnecessárias ao servidor (`roundtrips`). Quando o usuário clica em um livro, os dados (título, autor, capa) são salvos temporariamente, e o roteamento segue para as Views genéricas (`Livro.cshtml`, `Autor.cshtml`) que se hidratam com essas informações no lado do cliente.
- **Segurança (Prevenção XSS):** Na manipulação de DOM baseada em inputs de usuários (como a busca ou renderização de títulos baseada em atributos locais), o projeto segue a diretriz de **sempre utilizar `innerText` em vez de `innerHTML`**.

## Funcionalidades Principais

1. **Catálogo Fluído:** Uma vitrine de clássicos com um carrossel horizontal de rolagem suave e opção para expandir o grid e visualizar todos os itens em blocos (responsivo).
2. **Sistema de Busca em Tempo Real:** Uma barra de pesquisa dinâmica na página inicial filtra os livros baseando-se no título ou autor conforme o usuário digita (usando o evento `oninput` para garantir que colagens e interações de scripts funcionem adequadamente).
3. **Sistema de Favoritos:**
   - Usuários podem adicionar e remover livros dos favoritos através de um botão na página de Detalhes da Obra.
   - O estado é persistido no `localStorage` sob a chave `bibliotecaFavoritos` (um Array JSON).
   - Livros favoritados exibem uma "⭐" (estrela) na página inicial.
   - O Catálogo possui um filtro rápido (checkbox) para visualizar apenas as obras favoritadas.

## Como Executar o Projeto

1. Certifique-se de ter o SDK do .NET (versão compatível com a definida no projeto, ex: `net10.0`) instalado.
2. Navegue até o diretório raiz do projeto no terminal.
3. Para compilar o projeto (em ambientes com restrições de conectividade NuGet, utilize a flag offline):
   ```bash
   dotnet build --no-restore
   ```
4. Para rodar o servidor localmente:
   ```bash
   dotnet run
   ```
5. Acesse a aplicação no navegador em: `http://localhost:5239` (ou na porta definida pelo servidor).

**Nota de Desenvolvimento:** Se a porta já estiver em uso, você pode liberá-la usando: `kill $(lsof -t -i :5239)`.

## Sobre o diretório WEB3

A pasta `WEB3/` na raiz do repositório contém protótipos visuais estáticos e isolados (HTML/CSS) das telas do projeto. Eles foram utilizados para modelar a UI antes da implementação final em ASP.NET MVC. Veja o `WEB3/README.md` para mais informações.