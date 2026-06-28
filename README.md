# Biblioteca Digital

Projeto focado em proporcionar uma experiência moderna, fluida e amigável para explorar livros clássicos da literatura.

## Tecnologias e Funcionalidades

- **ASP.NET Core MVC (C#):** Servidor local provendo as Views dinâmicas de catálogo, permitindo visualizar dezenas de obras no sistema.
- **Single Page Application (SPA) Like:** O fluxo e envio de dados entre as Views da plataforma utilizam propriedades embutidas do frontend, principalmente `localStorage`, sem recarregar o banco de dados desnecessariamente, provendo carregamento instantâneo.
- **Barra de Pesquisa de Obras:** Ferramenta na tela inicial (Home/Index) para filtrar a listagem de livros instantaneamente por título ou autor usando JS puro.
- **Sistema de Favoritos (⭐):** Permite curtir obras favoritas e salvá-las utilizando a key `bibliotecaFavoritos` via Local Storage, com indicação visual nos ícones de estrela e botões da aplicação.
- **Responsividade e Design Minimalista:** Interface moderna com Flexbox e Grid do CSS puro.

## Como Executar a Aplicação ASP.NET Core MVC (C#)

Para testar ou desenvolver na aplicação .NET local, execute o seguinte comando na raiz do repositório:
```bash
dotnet build
dotnet run
```
Acesse `http://localhost:5239` pelo navegador.

---
*Para visualização dos protótipos puramente estáticos HTML/CSS, verifique o README dentro da pasta `WEB3`.*
