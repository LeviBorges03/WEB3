# Biblioteca Web - Catálogo de Clássicos

Uma aplicação web moderna desenvolvida em ASP.NET Core MVC (C#) e .NET 10.0 para gerenciar e explorar um catálogo de livros clássicos. O projeto destaca-se por utilizar o padrão de design MVC no backend aliado a um forte uso de JavaScript no frontend, simulando uma Single Page Application (SPA) através do uso do `localStorage` para navegação e estado de sessão.

## Visão Geral do Projeto

A Biblioteca Web serve como um acervo digital para visualizar obras clássicas da literatura. Além de listar livros, a aplicação foca na experiência do usuário (UX), oferecendo:
- **Catálogo Dinâmico:** Uma grade em carrossel elegante que pode ser expandida para exibir toda a coleção de obras.
- **Sistema de Pesquisa e Filtros:** Pesquisa rápida de títulos, autores ou gêneros diretamente do catálogo, com respostas em tempo real.
- **Sistema de Favoritos:** Os usuários podem favoritar suas obras preferidas, persistidas usando `localStorage`. O catálogo inclui um filtro rápido para ver as obras favoritas.
- **Design SPA-like:** Ao clicar em um livro ou em um autor, os detalhes são visualizados sem a necessidade de múltiplas chamadas ao banco de dados; as informações trafegam agilmente por meio de `localStorage` para a view genérica (`Livro` e `Autor`).

## Tecnologias e Arquitetura

- **Backend:** C# com ASP.NET Core MVC.
- **Framework:** .NET 10.0.
- **Banco de Dados (Quando em uso):** Pomelo.EntityFrameworkCore.MySql (Versão 9.0.0). *Nota: Para garantir inicialização correta, o MySQL server version deve ser definido explicitamente, não usando AutoDetect.*
- **Frontend:** HTML5, CSS3, JavaScript puro.
- **Gerenciamento de Estado de UI:** `localStorage` (para simular SPA).
- **Design:** Responsivo, fluido e relaxante, focado na leitura clara e transições modernas com elementos CSS como pill-shaped buttons e variáveis globais CSS.

## Funcionalidades Chave

1. **Catálogo de Obras (Home):** O arquivo `Index.cshtml` atua como o ponto central, listando dezenas de clássicos pré-carregados (mockados via lista no Controller).
2. **Sistema de Favoritos:** O arquivo `Livro.cshtml` possui a lógica de "Adicionar/Remover dos Favoritos", e a tela Home (Index) possui a opção "Mostrar Favoritos".
3. **Barra de Pesquisa:** Presente na tela inicial, filtrando os cards com a mesma experiência de um app front-end moderno.

## Como Executar o Projeto Localmente

1. Tenha o [.NET 10.0 SDK](https://dotnet.microsoft.com/download) instalado.
2. Clone o repositório ou baixe os arquivos fonte.
3. Abra a pasta raiz em um terminal.
4. Execute o comando de compilação:
   ```bash
   dotnet build
   ```
5. Rode o projeto:
   ```bash
   dotnet run
   ```
6. O terminal indicará o link local (ex: `http://localhost:5000` ou `https://localhost:5001`). Acesse pelo seu navegador de preferência.

---
**Dica de Manutenção:** Ao editar ou adicionar novos recursos visuais, mantenha os estilos das animações e cores em `wwwroot/css/biblioteca.css`. Sempre prefira modificar o código existente para criar novos recursos do que reconstruir ou alterar as rotas do Controller atual.
