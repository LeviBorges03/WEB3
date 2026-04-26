# Sistema de Biblioteca

Este projeto é um sistema de catálogo de biblioteca digital com uma interface moderna e rápida (Single Page Application - SPA Like), focado em proporcionar uma excelente experiência de usuário com transições suaves e recursos de pesquisa e favoritos.

## Arquitetura

O sistema é construído sobre duas bases complementares:

1.  **ASP.NET Core MVC (Backend e Visualização Dinâmica):**
    A raiz do projeto abriga um aplicativo ASP.NET Core MVC escrito em C#. Ele gerencia o catálogo de livros, ordenando-os pela data de publicação, e lida com o roteamento. O projeto visa o framework .NET 10.0.

2.  **WEB3 (Prototipagem Estática Front-end):**
    O diretório `WEB3/` contém representações estáticas puras em HTML, CSS e JavaScript da interface do usuário. Essa arquitetura paralela permite prototipagem visual isolada e testes de UI sem a necessidade de rodar o servidor ASP.NET completo. Qualquer alteração de design deve ser refletida tanto no `.cshtml` do ASP.NET quanto no `.html` do `WEB3/` para garantir consistência.

## Funcionalidades Principais

*   **Catálogo Dinâmico:** Exibe livros em um formato de carrossel com rolagem horizontal suave, com a capacidade de expandir para visualizar todas as obras de uma vez.
*   **Pesquisa em Tempo Real:** Uma barra de pesquisa no topo do catálogo permite aos usuários filtrar livros instantaneamente por título, autor ou gênero. A pesquisa é ativada através do evento `oninput` para garantir captura de colagem e respostas rápidas.
*   **Sistema de Favoritos SPA:** Os usuários podem favoritar obras diretamente na página de Detalhes do Livro. Este sistema não requer recarregamento da página e persiste os favoritos no `localStorage` do navegador sob a chave `bibliotecaFavoritos`.
*   **Navegação Fluida:** O uso inteligente de transferência de dados por JavaScript e `localStorage` imita a navegação de uma SPA, enviando os dados do livro/autor selecionados entre as visualizações genéricas (Index -> Livro, Index -> Autor).
*   **Cores Temáticas:** As capas dos livros utilizam cores sólidas hexadecimais correspondentes ao tema do livro em vez de carregar imagens pesadas, aprimorando a performance.

## Requisitos

*   .NET 10.0 SDK
*   Banco de Dados MySQL (Se utilizado pelo Entity Framework, atualmente as obras estão mockadas na memória do Controller). O projeto é configurado com `Pomelo.EntityFrameworkCore.MySql`.

## Configuração e Execução

### Configuração de Segurança
As credenciais do banco de dados (como UID e PWD) nunca devem ser gravadas no `appsettings.json`. O sistema deve usar variáveis de ambiente em produção para fornecer a `ConnectionStrings__DefaultConnection`.
No `appsettings.json`, a propriedade `AllowedHosts` deve ser estritamente configurada para hosts confiáveis (ex: `localhost`) para prevenir ataques ao cabeçalho Host.

### Como Rodar Localmente (ASP.NET)

1. Restaure as dependências e compile o projeto:
   ```bash
   dotnet build
   ```
2. Execute o servidor de desenvolvimento:
   ```bash
   dotnet run
   ```
   *Nota: O servidor padrão rodará na porta 5239 (`http://localhost:5239`). Se a porta estiver em uso, utilize o comando `kill $(lsof -t -i :5239)` antes de rodar novamente.*
   *Em ambientes de desenvolvimento propensos a timeout, recomenda-se rodar o processo em background:* `dotnet run > dotnet_run.log 2>&1 &`

### Como Rodar Localmente (Protótipo WEB3)
Para verificar o design isoladamente, simplesmente abra o arquivo `WEB3/index.html` ou inicie um servidor HTTP simples no diretório `WEB3/` (ex: `python -m http.server 8000`).

## Boas Práticas Adotadas

*   **Desempenho no Controller:** Dados estáticos no Controller são declarados usando `private static readonly` para diminuir a pressão da Coleta de Lixo (GC).
*   **CSS Flexbox:** A filtragem manipula a visibilidade trocando `display` para `flex` (ou `none`), garantindo que o layout dos cartões continue intacto.
*   **Conexão Segura:** Ao configurar a inicialização do MySQL no `Program.cs`, sempre evite usar `ServerVersion.AutoDetect`, fornecendo explicitamente uma versão válida.
