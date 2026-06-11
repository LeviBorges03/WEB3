# Protótipos Estáticos - WEB3

Este diretório contém os protótipos puramente estáticos criados com **HTML, CSS e JavaScript puros** para servirem como base de design, UX/UI e validação de scripts (como o armazenamento SPA-like e favoritos) antes de serem integrados ao projeto ASP.NET Core MVC na raiz do repositório.

## Estrutura
- **Autor**: Contém o layout da página do Autor.
- **Livro**: Contém o layout da página do Livro e um protótipo local do script para favoritar o livro com estado mantido pelo `localStorage`.

## Como Visualizar Localmente
Para garantir que todos os links e assets relativos nestes HTMLs carreguem corretamente, execute um pequeno servidor local (em vez de apenas abrir os arquivos duas vezes no seu navegador):

```bash
# Na raiz deste diretório WEB3, execute:
python3 -m http.server 8000
```
E então, acesse: `http://localhost:8000` ou as rotas das respectivas páginas como `http://localhost:8000/Livro/`.