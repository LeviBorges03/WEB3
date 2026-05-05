# WEB3: Protótipos de Interface de Usuário

Este diretório contém uma representação puramente estática e isolada da interface da Biblioteca Clássica.

## Propósito

A pasta `WEB3/` atua como um laboratório ou "sandbox" para design de UI e testes de experiência do usuário (UX). Ela **não** interage com o ASP.NET Core e consiste estritamente em arquivos HTML, CSS e JavaScript puros (Vanilla). Essa abordagem facilita a validação rápida de layouts, estilos e animações CSS antes da integração no projeto MVC principal.

## Funcionalidades e Telas Disponíveis

Atualmente, o laboratório conta com protótipos em HTML das seguintes telas:

*   **Página de Detalhes da Obra (`Livro/index.html`)**: Protótipo de como os detalhes de um livro específico devem se parecer. Demonstra também a estrutura base da interface responsiva e inclui a simulação isolada do **Sistema de Favoritos** armazenado no `localStorage` sob a chave `bibliotecaFavoritos`.
*   **Página do Autor (`Autor/index.html`)**: Protótipo estático do layout de exibição da biografia e obras relacionadas ao autor.

## Regras de Integração

Sempre que uma nova funcionalidade (visual ou comportamental em JS) for adicionada aqui, ela deve ser devidamente espelhada para as *Views* oficiais do projeto (localizadas em `../Views/Biblioteca/`) ou na estilização em `../wwwroot/css/biblioteca.css`. Da mesma forma, alterações visuais feitas diretamente no sistema ASP.NET devem ter seu protótipo em `WEB3/` atualizado para manter a consistência de documentação do design.