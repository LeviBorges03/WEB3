# Protótipos WEB3 - Biblioteca

Esta pasta contém protótipos puramente estáticos (HTML, CSS e JavaScript) do projeto da Biblioteca. Eles foram desenvolvidos para facilitar o design, os testes visuais e a implementação de scripts do lado do cliente (como a navegação SPA-like, sistema de pesquisa e favoritos) sem depender do backend ASP.NET Core MVC.

## Como Visualizar os Protótipos

Para que os scripts baseados em `localStorage` e outras funcionalidades web funcionem perfeitamente, é recomendado servir os arquivos usando um servidor HTTP local simples, em vez de abrir os arquivos HTML diretamente do sistema de arquivos.

Se você tiver o Python instalado, você pode iniciar um servidor rapidamente. Navegue até a raiz do projeto (ou desta pasta `WEB3`) e execute:

```bash
cd WEB3
python3 -m http.server 8000
```

Em seguida, abra o seu navegador e acesse:
[http://localhost:8000](http://localhost:8000)

## Características Testáveis

1. **Pesquisa**: A página principal permite a filtragem da listagem de livros.
2. **Favoritos**: A página de Livro demonstra o botão de adicionar ou remover favoritos interligado ao `localStorage`.
3. **Navegação (Mock)**: Alguns botões simulam a transição de páginas transferindo dados temporários via `localStorage`.