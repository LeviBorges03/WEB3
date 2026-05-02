# Biblioteca

Bem-vindo à Biblioteca! Este é um projeto desenvolvido em ASP.NET Core MVC projetado para fornecer um catálogo digital de livros de forma organizada e moderna.

## Arquitetura do Projeto

O sistema possui duas frentes principais:
* **Aplicação Principal (Raiz):** Construída com ASP.NET Core MVC (C#). Ela fornece as Views, Controllers e Models da nossa aplicação.
* **Protótipo Isolado (`WEB3/`):** Um diretório contendo uma representação estática da interface de usuário (HTML, CSS e JS puros). Isto serve como documentação viva da UI e base para as views da aplicação principal. Sempre que realizar alterações de layout ou design, você também deve atualizar este protótipo.

## Funcionalidades Principais

* **Navegação Estilo SPA:** O projeto utiliza `localStorage` e JavaScript para transferir dados entre as páginas (como dados do livro ou do autor em foco), proporcionando uma navegação fluida sem exigir carregamentos completos constantes ou passar muitos dados pelas rotas.
* **Filtro de Pesquisa em Tempo Real:** O catálogo (`Index`) possui uma barra de pesquisa dinâmica que utiliza o evento de `oninput` do JavaScript, filtrando a exibição das obras de forma imediata à medida que o usuário digita.
* **Sistema de Favoritos:** Os usuários podem marcar livros como favoritos a partir da página de detalhes do livro. Essa informação é armazenada via `localStorage` no array `bibliotecaFavoritos`, permitindo persistir as seleções do usuário localmente no navegador.

## Como Executar Localmente

**Pré-requisitos:**
* .NET SDK (Versão 10.0 ou compatível) configurado no seu ambiente.
* Banco de dados MySQL (opcional para visualização do catálogo que utiliza dados na memória da Controller, mas necessário caso utilize o contexto completo).

**Passos:**
1. Clone este repositório para o seu ambiente local.
2. Navegue até o diretório raiz do projeto onde se encontra o arquivo `Biblioteca.csproj`.
3. Certifique-se de não bloquear a porta usada (ex: 5239).
4. Para executar, rode o comando:
   ```bash
   dotnet run
   ```
5. Acesse `http://localhost:5239` no seu navegador para utilizar o sistema.

**Nota:** As capas dos livros não utilizam imagens para fins de simplificação, mas sim cores sólidas hexadecimais associadas à temática da obra.
