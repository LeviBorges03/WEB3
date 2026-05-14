# WEB3 (Prototipação Estática)

Este diretório contém uma representação puramente estática em HTML, CSS e JavaScript da interface de usuário da Biblioteca construída no diretório raiz. O objetivo desta pasta é fornecer um ambiente isolado para o design e prototipagem da interface web sem a necessidade do backend ASP.NET Core MVC.

## Estrutura
- `Livro/` e `Autor/` possuem seus próprios arquivos `index.html` estáticos que imitam os respectivos arquivos `.cshtml`.

## Funcionalidades Implementadas
- **Sistema de Favoritos:** O `WEB3/Livro/index.html` inclui um botão "Adicionar aos Favoritos", que gerencia o estado da obra selecionada localmente usando a chave `bibliotecaFavoritos` no `localStorage`. Este comportamento é idêntico ao implementado em `Views/Biblioteca/Livro.cshtml`.

## Como Executar
Nenhuma dependência ou build step é necessário. Para visualizar as páginas neste diretório, basta abrir o arquivo `index.html` desejado diretamente no navegador web.