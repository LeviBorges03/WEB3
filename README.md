# Biblioteca Virtual (ASP.NET Core MVC)

Bem-vindo ao projeto da Biblioteca Virtual! Este sistema foi desenvolvido em ASP.NET Core MVC utilizando C# (no framework .NET 10.0), oferecendo uma experiência de catálogo de clássicos da literatura moderna.

## Arquitetura e Funcionalidades
* **Catálogo Moderno**: Interface em carrossel e exibição em grade inspirada no conceito SPA (Single Page Application), com transições e filtragem em tempo real utilizando JavaScript (vanilla) e manipulação do DOM (`oninput`).
* **Visualização Fluida**: A passagem de dados entre o catálogo (`Index`), a página do livro (`Livro`) e do autor (`Autor`) ocorre via `localStorage`, proporcionando tempos de resposta instantâneos sem recarregamento completo (server-side rendering das propriedades).
* **Sistema de Favoritos**: Os usuários podem favoritar livros na página de detalhes, cujo estado é armazenado e persistido utilizando `localStorage` com a chave `bibliotecaFavoritos`.
* **Banco de Dados (MySQL)**: Integrado com Entity Framework Core (`Pomelo.EntityFrameworkCore.MySql` versão 9.0.0). _Nota: Variáveis de ambiente (`ConnectionStrings__DefaultConnection`) são usadas para evitar a exposição de credenciais no `appsettings.json`._

## Como Executar o Projeto Localmente

1. Certifique-se de ter o [.NET SDK 10.0](https://dotnet.microsoft.com/download) instalado.
2. Clone o repositório e navegue até a pasta raiz.
3. Restaure e compile o projeto:
   ```bash
   dotnet build
   ```
4. Execute o servidor de desenvolvimento:
   ```bash
   dotnet run
   ```
5. Acesse `http://localhost:5239` no seu navegador.
   _Dica: Se encontrar erro de "Address already in use", utilize `kill $(lsof -t -i :5239)` (Linux/Mac) para liberar a porta antes de executar novamente._

## Repositório WEB3 (Prototipação)
Na pasta `/WEB3` você encontrará uma versão puramente estática (HTML/CSS/JS) da interface do usuário. Estes arquivos servem como protótipos de design e interações, independentes do ambiente .NET. Manter atualizações paralelas em ambas as estruturas é recomendado ao alterar estilos e lógica de frontend básica.
