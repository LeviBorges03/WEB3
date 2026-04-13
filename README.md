# Biblioteca V2

Bem-vindo à Biblioteca V2! Este é um sistema moderno de catálogo de livros construído com ASP.NET Core MVC e práticas de frontend fluidas simulando uma SPA (Single Page Application).

## Funcionalidades Principais

- **Catálogo de Clássicos:** Uma vitrine elegante de obras literárias usando um design em grade responsivo que pode ser navegado horizontalmente ou expandido para visualização completa.
- **Barra de Pesquisa em Tempo Real:** Permite aos usuários filtrar rapidamente os livros por título, autor ou gênero sem recarregar a página (implementado com `oninput`).
- **Navegação Estilo SPA:** A transição entre o Catálogo, Detalhes do Livro e Perfil do Autor é feita transferindo o estado dos dados em JavaScript através da API `localStorage`, permitindo uma navegação rápida sem carregar grandes cargas do servidor de cada vez.
- **Sistema de Favoritos (Local):** Na página de Detalhes do Livro, os usuários podem salvar ou remover obras de sua lista de favoritos, cujos dados são mantidos e lidos dinamicamente usando o `localStorage`.

## Detalhes Técnicos e Arquitetura

- **Backend:** C# / .NET 10.0 com ASP.NET Core MVC.
- **Banco de Dados (Configuração):** O sistema foi projetado para se integrar ao MySQL através do Pomelo EntityFrameworkCore (versão 9.0.0). Notavelmente, utilizamos um servidor com versão explícita (`new MySqlServerVersion(new Version(8, 0, 40))`) no `Program.cs` para acelerar a inicialização. As informações sensíveis de conexão devem ser mantidas em variáveis de ambiente (`ConnectionStrings__DefaultConnection`).
- **Controladores (Otimização):** Dados estáticos em memória foram alocados em campos `private static readonly` (por exemplo, na `BibliotecaController`) para minimizar o esforço do Garbage Collector durante cada requisição de página.

## Frontend UI e UX

A interface é construída sobre um tema relaxante e moderno:
- Animações suaves em hover (elevações, transições de cor).
- O sistema visual prioriza cores hexadecimais sólidas em vez de imagens pesadas para manter a aplicação veloz.
- O Javascript interage diretamente alterando `style.display = 'flex'` e `none` no DOM, aderindo às melhores práticas de compatibilidade ao usar Flexbox.

## Como Executar

1. Tenha o .NET 10 SDK instalado.
2. Clone o repositório e navegue até o diretório raiz.
3. Se estiver usando banco de dados em um ambiente local, defina suas variáveis de ambiente ou arquivo `appsettings.json`.
4. Execute `dotnet build` seguido de `dotnet run`. O sistema rodará localmente (geralmente na porta 5239).
