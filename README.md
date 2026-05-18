# Biblioteca - Catálogo Clássico

Este é um projeto **ASP.NET Core MVC** que simula uma vitrine ou catálogo de biblioteca de livros clássicos. O aplicativo demonstra como integrar funcionalidades modernas de forma fluída e reativa usando tecnologias web padrão e o framework .NET.

## Arquitetura do Projeto

*   **ASP.NET Core MVC**: Utilizado para roteamento, estruturação de models e controllers e injeção de dependências. O aplicativo **não utiliza** banco de dados ou Entity Framework. Todos os modelos de dados e informações dos livros estão hardcoded nas `Controllers`.
*   **Single-Page Application (SPA) Like Experience**: Embora seja um MVC tradicional, o projeto utiliza transferências de dados via **`localStorage`** do navegador e chamadas JavaScript nativas para navegar fluidamente do catálogo geral para páginas de detalhes de livros ou autores sem recarregar e buscar dados do servidor desnecessariamente.

## Funcionalidades

*   **Catálogo Responsivo**: Uma interface moderna com carrossel para exibir os livros disponíveis e navegação simplificada.
*   **Barra de Pesquisa**: Uma barra de pesquisa rápida (que reage a eventos `oninput`) que permite a busca instantânea de livros por *título, autor ou gênero* sem requisições adicionais ao servidor.
*   **Sistema de Favoritos**: Permite que usuários "favoritem" livros, que são armazenados de forma persistente através do estado do navegador (`localStorage` na chave `bibliotecaFavoritos`), adaptando os botões da UI automaticamente caso a obra já seja um favorito.
*   **Perfil do Autor e Obra**: Visualização de perfis detalhados dinâmicos baseados no contexto salvo da página principal.

## Execução Local

Para executar o projeto localmente:

1.  Clone o repositório.
2.  No diretório raiz do projeto, certifique-se de que tem o .NET SDK 10 instalado e execute:

```bash
dotnet build
```

3. E então para iniciar a aplicação na porta localhost disponível (como `http://localhost:5239`):

```bash
dotnet run
```

---

## Prototipação UI (Pasta `WEB3`)

A raiz do projeto conta com uma pasta separada chamada `WEB3/`. Ela foi usada para a **prototipação visual inicial estática** da aplicação sem a necessidade do backend .NET.
Se você precisa realizar mudanças e testar variações de interface e estilos brutos (CSS puro, JS puro, HTML), pode fazer nessa pasta antes de migrar os códigos para as views `.cshtml` em `Views/Biblioteca`. Note que deve-se manter a consistência entre o que é feito lá e no projeto real.