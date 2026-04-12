# Documentação Específica do Frontend (WEB3)

Este diretório mantém anotações e arquivos de documentação mais específicos sobre as lógicas exclusivas de interface utilizadas nas Views do ASP.NET Core (`Index`, `Livro`, `Autor`).

## Dinâmica SPA-Like com Vanilla JS

A premissa fundamental das telas desenvolvidas na Biblioteca é proporcionar uma experiência de "Single Page Application" (SPA) sem a complexidade de um framework como React ou Angular.

Para isso, empregamos o uso estratégico do `localStorage` do navegador:
1.  **Index.cshtml (Vitrine):** Ao invés de o link do Livro ou do Autor redirecionar para um Controller com um ID via QueryString (que forçaria uma nova consulta no banco), o evento `onclick` dispara uma função em JavaScript (`abrirLivro` / `abrirAutor`).
2.  **Armazenamento Temporário:** Esta função serializa os dados básicos do livro atual (Título, Autor, Gênero, CorCapa) via JSON e salva em uma chave no `localStorage` (`livroAtual` ou `autorAtual`).
3.  **Apresentação:** A View genérica correspondente (`Livro.cshtml` ou `Autor.cshtml`) é aberta. Em seu evento de inicialização (`DOMContentLoaded`), ela captura esses dados locais e preenche a interface instantaneamente.

## Novas Funcionalidades de Interface

### Busca e Filtros
A `Index.cshtml` inclui uma barra de busca dinâmica no topo do catálogo.
- Ela funciona escutando o evento `oninput`, permitindo que os `.livro-card` sejam ocultados ou mostrados em tempo real conforme o usuário digita.
- Para manter os padrões de design, os itens visíveis têm sua propriedade `display` configurada como `flex` (e não uma string vazia `""`).

### Sistema de Favoritos
O sistema de favoritos atua exclusivamente pelo lado do cliente.
- **Na página de Livro (`Livro.cshtml`):** O usuário encontra o botão "Adicionar aos Favoritos". Ao clicar, o livro inteiro é gravado em um array `livrosFavoritos` no `localStorage`. Se o livro já for favorito, ele é removido do array e o botão reage visualmente (ícone de coração e troca de cor).
- **Na vitrine principal (`Index.cshtml`):** Há um botão para "Mostrar Favoritos". Esta função integra-se logicamente ao filtro de busca. O estado deste botão cruza com o valor da barra de texto para mostrar "apenas favoritos que correspondam ao termo digitado".

Para detalhes mais microscópicos, confira os subdiretórios ou comentários direto no código-fonte em HTML/JS.