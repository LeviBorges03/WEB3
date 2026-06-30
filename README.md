# Biblioteca Digital - ASP.NET Core MVC

Este projeto é uma **Biblioteca Digital** focada em apresentar um catálogo de clássicos da literatura. Construído usando o padrão arquitetural MVC (Model-View-Controller) na plataforma ASP.NET Core (.NET 10.0), o sistema simula uma Single Page Application (SPA) utilizando recursos nativos do HTML5 e JavaScript.

## 🚀 Funcionalidades Principais

* **Catálogo de Clássicos:** Um carrossel interativo exibindo vários livros clássicos.
* **Sistema de Busca em Tempo Real:** Permite a filtragem de livros pelo título ou nome do autor de forma instantânea. A pesquisa ignora acentos (accent-agnostic) para proporcionar uma experiência de busca mais robusta.
* **Sistema de Favoritos:** O usuário pode favoritar e desfavoritar livros usando o ícone de estrela (⭐) diretamente nos cartões dos livros.
* **Páginas de Detalhes:** Navegação rápida para as páginas detalhadas do livro ou do autor sem a necessidade de recarregar dados a partir do servidor, garantindo máxima performance.

## 🏗️ Arquitetura e Gestão de Estado

Embora o projeto seja fundamentado no ASP.NET Core MVC para renderização inicial e organização das rotas, ele utiliza extensivamente o **Client-Side State Management** para simular uma SPA:
* Todos os dados iniciais são injetados pelo servidor nas views (`Index.cshtml`).
* A navegação entre o Catálogo, Livro e Autor ocorre repassando o contexto via `localStorage` (chaves `livroAtual`, `autorAtual` e `bibliotecaFavoritos`).
* Não há dependência de banco de dados nem do Entity Framework. A lista de modelos (`Livro`) fica _hardcoded_ de forma performática na camada `Controller`.

## 🛠️ Como Executar o Projeto Principal

1. Certifique-se de que possui o .NET SDK 10.0 instalado.
2. Abra um terminal na raiz do projeto.
3. Execute o comando de compilação para instalar dependências e compilar a aplicação:
   ```bash
   dotnet build
   ```
4. Em seguida, inicie o servidor de desenvolvimento:
   ```bash
   dotnet run
   ```
5. Acesse `http://localhost:5239` no seu navegador.

---
**Nota:** Caso ocorra um erro de "Address already in use", execute `kill $(lsof -t -i :5239)` e rode o `dotnet run` novamente.
