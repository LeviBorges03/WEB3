# Biblioteca - Projeto de Catálogo de Livros

Este projeto é uma aplicação web de catálogo de livros, desenvolvida em C# com ASP.NET Core MVC (net10.0). Ele permite aos usuários visualizar uma vitrine de obras clássicas, ver detalhes dos livros e pesquisar na coleção.

## Funcionalidades Principais

* **Vitrine de Clássicos:** Um carrossel interativo e um grid expansível de obras clássicas, com capas dinâmicas baseadas em cores sólidas.
* **Sistema SPA-Like:** A navegação entre as visualizações de catálogo, livro e autor é aprimorada por meio da transferência de dados em `localStorage`, proporcionando uma experiência de carregamento mais rápida sem sobrecarga no servidor.
* **Barra de Pesquisa:** Permite filtrar livros instantaneamente por título, autor ou gênero usando o evento `oninput`.
* **Sistema de Favoritos:** Os usuários podem adicionar e remover livros dos seus favoritos. O estado dos favoritos é mantido localmente usando `localStorage` sob a chave `bibliotecaFavoritos`.
* **Páginas Genéricas e Dinâmicas:** As páginas de "Detalhes da Obra" e "Perfil do Autor" são populadas dinamicamente via JavaScript com base nas seleções no catálogo.

## Requisitos

* .NET 10 SDK
* MySql Server (ex: versão 8.0.40) - Gerenciado via Pomelo.EntityFrameworkCore.MySql 9.0.0.

## Como Executar o Projeto ASP.NET Core

1. Clone o repositório.
2. Defina as configurações de banco de dados no seu ambiente (ex: `ConnectionStrings__DefaultConnection`). Nunca armazene as credenciais sensíveis diretamente no `appsettings.json`.
3. Garanta que a porta `5239` esteja livre. Se estiver em uso, você pode matar o processo em sistemas Unix usando: `kill $(lsof -t -i :5239)`.
4. Compile e execute a aplicação (recomenda-se rodar em background caso sofra de timeouts no ambiente de desenvolvimento):
   ```bash
   dotnet build
   dotnet run > dotnet_run.log 2>&1 &
   ```
5. Acesse a aplicação localmente: `http://localhost:5239`.

## Como Explorar o Protótipo WEB3

Dentro da pasta `/WEB3/` encontra-se um protótipo puro em HTML/CSS/JS das telas do sistema.
Isto é útil para testes de UI e design rápidos sem a necessidade de compilar o back-end ASP.NET Core.

Para ver o protótipo, você pode abrir os arquivos HTML (como `WEB3/Livro/index.html` ou `WEB3/Autor/index.html`) diretamente no seu navegador, ou usar uma ferramenta simples de live server.

*Nota:* O sistema de favoritos e os metadados dinâmicos também funcionam nesta versão baseados no `localStorage` do navegador.

## Notas de Desenvolvimento e Segurança

* O projeto restringe o `AllowedHosts` apenas para hostnames confiáveis.
* Não commite os diretórios `bin/` ou `obj/`.
* Certifique-se de preencher `ServerVersion` explicitamente em vez de usar auto-detect no `Program.cs`.