# Biblioteca - Projeto ASP.NET Core MVC

Este projeto é uma aplicação web de vitrine de biblioteca desenvolvida em ASP.NET Core MVC (C#). Ele permite que os usuários explorem um catálogo de livros clássicos, visualizem detalhes de obras e autores, realizem pesquisas em tempo real e gerenciem seus livros favoritos.

## Funcionalidades
* **Catálogo de Obras**: Uma lista de clássicos da literatura ordenados pela data de publicação.
* **Sistema de Busca Integrada**: Pesquisa instantânea por título ou autor usando JavaScript (sem recarregamento da página).
* **Meus Favoritos**: Permite ao usuário adicionar e remover livros da sua lista de favoritos, utilizando `localStorage` para manter o estado persistente no navegador do usuário.
* **Navegação Dinâmica (SPA-Like)**: Uso de transição de dados via JavaScript para não necessitar consultas redundantes ao servidor na visualização de detalhes.
* **Layout Moderno e Responsivo**: Design limpo e fluido adaptável a diversos tamanhos de tela.

## Tecnologias e Arquitetura
* **Framework**: .NET 10.0 (ASP.NET Core MVC).
* **Linguagem**: C#.
* **Banco de Dados**: Configurado para Entity Framework Core com MySQL (Pomelo.EntityFrameworkCore.MySql v9.0.0). *Atenção:* O servidor MySQL foi configurado com a versão explícita (`8.0.40`) no arquivo `Program.cs` para evitar bloqueios durante o startup da aplicação (substituindo o problemático `AutoDetect`).
* **Front-end**: HTML5, CSS3, JavaScript e Bootstrap.
* **Padrão de Projeto**: Arquitetura em camadas (Models, Views, Controllers) e padrão Repository (pronto para ser expandido).

## Como Executar o Projeto
1. Certifique-se de que o SDK do .NET 10.0 está instalado na sua máquina.
2. Abra o terminal na raiz do projeto.
3. Restaure as dependências e compile a aplicação:
   ```bash
   dotnet build
   ```
4. Inicie o servidor de desenvolvimento:
   ```bash
   dotnet run
   ```
5. Acesse no seu navegador o endereço padrão que aparecerá no terminal (geralmente `http://localhost:5000` ou `https://localhost:5001`).

## Destaques da Implementação
* **Search & Favorites UI**: As barras de pesquisa e o botão "Ver Meus Favoritos" no `Index.cshtml` utilizam as mesmas variáveis CSS globais de padronização visual, resultando em botões elegantes e em formato *pill*.
* **Sem imagens em disco**: Para manter a simplicidade, as capas dos livros utilizam cores sólidas em HEX baseadas no gênero e "clima" do livro. Isso garante rápido carregamento.
