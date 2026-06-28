# WEB3 - Protótipos Estáticos UI

Esta pasta foi mantida para armazenar os mockups HTML e CSS originais de demonstração da interface (Front-End Design System), criados antes e durante a conversão do design para o ASP.NET Core MVC (C#).

## Funcionalidades do Protótipo (Estático)
Mesmo sendo uma representação estática, alguns componentes possuem funcionalidade própria, baseada no ambiente de navegador (Javascript `localStorage`):

- **Favoritos (`WEB3/Livro/index.html`):** Interação visual (estrelas e botões). Os itens salvos refletirão em qualquer outra interface do projeto que também ler a chave `bibliotecaFavoritos` (inclusive o projeto .NET se acessado do mesmo domínio ou local de desenvolvimento).

## Como Visualizar

Abra esta pasta no terminal e sirva os arquivos utilizando python (ou outra extensão web server para HTML estático):
```bash
python3 -m http.server 8000
```
Navegue para `http://localhost:8000/WEB3/Livro/index.html` para testar os mockups e UI.