# Biblioteca de Clássicos

Um projeto ASP.NET Core MVC (C#) voltado para organizar, visualizar e favoritar livros clássicos. O projeto não utiliza banco de dados e concentra seus dados e lógicas principais na própria controller e gerenciamento de estado no lado do cliente (`localStorage`).

## Funcionalidades
* **Catálogo Moderno**: Exibição em carrossel horizontal de dezenas de obras literárias.
* **Barra de Pesquisa Real-time**: Filtre por título, autor ou gênero instantaneamente.
* **Sistema SPA-like (Single Page Application)**: Navegação ágil usando `localStorage` para transferir estados entre visualizações sem a necessidade de recarregar dados do servidor.
* **Sistema de Favoritos**: Salve suas obras prediletas localmente no navegador (`localStorage`), persistindo-as em sessões futuras.

## Tecnologias e Arquitetura
* **Backend**: ASP.NET Core MVC (.NET 10.0), C#
* **Frontend**: HTML5, CSS3, JavaScript puro
* **Armazenamento**: Hardcoded no C# (`Controllers/BibliotecaController.cs`) e `localStorage` no frontend. Nenhuma dependência do Entity Framework.

## Como rodar o projeto localmente
1. Certifique-se de possuir o .NET 10.0 SDK instalado.
2. Na raiz do projeto, execute o comando para construir e inicializar a aplicação:
   ```bash
   dotnet run
   ```
3. O servidor subirá e poderá ser acessado pelo navegador, geralmente no endereço `http://localhost:5239`.

---
*Para ver uma representação estática e isolada da UI (Prototipação), confira o diretório `WEB3/`.*