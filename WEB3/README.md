# Biblioteca - WEB3 Prototypes

Esta pasta contém protótipos puramente estáticos (HTML/CSS/JS) das páginas de Detalhes do Livro e Autor, usados para guiar o desenvolvimento do frontend da aplicação principal em ASP.NET Core MVC.

## Funcionalidades Implementadas nos Protótipos

*   **Página de Livro:** Layout demonstrando a capa, informações (título, autor, publicação), sinopse e um card do autor.
*   **Página de Autor:** Layout demonstrando foto, biografia e uma listagem de obras notáveis.
*   **Interatividade Básica:** A página de Livro inclui uma simulação do botão "Adicionar aos Favoritos", utilizando JS nativo e `localStorage` (chave `bibliotecaFavoritos`) para persistir o estado no navegador, demonstrando o comportamento esperado no sistema final.

## Como Visualizar

Para visualizar estes protótipos localmente, inicie um servidor web simples dentro desta pasta. Por exemplo, usando Python:

```bash
cd WEB3
python3 -m http.server 8000
```

Em seguida, acesse as URLs no seu navegador:
*   Livro: `http://localhost:8000/Livro/`
*   Autor: `http://localhost:8000/Autor/`
