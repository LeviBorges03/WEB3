# Biblioteca Digital (ASP.NET Core)

Um projeto moderno de catálogo de livros desenvolvido em ASP.NET Core MVC e C#, com uma interface interativa focada em navegação tipo SPA (Single Page Application) utilizando Vanilla JavaScript e `localStorage`.

## Funcionalidades Principais
- **Catálogo de Clássicos:** Uma vitrine de obras clássicas da literatura com um design agradável e carrossel de rolagem.
- **Sistema de Pesquisa:** Barra de busca em tempo real para filtrar obras e autores (agnóstica a acentos).
- **Sistema de Favoritos:** Capacidade de adicionar e remover livros dos favoritos diretamente pelo catálogo (ícone ⭐) ou pela página de detalhes, com os dados persistidos no `localStorage`.
- **Navegação Suave:** Transição de dados entre o catálogo, a página do livro e do autor feita no lado do cliente, sem necessidade de recarregar o servidor a todo clique.

## Como Executar
1. Certifique-se de ter o SDK do .NET 10.0 instalado.
2. Clone o repositório e navegue até a raiz.
3. Restaure as dependências e compile o projeto:
   ```bash
   dotnet build
   ```
4. Execute a aplicação:
   ```bash
   dotnet run
   ```
5. Acesse no seu navegador em `http://localhost:5239` (ou a porta listada no terminal).

## Estrutura
- **`/Controllers` e `/Models`:** Lógica de negócio e dados (hardcoded) do lado do servidor em C#.
- **`/Views`:** Componentes de interface utilizando Razor (HTML/C#).
- **`/wwwroot`:** Arquivos estáticos (CSS, JS, Imagens).
- **`/WEB3`:** Diretório contendo as provas de conceito estáticas (protótipos) da interface.
