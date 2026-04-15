# Sistema de Biblioteca

Este é um projeto de um sistema de Biblioteca Digital construído com **ASP.NET Core MVC** (.NET 10). O sistema oferece um catálogo curado de obras literárias clássicas com navegação moderna e interativa estilo SPA (Single Page Application) e persistência no lado do cliente.

## Funcionalidades e Características

- **Catálogo Interativo:** Exibição de livros em formato carrossel, com possibilidade de expandir a visualização para ver todas as obras usando CSS Grid e flexbox.
- **Navegação SPA-Like:** Utiliza `localStorage` e JavaScript (via transferências de estado em `window.location`) para transições fluidas entre as páginas do Catálogo, Detalhes do Livro e Perfil do Autor, reduzindo dependências de back-end desnecessárias para dados simples.
- **Barra de Pesquisa em Tempo Real:** Permite aos usuários pesquisar livros rapidamente por Título, Autor ou Gênero. A pesquisa reage no evento `oninput` do DOM, garantindo filtragem imediata inclusive em ações de "colar" ou testes automatizados.
- **Sistema de Favoritos:** Os usuários podem marcar livros como favoritos na página de detalhes da obra. Na página inicial, um botão de filtro exclusivo exibe apenas os livros adicionados aos favoritos. Esses dados são salvos de forma persistente utilizando o `localStorage` do navegador.
- **Design Moderno:** Interface de usuário fluida e relaxante com animações CSS, botões elegantes e sem uso de arquivos de imagens (capas são renderizadas via CSS `background-color` utilizando cores do tema salvas no banco de dados).
- **Gerenciamento de Banco de Dados Otimizado:** Implementação baseada em `Pomelo.EntityFrameworkCore.MySql` (v9.0.0), otimizado no controlador com `IReadOnlyList` e instanciações estáticas para evitar pressão excessiva no Garbage Collector.

## Pré-Requisitos

- .NET 10 SDK
- MySQL Server (versão 8.0.40 recomendada)

## Instruções de Configuração e Execução

1. **Configuração do Banco de Dados:**
   - As credenciais de banco de dados sensíveis (UID/PWD) **não** devem ser gravadas diretamente no `appsettings.json` ou `appsettings.Development.json`.
   - Crie uma variável de ambiente na sua máquina chamada `ConnectionStrings__DefaultConnection` contendo a sua string de conexão MySQL (Ex: `Server=localhost;Database=biblioteca_db;Uid=seu_usuario;Pwd=sua_senha;`).
   - Se o projeto for recriado a partir do zero, certifique-se de que o provedor `Pomelo` no arquivo `Program.cs` especifica corretamente a versão explícita do MySQL (ex: `new MySqlServerVersion(new Version(8, 0, 40))`).
   - Lembre-se de restringir as configurações de `AllowedHosts` no seu `appsettings.json` de produção para prevenir falhas de segurança (HTTP Host header attacks).

2. **Compilar e Rodar o Projeto:**
   Abra o terminal no diretório raiz do projeto e execute:
   ```bash
   dotnet build
   dotnet run
   ```

3. **Ambiente de Desenvolvimento:**
   O aplicativo estará disponível (por padrão no desenvolvimento) no endereço:
   - `http://localhost:5239`

## Organização do Repositório

O repositório contém a versão principal do ASP.NET Core e pastas secundárias:
- `BibliotecaV2/` (quando presente): Representa um espelho do projeto raiz. Mudanças de configuração em `appsettings.json` devem ser refletidas aqui para sincronia.
- `WEB3/`: Contém arquivos vitrines puramente estáticos e documentação auxiliar (`WEB3/README.md`) para propósitos de portfólio.
