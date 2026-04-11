# Documentação do Módulo WEB3 (Biblioteca Web)

Este diretório contém anotações, descrições complementares e arquivos relacionados ao projeto **Biblioteca Web**, focado nas entregas e requisitos para WEB3.

## Estrutura do Projeto

O projeto principal está localizado na raiz do repositório, mas as diretrizes de WEB3 abordam especificamente a interação entre o C# (Backend) e as práticas de Front-end (UI/UX e JS).

### Principais Entregas deste Módulo

1. **Filtro e Busca:** A barra de pesquisa (pill-shaped) foi implementada na página do catálogo (Index) para permitir buscas em tempo real em cima do DOM carregado, evitando requisições extras ao servidor.
2. **Sistema de Favoritos SPA-like:**
   - A lista de obras "favoritadas" pelo usuário é armazenada diretamente no navegador usando o `localStorage` (chave `favoritos`).
   - A view de detalhes (`Livro.cshtml`) lida com a verificação de estado e possibilita "Adicionar" ou "Remover".
   - O catálogo (Home) pode ser filtrado usando o botão "Mostrar Favoritos", alinhado ao lado da busca.
3. **Padrão de UX Moderno:** Os estilos priorizam uma aparência suave (soft edges), cores consistentes via variáveis (`:root` CSS), fontes de leitura agradáveis e responsividade sem quebras rústicas.

### Boas Práticas Empregadas

- **Separação de Preocupações:** O controller envia uma lista ordenada por data descrescente e as views lidam com a interatividade, de modo que o servidor apenas sirva os dados estáticos essenciais na primeira carga.
- **Comentários de Código:** O código JavaScript inserido nos arquivos `.cshtml` está comentado e organizado de forma funcional (funções isoladas como `toggleFavorito` e `filtrarLivros`).
- **Nenhum Artefato Rastreado:** Arquivos de build como as pastas `bin/` e `obj/` estão incluídos no `.gitignore`, evitando o bloqueio de versionamento.

Para instruções de como rodar o projeto principal, consulte o [README.md principal](../README.md) na raiz do repositório.
