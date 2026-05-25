# Biblioteca - Catálogo de Clássicos (ASP.NET Core MVC)

Este projeto é um catálogo digital de livros clássicos construído utilizando ASP.NET Core MVC e C#. Ele oferece uma interface moderna e agradável para explorar grandes obras da literatura.

## Funcionalidades Principais

- **Catálogo de Obras**: Explore uma lista de livros clássicos com capas coloridas e dinâmicas (utilizando cores hexadecimais), autores, gêneros e datas de publicação.
- **SPA-like Navigation**: A navegação entre as páginas do catálogo (Index), detalhes do livro (Livro) e perfil do autor (Autor) ocorre através da transferência de estado utilizando o `localStorage` do navegador. Isso reduz a necessidade de requisições pesadas ao servidor para consultar os mesmos dados, oferecendo uma experiência mais rápida.
- **Pesquisa em Tempo Real**: Na página inicial, você pode utilizar a barra de pesquisa para filtrar rapidamente o catálogo por título da obra ou nome do autor. A filtragem é executada no lado do cliente (`oninput`) para máxima performance, inclusive ao colar texto.
- **Sistema de Favoritos**: Na página de detalhes do livro, os usuários podem marcar suas obras preferidas clicando no botão "Adicionar aos Favoritos". Esta preferência é salva no `localStorage` (na chave `bibliotecaFavoritos`) como um array JSON com os títulos dos livros. O estado do botão é alterado dinamicamente para indicar se o livro está favoritado ou não.

## Como Executar o Projeto Localmente

**Pré-requisitos**: .NET SDK 10.0 ou superior.

1. Clone o repositório.
2. Na raiz do projeto, você pode compilar a aplicação com o comando:
   ```bash
   dotnet build --no-restore
   ```
3. Para iniciar o servidor de desenvolvimento, execute:
   ```bash
   dotnet run
   ```
4. Se houver problemas de porta em uso na porta `5239`, você pode terminá-la antes de executar o `dotnet run`:
   ```bash
   kill $(lsof -t -i :5239)
   ```
5. Acesse `http://localhost:5239` no seu navegador para visualizar a aplicação.

## Protótipos Estáticos (WEB3)

A pasta `WEB3` contém protótipos em HTML, CSS e JS puros. Eles representam versões estáticas das views e servem para fins de design e desenvolvimento do layout antes de serem integradas no ASP.NET.
Para servi-los localmente, navegue até a pasta `WEB3` e utilize o Python (se disponível):
```bash
cd WEB3
python3 -m http.server 8000
```
E acesse `http://localhost:8000`.