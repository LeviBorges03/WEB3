# Biblioteca de Clássicos

Um projeto ASP.NET Core MVC (net10.0) que implementa um catálogo digital de obras literárias clássicas, estruturado como um Single Page Application (SPA) em que o roteamento de dados visuais é resolvido inteiramente via frontend (`localStorage` e Javascript).

## Funcionalidades

- **Catálogo Vitrine**: Uma interface limpa, onde os livros são categorizados e navegáveis (com carrossel horizontal ou expandidos em grade).
- **SPA-like Data Transfer**: Os dados de obras selecionadas são armazenados no `localStorage` antes de invocar uma rota, e preenchidos em templates visuais genéricos sem necessidade de roundtrips adicionais ao backend.
- **Sistema de Favoritos**: Funcionalidade baseada no client-side (`localStorage` com a chave `bibliotecaFavoritos`) onde usuários podem "favoritar" títulos. Eles são visualizados como uma estrela amarela `⭐` e podem ser adicionados tanto no card principal como na visualização estendida da obra.
- **Busca Integrada**: Busca flexível para livros por título, autor e gênero, com o uso de `data-attributes` nos cards HTML. A funcionalidade usa o evento `oninput` para garantir que as buscas e eventuais colagens ocorram em tempo real.

## Arquitetura e Modelagem

- **Nenhum banco de dados configurado**: Não há uso de Entity Framework ou conexões ativas com DB. Toda a lista de obras encontra-se `hardcoded` diretamente no controller principal (`BibliotecaController.cs`) para fácil distribuição e execução.
- O arquivo `WEB3/` é uma pasta separada criada inicialmente para testes de Interface (UI) puramente estáticos.

## Como Executar (Ambiente de Desenvolvimento)

**1. Requisitos:**
- SDK .NET 10.0 (Instalado na máquina)

**2. Passos:**
1. Clone o repositório ou navegue até a pasta base (`/home/jules/workspace`).
2. Digite: `dotnet build`
3. Execute o servidor: `dotnet run`
4. A página deverá rodar localmente, tipicamente no endereço `http://localhost:5239`.

_Nota: Os scripts `dotnet` podem sofrer _timeouts_ e bloqueios. Ocasionalmente, portas presas devem ser mortas (`kill $(lsof -t -i :5239)`)._
