# Sistema de Biblioteca Digital

Este projeto é um sistema web responsivo e moderno para catálogo de livros clássicos, estruturado em C# (.NET) com ASP.NET Core MVC, e com suporte a protótipos puramente estáticos para web design (WEB3).

## Arquitetura e Tecnologias
- **Backend:** C# / ASP.NET Core MVC (.NET 10.0). Os dados são mockados no Controller, eliminando a dependência do Entity Framework ou banco de dados externo.
- **Frontend Principal:** Views em Razor (`.cshtml`), com CSS modular (`wwwroot/css/biblioteca.css`) e SPA-like behavior.
- **SPA-Like com Vanilla JS:** A aplicação utiliza o `localStorage` intensivamente para passar dados de estado (como qual livro ou autor está aberto) sem precisar fazer um request ao backend para recarregar informações, tornando a navegação mais rápida. Chaves utilizadas:
  - `livroAtual`: Objeto JSON com dados do livro selecionado.
  - `autorAtual`: String com o nome do autor selecionado.
  - `bibliotecaFavoritos`: Array JSON com os títulos dos livros favoritados pelo usuário.
- **Protótipo (WEB3/):** Um diretório isolado contendo arquivos HTML/CSS puros que foram usados para prototipar a interface sem a dependência do motor Razor. Deve ser mantido consistente com a aplicação principal.

## Instruções de Execução

### Rodar o Projeto Principal (ASP.NET Core)
1. Certifique-se de que a porta `5239` não está em uso (`kill $(lsof -t -i :5239)`).
2. Execute o comando: `dotnet run` (Opcionalmente: `dotnet build` primeiro para compilar).
3. Acesse via browser em `http://localhost:5239`.

### Rodar os Protótipos Estáticos (WEB3)
Para fins de revisão de UI/UX, você pode servir a pasta WEB3 localmente usando o Python:
1. Navegue até o diretório: `cd WEB3`
2. Inicie um servidor HTTP simples: `python3 -m http.server 8000`
3. Acesse `http://localhost:8000/Livro/` ou `http://localhost:8000/Autor/`.
