# Sistema de Biblioteca

Este é um projeto ASP.NET Core MVC focado em construir um catálogo de clássicos da literatura. O sistema não utiliza banco de dados para facilitar a demonstração de conceitos de manipulação de modelos em memória e interação no cliente.

## Funcionalidades Principais

- **Catálogo de Livros:** Exibição de dezenas de livros clássicos listados com dados dinâmicos.
- **Busca em Tempo Real:** Uma barra de pesquisa permite filtrar as obras por título instantaneamente sem recarregar a página.
- **Sistema de Favoritos:** Os usuários podem marcar livros como favoritos (ícone ⭐ no catálogo e botão na página de detalhes). A preferência é armazenada no navegador utilizando o `localStorage` (chave `bibliotecaFavoritos`).
- **Navegação SPA-like:** Transferência de estados e informações entre as páginas usando `localStorage` (chaves `livroAtual` e `autorAtual`) em vez de requisições back-end, proporcionando transições muito mais rápidas e fluidas.

## Como Executar

Para rodar este projeto localmente, tenha o SDK do .NET 10.0 instalado.

```bash
dotnet build
dotnet run
```
O servidor de desenvolvimento local costuma rodar na porta 5239 (http://localhost:5239).

## Estrutura do Projeto
- `Controllers/` e `Models/`: Onde ficam os dados codificados de maneira fixa (mockados) e a lógica de apresentação.
- `Views/Biblioteca/`: Views (Index, Livro, Autor) que consomem estilos CSS em comum.
- `WEB3/`: Protótipos puramente estáticos para testar visuais e comportamentos isoladamente antes de integrar no ASP.NET Core.

## Dicas
A aplicação conta com um design moderno com botões interativos e responsivos. Foi feito uso pesado do `event.stopPropagation()` para garantir que cliques em botões dentro do cartão (ex: favoritos, link do autor) não ativem o clique global da capa do livro.
