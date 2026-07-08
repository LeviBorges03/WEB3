# WEB3 - Protótipos Estáticos

Este diretório contém a representação estática, puramente em HTML/CSS, e isolada (sem ASP.NET Core) da interface de usuário da Biblioteca. É usado para facilitar testes de prototipagem rápida, verificar design, responsividade e construir as Views de forma rápida e segura antes da integração no backend MVC.

## Como Visualizar

Para simular o ambiente local para visualização do design, você pode rodar um servidor HTTP simples.

Execute no terminal (na raiz deste diretório `WEB3`):

```bash
python3 -m http.server 8000
```

E em seguida, acesse via navegador em `http://localhost:8000`.

## Dicas e Alinhamento

Ao realizar manutenções no estilo (CSS) ou nas estruturas das páginas, lembre-se de atualizar tanto o ambiente estático `WEB3` quanto os arquivos Razor (`.cshtml`) da raiz do projeto para manter a consistência entre o protótipo e o projeto final.