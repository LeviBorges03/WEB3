# WEB3 - Protótipos de Interface

A pasta `WEB3/` deste repositório contém as versões estáticas (puro HTML, CSS e JavaScript Vanilla) da interface da Biblioteca.

## Propósito

Estes arquivos não possuem dependência com o backend em ASP.NET Core MVC (presente na raiz do repositório). O objetivo desta pasta é atuar como um "laboratório" (sandbox) para os designers de UI/UX testarem novas paletas de cores, animações CSS, responsividade e layout de novas telas.

Quando um layout ou comportamento for validado aqui, ele deve ser portado posteriormente para as Views (CSHTML) e arquivos na pasta `wwwroot` no projeto em C#.

A lógica front-end baseada no armazenamento local (API de `localStorage`), incluindo o sistema de Favoritos implementado para o protótipo da página do Livro, também pode ser testada e depurada por aqui antes de escalar para o projeto principal.

## Como Visualizar

Para exibir esses protótipos de forma que referências a arquivos CSS e imagens relativas funcionem adequadamente, é recomendado subir um servidor local rápido (como no Python) ao invés de apenas abrir o arquivo de arquivo local (`file://`).

Você pode rodar:

```bash
cd WEB3
python3 -m http.server 8000
```

Feito isso, abra `http://localhost:8000` em seu navegador de escolha.
