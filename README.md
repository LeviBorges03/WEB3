# Projeto Biblioteca

O Projeto Biblioteca é uma aplicação em **ASP.NET Core MVC** desenvolvida para apresentar um catálogo digital de livros clássicos. A aplicação foi pensada para oferecer uma experiência de "Single Page Application" (SPA) sem a necessidade de frameworks complexos de frontend, utilizando para isso o poder do **JavaScript Vanilla** e **localStorage** para passar os estados entre as views.

## 🚀 Tecnologias Utilizadas

- **Backend:** C# (.NET 10.0), ASP.NET Core MVC
- **Frontend:** HTML5, CSS3, JavaScript Vanilla (sem jQuery para o core da aplicação)
- **Armazenamento:** `localStorage` (Armazenamento de estado no lado do cliente: livro selecionado, autor e lista de favoritos)
- **Estilização:** CSS Customizado (CSS variables para temas, Flexbox e Grid)

## 🌟 Funcionalidades Principais

- **Catálogo de Clássicos:** Um carrossel interativo exibindo diversos livros clássicos ordenados por data de publicação.
- **Pesquisa Dinâmica:** Busca em tempo real de livros por título ou autor usando JS para filtrar os itens visíveis.
- **Sistema de Favoritos:** Um sistema mantido puramente por estado local, no qual os usuários podem favoritar (⭐) os livros direto pelo catálogo ou na página de detalhes da obra.
- **Visualização de Detalhes SPA-like:** Transferência fluída dos dados do livro ou do autor pela navegação sem necessidade de bancos de dados; a informação flui via cache local e DOM.
- **Design Limpo e Responsivo:** Baseado em princípios de UI/UX modernos com microinterações focadas.

## 💻 Como Executar o Projeto Localmente

### Pré-requisitos
- .NET SDK 10.0 ou superior
- Um navegador web moderno (Chrome, Edge, Firefox, etc.)

### Rodando o Servidor ASP.NET
1. Abra um terminal na raiz do projeto (onde está localizado o arquivo `Biblioteca.csproj`).
2. Construa e execute a aplicação usando a CLI do dotnet:
   ```bash
   dotnet build
   dotnet run
   ```
3. Acesse a aplicação no seu navegador pelo endereço local padrão, tipicamente: `http://localhost:5239` (ou o especificado em `Properties/launchSettings.json`).

*Nota: Se encontrar o erro de porta em uso ("Address already in use"), feche os processos ocupando a porta com:*
`kill $(lsof -t -i :5239)`

## 📁 Estrutura de Diretórios de Destaque

- `/Controllers`: Contém o `BibliotecaController.cs` que orquestra a lógica C# e alimenta a listagem estática do modelo.
- `/Views`:
  - `Biblioteca/Index.cshtml`: Página inicial (catálogo), implementa a UI e scripts da pesquisa e carrossel.
  - `Biblioteca/Livro.cshtml`: View de detalhes, resgata as informações armazenadas no `localStorage`.
- `/wwwroot/css`: Contém a biblioteca de estilos, destacando o `biblioteca.css`. Observe o arquivo `DescricaoEstilo.txt` para um guia de design system.
- `/WEB3`: Uma pasta contendo protótipos puramente estáticos e visuais (arquivos `HTML`/`CSS`/`JS` brutos). Usada para validação de layout antes de integração com o backend C#. (Ver `WEB3/README.md`)

## 🛡️ Segurança e Performance

- A aplicação não expõe rotas inseguras de banco de dados, visto que todos os modelos estão em memória ou client-side.
- Proteção XSS intrínseca pela utilização restrita de `.innerText` em inserção dinâmica de DOM.
- Arquitetura leve favorece baixa alocação de memória do lado do servidor.
