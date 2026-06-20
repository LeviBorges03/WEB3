# WEB3 Prototyping

Esta pasta contém versões prototipadas estáticas da interface da Biblioteca.

Foi inicialmente desenvolvida de forma separada utilizando apenas **HTML**, **CSS** e **JS**, para validação de layouts (ex. páginas de Livro e Autor), sendo posteriormente integradas no ecossistema do `ASP.NET Core MVC`.

## Como Executar Localmente
Para avaliar as interfaces estáticas separadamente do servidor C#:

1. Navegue até este diretório:
   ```bash
   cd WEB3
   ```
2. Rode um servidor em Python para expor os HTMLs:
   ```bash
   python3 -m http.server 8000
   ```
3. Acesse `http://localhost:8000/Livro` ou `http://localhost:8000/Autor` no navegador.

## Diferenças do Projeto Principal (`ASP.NET MVC`)
- A pasta `WEB3` não consome o backend e não renderiza layouts do `_Layout.cshtml`.
- As lógicas de "Adicionar a Favoritos", "Carrossel Horizontal" e "Pesquisa Integrada" não estão implementadas ou funcionam com mocks nesta pasta, diferente do root do repositório onde dados reais integram o `localStorage`.
- É um acervo mantido passivamente como referência visual de UI/UX. Para modificações reais, utilize os diretórios `wwwroot` e `Views/Biblioteca`.
