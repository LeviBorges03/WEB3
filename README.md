# Sistema de Biblioteca

Bem-vindo ao projeto do Sistema de Biblioteca, uma aplicação web focada em navegação fluida, interface relaxante e prototipação isolada do lado do cliente. O projeto foi construído utilizando o ASP.NET Core MVC aliado a conceitos de Single Page Application (SPA) implementados por meio de JavaScript e `localStorage`.

## Funcionalidades e Estrutura

- **Catálogo de Obras (Home):** Uma vitrine para exibir os livros cadastrados na biblioteca. Oferece visualização em carrossel rolável e expansível.
- **Barra de Pesquisa:** Implementada de forma que a pesquisa atua em tempo real (utilizando o evento `oninput`), filtrando pelo título ou autor sem a necessidade de recarregar a página.
- **Sistema de Favoritos:** O usuário pode "Adicionar aos Favoritos" diretamente na tela de detalhes de um livro. Esta informação é salva localmente usando a chave `bibliotecaFavoritos` no `localStorage`, garantindo a persistência na sessão do navegador sem precisar conectar ao backend.
- **Protótipo (WEB3):**
  - Existe uma pasta denominada `WEB3/` na raiz do repositório. Ela contém uma representação puramente estática e isolada (apenas HTML, CSS, e JS) para rápida visualização e prototipação do design e comportamento do front-end sem a necessidade de executar o projeto ASP.NET Core.
  - Toda vez que uma alteração é feita no visual ou comportamento via JavaScript, ela deve ser sincronizada entre as visualizações do .NET (`Views/`) e os arquivos do protótipo (`WEB3/`).

## Como Executar o Projeto

1. Certifique-se de possuir o .NET 10.0 SDK instalado.
2. Certifique-se de configurar o acesso ao banco de dados MySQL nas variáveis de ambiente em vez do `appsettings.json` (por exemplo: `ConnectionStrings__DefaultConnection`). O servidor MySQL precisa ser da versão `8.0.40`.
3. Abra o terminal na raiz do projeto e execute:
   ```bash
   dotnet build
   dotnet run
   ```
4. Caso ocorra erro de porta (`Address already in use`) para a porta `5239`, certifique-se de matar o processo anterior executando `kill $(lsof -t -i :5239)`.

## Destaques de Arquitetura

- **State Management Local:** A transferência de contexto (como o autor atual ou o livro atual escolhido no catálogo) é gerida via JavaScript com `localStorage`, reduzindo requisições ao backend e providenciando uma navegação extremamente rápida (SPA-like).
- **Interface e UI/UX:** Foram utilizados botões "pill-shaped" (com bordas arredondadas) e efeitos de hover de translação com `box-shadow` modernos e cores de contraste balanceadas para criar um ambiente de leitura agradável.
