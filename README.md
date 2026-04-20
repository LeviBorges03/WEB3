# Biblioteca - Catálogo Digital de Clássicos

Uma aplicação web em ASP.NET Core MVC projetada para navegar em um catálogo de obras clássicas da literatura.

## Como Rodar o Projeto (Ambiente de Desenvolvimento)
Para compilar e iniciar o servidor de desenvolvimento, execute:
```bash
dotnet build
dotnet run
```
O servidor será inicializado localmente (ex: http://localhost:5239) para testes e verificação da UI.

## Sobre a Arquitetura (SPA-like)
A aplicação utiliza renderização server-side parcial com forte apoio de JavaScript do lado do cliente para prover navegação SPA-like (Single Page Application):
- Transferência de Estado: Os dados de Livros e Autores são trafegados entre as Views `Index`, `Livro` e `Autor` utilizando `localStorage`.
- Sistema de Favoritos: Os usuários podem favoritar/desfavoritar livros. Os dados são persistidos no navegador pela chave `bibliotecaFavoritos`.
- Busca Dinâmica: A tela principal (Index) possui uma barra de busca otimizada (`oninput`) capaz de filtrar livros sem refresh da página, utilizando propriedades como título, autor, e gênero, além de permitir visualização isolada das obras favoritas.

## Design e UI
A interface é baseada em práticas modernas com cantos arredondados, flexbox e transitions em CSS, oferecendo uma experiência focada na leitura e descoberta. Imagens não são utilizadas para as capas dos livros; os fundos dinâmicos são baseados na cor da temática de cada obra (Hex Colors gravados no Banco de Dados/Model).

## Pasta `WEB3/`
Dentro do repositório, existe uma subpasta chamada `WEB3/` que contém a prototipagem pura em HTML, CSS e JS (sem ASP.NET Core). Esta pasta é focada em experimentações isoladas de design e de navegação de elementos. Deve sempre se manter síncrona com os princípios de UI presentes na aplicação final.