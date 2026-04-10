# Biblioteca Digital (ASP.NET Core MVC)

Bem-vindo ao projeto Biblioteca Digital! Esta aplicação web é desenvolvida utilizando o framework ASP.NET Core MVC (C#).

## Funcionalidades e Arquitetura

O projeto se destaca pelo uso misto de renderização no servidor (Server-Side Rendering) e gerenciamento de estado no lado do cliente (Client-Side State Management). Isso nos permite entregar uma experiência rápida (SPA-Like) sem a necessidade de uma Single Page Application complexa em React ou Angular.

### Navegação SPA-Like via `localStorage`
Em vez de depender de recarregamentos completos de página para cada navegação entre views, o sistema armazena informações temporárias no `localStorage` do navegador.

- Quando um usuário clica num livro no **Catálogo Principal (Home)**, os dados deste livro são salvos no `localStorage`.
- O usuário é redirecionado para a View genérica `Livro.cshtml`.
- Ao carregar a página do Livro, o JavaScript lê o `localStorage` e preenche dinamicamente o título, a capa, o autor, sinopse, entre outros detalhes.

Este mesmo princípio é aplicado para a exibição dos detalhes de um Autor (na view `Autor.cshtml`).

### Barra de Pesquisa e Filtros (Client-Side)
A pesquisa por obras no Catálogo Principal foi implementada inteiramente no lado do cliente com JavaScript para garantir respostas em tempo real:
- Os usuários podem pesquisar pelo título do livro, pelo nome do autor ou pelo gênero.
- A função de busca filtra os elementos da DOM em tempo real e adapta o layout (expandindo a visualização em grade se estiver no modo carrossel) conforme necessário.

### Sistema de Favoritos
Os usuários podem salvar seus livros prediletos utilizando o sistema de favoritos:
- Na página de detalhes do Livro, o usuário pode clicar em "Adicionar aos Favoritos".
- Os livros favoritos são guardados num array persistente dentro do `localStorage` do navegador.
- Na página Home (Catálogo), o usuário pode clicar em "Mostrar Apenas Favoritos", e a grade de livros será instantaneamente filtrada para mostrar apenas os livros que foram favoroitados, integrando-se perfeitamente com a barra de pesquisa!

## Estilização e UI/UX
- **Visual Moderno e Relaxante:** Cores selecionadas para proporcionar um baixo estresse visual, ideal para leitura.
- **Micro-interações:** Botões elegantes com efeito pílula, transições suaves (hovers) e rolagem suave.
- **Capas Dinâmicas de Livros:** Os livros não carregam imagens estáticas pesadas; eles utilizam cores hexadecimais sólidas atreladas ao tema da obra, geradas via CSS.

## Como Executar o Projeto

Certifique-se de ter o SDK do .NET 10 (ou compatível configurado no projeto) instalado.

1. Restaure as dependências do projeto:
   ```bash
   dotnet restore
   ```
2. Compile a aplicação:
   ```bash
   dotnet build
   ```
3. Execute o servidor:
   ```bash
   dotnet run
   ```

## Boas Práticas e Convenções Adotadas
- O projeto não utiliza o `ServerVersion.AutoDetect` do EntityFrameworkCore de maneira hardcoded para evitar lentidões na inicialização, definindo versões de MySQL de forma estática.
- Listas estáticas e mockadas ficam alocadas em variáveis otimizadas nos controladores para aliviar a pressão do Garbage Collector.
