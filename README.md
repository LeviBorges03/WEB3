# Biblioteca Web MVC & WEB3 Prototypes

Este repositório contém a implementação final de uma Biblioteca baseada em C# ASP.NET Core MVC (na raiz) e um conjunto de protótipos de interface isolados localizados no diretório `WEB3/`.

## Funcionalidades e Arquitetura SPA-Like
O sistema de Biblioteca não utiliza bancos de dados no backend, mas tira proveito de tecnologias do lado do cliente (`localStorage`) para gerenciar estado, simulando um comportamento Single Page Application (SPA):

- **Navegação Dinâmica**: Ao clicar em um livro ou autor, a aplicação serializa os dados e os envia ao `localStorage` (nas chaves `livroAtual` e `autorAtual`). As views de Detalhes (`Livro.cshtml` e `Autor.cshtml`) recuperam e populam os dados na tela.
- **Barra de Pesquisa**: Uma barra de pesquisa na tela inicial (`Index.cshtml`) permite a filtragem de livros em tempo real. A implementação captura o texto inserido, normaliza (remove acentos e ajusta as letras) e altera a visibilidade dos cartões (`display: flex` / `display: none`) buscando correspondência em título, autor ou gênero (usando HTML5 `data-*` attributes).
- **Sistema de Favoritos**: Você pode adicionar seus livros favoritos pela página principal (clicando no ícone de estrela dentro da capa do livro) ou pela tela de detalhes do livro. Esses favoritos também são persistidos no browser usando a chave `bibliotecaFavoritos`.

## Executando o Projeto Principal (ASP.NET Core)
A aplicação está configurada para .NET 10. Para executar a aplicação e visualizá-la:

1. Limpe / Restaure dependências:
   ```bash
   dotnet clean
   dotnet build
   ```
2. Inicie a aplicação (Recomenda-se rodar em background no ambiente isolado):
   ```bash
   dotnet run > dotnet_run.log 2>&1 &
   ```
3. A aplicação estará disponível localmente. Por padrão, a aplicação roda na porta `5239` (http://localhost:5239).
*Obs: Se você encontrar problemas de "porta em uso", você pode liberar a porta usando `kill $(lsof -t -i :5239)`.*

## Executando os Protótipos Estáticos (WEB3)
O diretório `WEB3/` serve os arquivos puramente estáticos criados para a prototipação. Você pode navegá-los lançando um servidor HTTP local:
```bash
cd WEB3
python3 -m http.server 8000
```
Em seguida, acesse os protótipos como http://localhost:8000/Livro/ e http://localhost:8000/Autor/
