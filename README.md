# Biblioteca 📚

Este é o projeto **Biblioteca**, uma aplicação web moderna para exploração de um catálogo de livros clássicos, desenvolvida utilizando o framework **ASP.NET Core MVC** (.NET 10.0). O projeto tem como foco proporcionar uma experiência de usuário fluida e interativa (semelhante a uma Single Page Application - SPA), combinando renderização do lado do servidor e gerenciamento de estado dinâmico no cliente.

## 🚀 Funcionalidades e Características

- **Catálogo Interativo:** Navegue por uma vasta coleção de clássicos literários em um grid responsivo ou por um carrossel horizontal contínuo.
- **Barra de Pesquisa em Tempo Real:** Encontre facilmente obras filtrando simultaneamente por título, autor ou gênero literário, diretamente do lado do cliente para uma resposta instantânea.
- **Sistema de Favoritos:** Adicione ou remova livros de sua lista de favoritos através do `localStorage`, mantendo as seleções do usuário ativas no próprio navegador.
- **Navegação SPA-Like:** Utiliza injeção de estado via `localStorage` e JavaScript puro para transitar entre informações da Home, detalhes do Livro e o perfil do Autor sem necessidade de consultar repetidamente o backend para dados de exibição em tempo real.
- **Design Moderno:** Interface de usuário minimalista com o uso de variáveis CSS para facilitar a customização de temas, transições suaves, e elementos visuais arredondados (como botões formato "pill") para maximizar o apelo estético.

## 🛠️ Tecnologias Utilizadas

- **C# / ASP.NET Core MVC:** Estruturação robusta, seguindo os padrões de controlers, modelos e visões para roteamento eficiente.
- **Entity Framework Core (Pomelo MySQL):** Configurado para a versão `9.0.0`, preparado para injeção de dependências e escalonamento de dados, contendo seeds e definições rigorosas via `OnModelCreating`.
- **HTML5 / CSS3 / JavaScript:** Frontend sem dependências pesadas; CSS customizado baseado no conceito `mobile-first` com fallback para grids complexos em telas grandes.

## 📂 Organização do Projeto

Além do modelo padrão de pastas ASP.NET (`Controllers/`, `Views/`, `Models/`), este repositório possui a pasta separada **`WEB3/`**, que serve como um ambiente isolado de **prototipagem visual**. Qualquer alteração de documentação ou design que ocorra na raiz deve ser validada e replicada nesta pasta estática, se aplicável, para assegurar a consistência entre o layout final e o protótipo.

## ⚙️ Como Executar o Projeto Localmente

1. Tenha o .NET SDK 10 instalado em sua máquina.
2. Clone o repositório.
3. Configure a variável de ambiente correspondente ou a Connection String no seu servidor, mas *lembre-se de nunca armazenar credenciais sensíveis* no `appsettings.json` (Utilize `ConnectionStrings__DefaultConnection`).
4. Execute o comando de compilação:
   ```bash
   dotnet build
   ```
5. Rode a aplicação em segundo plano (devido a limitações de timeout local do ambiente em alguns cenários):
   ```bash
   dotnet run > dotnet_run.log 2>&1 &
   ```
6. O servidor estará acessível na porta estipulada, normalmente em `http://localhost:5239`. Se a porta estiver em uso, limpe a execução com:
   ```bash
   kill $(lsof -t -i :5239)
   ```

---
*Este projeto foi construído focando na performance de navegação e em componentes modulares que facilitam a introdução de futuras regras de negócios focadas em dados assíncronos.*