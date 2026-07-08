# Biblioteca (ASP.NET Core MVC)

Este é um projeto de Biblioteca Clássica utilizando ASP.NET Core MVC. Ele foi construído focado em demonstrar o padrão MVC sem o uso do Entity Framework para acesso a banco de dados. Em vez disso, os dados são gerenciados em memória no controller (hardcoded list) para simplicidade e performance na listagem de dados.

## Funcionalidades e Arquitetura

* **ASP.NET Core MVC**: Estruturação completa em MVC.
* **SPA-like Navigation**: A navegação entre a listagem de livros, os detalhes do livro e os detalhes do autor é feita passando o estado através do `localStorage` via JavaScript em vez de múltiplas requisições ao backend.
* **Pesquisa Dinâmica**: Barra de pesquisa para filtrar os livros em tempo real no cliente ignorando acentos (buscando atributos `data-titulo`).
* **Sistema de Favoritos**: Permite favoritar livros. A lista de favoritos é salva localmente usando `localStorage` e é representada visualmente por estrelas amarelas (⭐) no catálogo principal e com o botão na tela de detalhes.

## Pré-requisitos

* [.NET SDK 10.0](https://dotnet.microsoft.com/download) instalado.

## Como Executar o Projeto Principal (ASP.NET Core)

1. Restaure e compile as dependências:
   ```bash
   dotnet build
   ```

2. Execute o servidor de desenvolvimento:
   ```bash
   dotnet run
   ```

3. Acesse a aplicação no seu navegador: `http://localhost:5239` (ou a porta informada no console).

## Protótipos Estáticos (WEB3)

A pasta `WEB3` contém uma versão estática (HTML/CSS/JS isolada do ASP.NET) utilizada apenas para prototipagem de interface e verificação visual isolada das telas (Catálogo, Autor, Livro). Para rodar esses arquivos para fins de desenvolvimento de front-end:

Entre no diretório `WEB3` e utilize o Python (ou semelhante) para servir:

```bash
cd WEB3
python3 -m http.server 8000
```
Em seguida, acesse no navegador: `http://localhost:8000`.