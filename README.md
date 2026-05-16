# Biblioteca Digital Clássica

Bem-vindo ao projeto **Biblioteca Digital Clássica**, um catálogo elegante e moderno de grandes obras literárias. Esta aplicação foi projetada para demonstrar boas práticas de desenvolvimento web moderno usando a stack .NET em conjunto com funcionalidades SPA (Single Page Application) sem recarregamento completo da página, impulsionado por JavaScript no lado do cliente.

## 🚀 Tecnologias Utilizadas

- **Backend:** C# / ASP.NET Core MVC (net10.0)
- **Frontend:** HTML5, CSS3, JavaScript Vanilla
- **Persistência Temporária:** API `localStorage` no lado do cliente
- **Design System:** Design fluído, usando variáveis CSS (`--primary`, `--accent`), flexbox e grids.

## 🌟 Funcionalidades

- **Catálogo de Obras:** Uma vitrine contendo uma curadoria extensa de obras com scroll horizontal ou uma visualização expandida em grid. As capas dos livros são coloridas automaticamente de acordo com um hexcode configurado no backend.
- **Barra de Pesquisa:** Filtragem de texto em tempo real (`oninput`) para busca rápida pelo nome do livro ou do autor sem realizar requisições pesadas ao servidor.
- **Sistema de Favoritos (Local):** Os usuários podem favoritar suas obras prediletas pela página do livro. Esses dados são salvos localmente no navegador via `localStorage` na chave `bibliotecaFavoritos`.
- **Filtro de Favoritos:** A página inicial permite alternar a visualização para apresentar apenas as obras favoritas com o clique de um botão.
- **Navegação SPA-Like:** A transição do estado do catálogo para a visualização das páginas detalhadas de Livro e Autor utiliza o `localStorage` para transferir as informações necessárias, reduzindo o tráfego backend e provendo uma experiência extremamente rápida.

## 📦 Estrutura do Projeto

- `/Controllers`: Lógica de controle e o modelo de dados unificado na classe `BibliotecaController`. Todo o acervo está "hardcoded" nesta camada, eliminando a dependência de um banco de dados externo ou do Entity Framework para esta etapa do projeto.
- `/Models`: Entidade de modelo de dados básica do C#.
- `/Views`: Camadas de apresentação Razor (`.cshtml`). O projeto possui views genéricas (`Livro.cshtml` e `Autor.cshtml`) que são populadas via JavaScript de acordo com a seleção na `Index.cshtml`.
- `/wwwroot`: Arquivos estáticos (CSS, JS).
- `/WEB3`: Este é um diretório de Prototipagem Visual puro (HTML/CSS). Usado pelos designers e engenheiros de frontend para validar interfaces e scripts antes da integração com o Razor (ASP.NET Core). **Toda mudança feita na raiz do projeto deve garantir consistência visual dentro deste diretório.**

## 🛠️ Como Executar a Aplicação

Este projeto foi construído para ser fácil de rodar em qualquer ambiente compatível com .NET 10.

1. **Clone ou baixe o repositório.**
2. **Abra o terminal na pasta raiz do projeto (onde está o `Biblioteca.csproj`).**
3. Execute o comando de compilação para garantir que o projeto está íntegro:
   ```bash
   dotnet build
   ```
4. Em seguida, inicie o servidor local:
   ```bash
   dotnet run
   ```
5. O terminal indicará o endereço local, como `http://localhost:5239`. Abra este endereço no seu navegador favorito.

**Dica em caso de problemas de porta:** Caso encontre erro de "Address already in use", libere a porta 5239 usando: `kill $(lsof -t -i :5239)`.

## 🛡️ Notas de Segurança e Performance

- A aplicação usa `AllowedHosts` configurada como `localhost` no `appsettings.json` para prevenção de vulnerabilidades do tipo _HTTP Host Header Attack_.
- As listas de livros pesadas foram otimizadas de forma que evitem recarga desnecessária, usando `static readonly` ou ordenação via LINQ apenas quando pertinente.

## 👥 Contribuições

Quando adicionar novas funcionalidades, sempre obedeça à regra de respeitar o design fluído pré-existente e utilize a API do `localStorage` para manter a experiência rápida caso não precise de processamento transacional forte no backend.

---
_Desenvolvido com dedicação por Jules e pela comunidade de desenvolvedores._