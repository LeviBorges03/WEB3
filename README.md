# Projeto Biblioteca Clássica (ASP.NET Core MVC)

Bem-vindo ao projeto Biblioteca Clássica, um sistema de catálogo digital construído com **ASP.NET Core MVC** (.NET 10). O sistema tem como objetivo exibir e organizar obras literárias clássicas de forma simples e intuitiva.

## Funcionalidades Implementadas

*   **Catálogo Digital**: Exibe uma vitrine dos grandes clássicos mundiais e nacionais com uma interface rica e responsiva.
*   **Barra de Pesquisa em Tempo Real**: Localizada na página principal (Catálogo), permite que o usuário filtre as obras pelo título do livro ou pelo nome do autor sem necessidade de recarregar a página (SPA-like experience).
*   **Sistema de Favoritos**: Permite que os usuários salvem seus livros preferidos ao clicar no botão "Adicionar aos Favoritos" na página de Detalhes do Livro. Essa informação é salva localmente no navegador (`localStorage`), garantindo que suas preferências persistam através das sessões do lado do cliente.
*   **Navegação Fluida (SPA-like)**: Utilização otimizada do JavaScript para transferir dados de navegação entre views sem chamadas redundantes ao backend (repassando estado pelo `localStorage`).

## Requisitos e Como Executar

*   **Tecnologia Backend**: C# com ASP.NET Core 10.
*   **Tecnologias Frontend**: HTML5, CSS3, JavaScript (Vanilla), jQuery, e Bootstrap.
*   **Banco de Dados**: O sistema está preparado para uso com MySQL (Pomelo EntityFrameworkCore).

### Para executar localmente:

1. Certifique-se de possuir o .NET SDK 10 instalado na máquina.
2. Abra seu terminal na pasta raiz do projeto.
3. Digite o seguinte comando:
   ```bash
   dotnet build
   dotnet run
   ```
4. O servidor iniciará. Acesse a aplicação pela URL fornecida no terminal (normalmente `http://localhost:5239`).
*(Se a porta 5239 estiver bloqueada, utilize `kill $(lsof -t -i :5239)` antes de rodar).*

## Arquitetura e Protótipos (Pasta `WEB3`)

O projeto conta com um diretório especial chamado `WEB3/`. Essa pasta **não** faz parte da lógica do backend ASP.NET Core MVC, mas atua como um laboratório isolado e puramente estático de prototipação da interface. Para mais detalhes sobre as regras de negócio da prototipação UI e CSS, consulte o documento específico `WEB3/README.md`.
