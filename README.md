# Projeto Biblioteca

Bem-vindo ao projeto Biblioteca! Este é um sistema moderno de catálogo de livros digitais desenvolvido em **ASP.NET Core MVC** utilizando C# (net10.0) e Entity Framework Core para a conexão com o banco de dados MySQL.

## Arquitetura e Estrutura

- **Frontend e UX**: A interface do usuário prioriza a fluidez, implementando navegação estilo SPA (Single Page Application) e gerenciamento de estado no lado do cliente usando JavaScript e `localStorage`. Isso permite a atualização de componentes da interface sem recarregamentos totais da página.
- **Backend**: C# em ASP.NET Core MVC que serve as Views (`.cshtml`) conectadas a um banco de dados MySQL via Pomelo.EntityFrameworkCore.MySql.

## Funcionalidades Principais

1. **Catálogo de Clássicos (Home)**: Um carrossel interativo exibindo todas as obras da biblioteca. Possui um sistema de **Pesquisa em Tempo Real** implementado através do evento `oninput`, permitindo filtrar rapidamente os livros pelo título ou autor, além de possuir rolagem lateral suave.
2. **Sistema de Favoritos**: Os usuários podem favoritar suas obras preferidas diretamente na página de detalhes do livro. Este sistema usa o `localStorage` do navegador com a chave `bibliotecaFavoritos` para salvar os títulos de forma persistente no dispositivo sem depender de autenticação do backend.
3. **Navegação de Autores e Detalhes de Livros**: O estado das seleções de visualização é transferido de forma otimizada via armazenamento no cliente.
4. **Design Moderno**: As páginas compartilham uma identidade visual relaxante, utilizando componentes elegantes como botões arredondados (pill-shaped) e animações suaves, centralizadas no arquivo principal `wwwroot/css/biblioteca.css`.

## Desenvolvimento e Boas Práticas

- As informações sensíveis do banco de dados (UID/PWD) devem ser mantidas seguras via variáveis de ambiente (`ConnectionStrings__DefaultConnection`) e nunca no `appsettings.json`.
- Restringimos fortemente a configuração de domínios em `AllowedHosts` apenas para os confiáveis, evitando vulnerabilidades de segurança (ex: wildcard *).
- O projeto contém uma pasta especial `WEB3/` que serve como ambiente estático para design isolado das páginas da Biblioteca. Quaisquer melhorias e refatorações no sistema de UI e documentação devem considerar a compatibilidade e a sincronização com este ambiente isolado para o design.
- Ao testar e iniciar o servidor de desenvolvimento, utilize o comando `dotnet run`. A porta de desenvolvimento local geralmente é configurada em `http://localhost:5239`.

---

*Nota do Desenvolvedor: Favor não commitar diretórios compilados (`bin/` ou `obj/`). Siga sempre as configurações presentes no `.gitignore` e verifique seu código antes da submissão para evitar o bloqueio de CI/CD e aprovações de Pull Request.*