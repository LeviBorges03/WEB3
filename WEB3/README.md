# WEB3 - Interface Prototipada

Esta pasta armazena o protótipo inicial (e apenas focado no Front-end) das telas do nosso sistema Biblioteca, sendo constituída puramente por HTML, CSS e um pouco de JavaScript.

## Atualizações de Features

Durante a integração contínua, as funcionalidades a seguir foram desenvolvidas na versão MVC do projeto e os conceitos podem ser referenciados:

- **Sistema de Busca em Tempo Real**: Filtro dos cards da vitrine pelo evento de JS `oninput` baseado no título e no autor.
- **Armazenamento de Favoritos**: Criação de array JSON armazenado no `localStorage` sob a chave `bibliotecaFavoritos`, que permite favoritar os livros (botão na visualização da obra) e realçá-los com uma ⭐ na visualização em grade no Catálogo principal.

*Nota: As implementações ativas e com os dados em lote completos estão no escopo global do projeto (dentro das Views ASP.NET Core MVC).*