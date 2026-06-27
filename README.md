# Biblioteca Digital (.NET Core MVC)

Bem-vindo à Biblioteca Digital, uma aplicação web baseada em ASP.NET Core MVC (Target .NET 10.0) que atua como uma vitrine para clássicos da literatura.

## Arquitetura e Decisões de Design
Este projeto segue uma abordagem híbrida:
- **Backend:** C# MVC para roteamento e injeção do modelo de dados (`Livro`). Os dados são mantidos em uma lista estática no `BibliotecaController` por questões de performance e simplicidade (sem dependência de banco de dados).
- **Frontend SPA-like:** Para manter a fluidez de navegação sem recarregar a página a cada ação, utilizamos extensamente o `localStorage` do navegador para transferir o contexto (como Livro Atual, Autor Atual e a lista de Favoritos).
- **Estilização:** CSS puro (`biblioteca.css`), focado em uma interface moderna, relaxante e responsiva.

## Novas Funcionalidades
- **Barra de Pesquisa:** Permite filtrar instantaneamente os livros da página inicial por Título ou Autor, manipulando o DOM em tempo real via JavaScript.
- **Sistema de Favoritos:** Os usuários podem favoritar obras usando a estrela nos cards da Home ou o botão na página de Detalhes do Livro. A lista de obras favoritas é persistida no `localStorage` do navegador.

## Como Executar

1. Tenha o .NET SDK 10.0 instalado.
2. Clone o repositório e acesse a pasta raiz do projeto.
3. Restaure as dependências e compile o projeto (se necessário):
   ```bash
   dotnet build
   ```
4. Execute o projeto na porta padrão:
   ```bash
   dotnet run
   ```
5. Acesse `http://localhost:5239` no seu navegador.
