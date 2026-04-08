# Biblioteca Digital Clássica

Bem-vindo à Biblioteca Digital Clássica, um acervo moderno de grandes obras da literatura.

Este projeto foi construído utilizando **ASP.NET Core MVC** (.NET 10.0) e demonstra a integração de uma arquitetura robusta no backend com interações dinâmicas ricas no frontend.

## 🌟 Funcionalidades

- **Catálogo Interativo:** Exibe uma vitrine dos livros com capas dinâmicas e design responsivo.
- **Navegação SPA-Like:** Utiliza JavaScript puro e `localStorage` para transições fluídas e instantâneas entre o Catálogo, Detalhes do Livro e o Perfil do Autor, sem a necessidade de recarregamentos completos da página.
- **Sistema de Pesquisa em Tempo Real:** Permite buscar obras no catálogo instantaneamente filtrando por *título, autor ou gênero* direto pelo DOM.
- **Sistema de Favoritos:** O usuário pode "Adicionar aos Favoritos" suas obras preferidas na página de Detalhes. As obras favoritas podem ser visualizadas isoladamente no catálogo clicando no botão "Ver Favoritos", proporcionando uma curadoria personalizada gerenciada via `localStorage`.

## 🛠 Arquitetura e Tecnologias

- **Backend:** C# / ASP.NET Core MVC (net10.0)
- **Frontend:** HTML5, CSS3, e JavaScript Vanilla para lógicas SPA e componentização via Razor Pages (`.cshtml`).
- **Banco de Dados (Configurado):** MySQL integrado utilizando o driver `Pomelo.EntityFrameworkCore.MySql` (versão 9.0.0). *As conexões do banco são gerenciadas exclusivamente via variáveis de ambiente (`ConnectionStrings__DefaultConnection`) para maior segurança.*

## 🚀 Performance e Práticas

- Listas de entidades fixas nos `Controllers` são otimizadas e implementadas como `private static readonly List<T>` para minimizar a pressão do Garbage Collector (GC) e alocações de Heap em múltiplas requisições.
- As consultas ao banco e regras de inicialização evitam detecção automática de versão do MySQL (utilizando uma versão explícita no instanciamento do `MySqlServerVersion` no `Program.cs`) para não bloquear a subida da aplicação.

## 🖥 Executando o Projeto

1. Clone o repositório.
2. Certifique-se de que o SDK .NET 10.0 está instalado na sua máquina.
3. No diretório principal, execute:
   ```bash
   dotnet build
   dotnet run
   ```
4. Acesse através do seu navegador no link disponibilizado no log do console (ex: `http://localhost:5000`).
