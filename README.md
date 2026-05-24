# Biblioteca Clássicos

Um catálogo moderno de livros clássicos desenvolvido em **ASP.NET Core MVC (C#)**, com uma interface responsiva, elegante e baseada em navegação **SPA-Like**. O sistema dispensa banco de dados convencional, usando dados "hardcoded" de forma otimizada nos controllers e transferindo estado para o front-end via `localStorage`.

## Características Principais

*   **Busca em Tempo Real:** Pesquisa ultrarrápida integrada diretamente na vitrine (Home). Digite o título, autor ou gênero para filtrar os livros na hora (através do evento `oninput` do JavaScript, alterando a exibição CSS).
*   **Sistema de Favoritos:** Ao clicar em "Adicionar aos Favoritos" nos detalhes de um livro, o sistema salva o livro escolhido localmente no navegador (`localStorage`), alterando o estado visual do botão instantaneamente.
*   **SPA-Like Navigation:** A transição entre os detalhes de diferentes livros e seus autores acontece transferindo metadados via JSON pelo `localStorage`, e injetando as informações dinamicamente usando JavaScript no carregamento das Views (`Livro.cshtml`, `Autor.cshtml`).
*   **Design Fluido:** Estilização com Flexbox e Grid (`biblioteca.css`), transições animadas e botões em estilo "pill". Cores de capas são geradas dinamicamente usando códigos Hex.

## Como Executar

O projeto foca no framework **.NET 10.0**.

1. Certifique-se de que a porta `5239` (ou a padrão configurada) está livre.
2. Abra o terminal na raiz do projeto.
3. Compile a aplicação sem logs de restauração desnecessários:
   ```bash
   dotnet build
   ```
4. Execute a aplicação:
   ```bash
   dotnet run
   ```
5. Acesse `http://localhost:5239` no navegador.

## Estrutura do Protótipo (WEB3/)

Para design e testes focados unicamente na UI/UX sem precisar compilar o C#, a pasta `WEB3/` serve como um protótipo estático (HTML, CSS e JS puros). As mesmas lógicas implementadas nas Views (como Favoritos e animações) devem sempre ser replicadas na pasta `WEB3/` para manter a paridade da documentação visual.
