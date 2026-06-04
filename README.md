# Biblioteca - Catálogo de Clássicos

Uma aplicação web moderna para explorar um catálogo de livros clássicos. A interface é construída seguindo o padrão Single Page Application (SPA), garantindo uma experiência de navegação rápida e sem recarregamentos completos da página.

## Funcionalidades

- **Catálogo de Livros:** Visualização em formato de carrossel ou grade com os clássicos literários.
- **Pesquisa em Tempo Real:** Barra de pesquisa que permite filtrar os livros por título ou autor usando JavaScript puro no lado do cliente.
- **Sistema de Favoritos:** Possibilidade de adicionar e remover livros dos favoritos. O status é salvo no `localStorage` do navegador e sinalizado visualmente com uma estrela (⭐) na capa dos livros favoritados.
- **Visualização de Detalhes:** Navegação rápida entre os detalhes do livro e o perfil do autor sem requisições adicionais ao servidor (utilizando `localStorage` para a passagem de dados).
- **Protótipos Estáticos:** O projeto inclui um diretório `WEB3/` que contém versões puramente HTML/CSS/JS da interface para facilitar o design e a prototipação.

## Estrutura e Dependências

- Desenvolvido em **ASP.NET Core MVC (C#)**.
- Interface construída com **HTML5**, **CSS3** (variáveis CSS, Grid, Flexbox) e **JavaScript vanilla**.
- A persistência de dados de navegação e favoritos é gerenciada via **localStorage**.

## Como Executar

1. Certifique-se de ter o [.NET SDK](https://dotnet.microsoft.com/download) instalado.
2. Na raiz do repositório, rode o comando:
   ```bash
   dotnet run
   ```
3. O servidor estará acessível em `http://localhost:5239` (ou na porta configurada).
