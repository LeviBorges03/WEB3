# Protótipo Estático de UI (WEB3)

Este diretório contém uma versão puramente estática (HTML, CSS e JavaScript Vanilla) da interface da aplicação **Biblioteca**.

## Propósito
- **Prototipação Rápida:** Permite o desenvolvimento, teste e refinamento de layouts, componentes visuais e lógicas de frontend (como o `localStorage` para a navegação ou favoritos) de forma isolada, sem a necessidade de inicializar o servidor ASP.NET Core e banco de dados.
- **Validação de Design:** É usado para validar novas implementações visuais e garantir que funcionem corretamente em navegadores.

## Estrutura
- `index.html`, `style.css`: View principal (Catálogo).
- `Livro/`: Mockup estático da página de detalhes do livro.
- `Autor/`: Mockup estático do perfil do autor.

## Diretrizes de Manutenção
Sempre que uma mudança significativa de layout, CSS ou script (como o sistema de Favoritos implementado via localStorage com a chave `bibliotecaFavoritos`) for feita no projeto principal (`Views/`, `wwwroot/css/`), recomenda-se replicar ou validar essas alterações aqui no ambiente estático para garantir a paridade da documentação visual.