# WEB3 - Prototipagem da Biblioteca

Este diretório contém a versão estática e de prototipagem (HTML, CSS e JavaScript puros) da nossa aplicação de Biblioteca construída em ASP.NET Core MVC (na pasta raiz). Ele é utilizado de forma isolada para modelar e visualizar o design e o layout da experiência web de forma rápida e sem depender do servidor em backend.

## Funcionalidades implementadas (Mock):
- **Barra de Busca Dinâmica**: Interatividade de buscar e ocultar componentes HTML baseados no "title, autor ou gênero" do livro.
- **Sistema de Favoritos**: Usa `localStorage` para simular adicionar e remover "favoritos" na view do Livro Atual.
- **Passagem de Parâmetros Static-SPA**: Usa o estado estático para salvar chaves e itens que permitem uma visualização mockada nas páginas subsequentes, simulando o ASP.NET View Engine.

Qualquer atualização nas lógicas isoladas da View devem ser replicadas e testadas neste diretório para manter consistência nos designs e ideias futuras.