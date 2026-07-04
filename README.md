# Sistema de Biblioteca 📚

Bem-vindo ao projeto do Sistema de Biblioteca! Esta aplicação é um catálogo digital de obras clássicas que visa promover o acesso à leitura através de uma interface moderna e responsiva. O projeto inclui um sistema de favoritos com armazenamento em `localStorage` e uma barra de pesquisa otimizada para filtragem de livros e autores em tempo real.

## Tecnologias e Arquitetura

O projeto é desenvolvido como uma aplicação ASP.NET Core MVC (C#) sem uso de banco de dados e focado no estado gerenciado do lado do cliente (via `localStorage` e JavaScript). A comunicação entre visualizações da web é realizada passando dados de estado por meio do `localStorage`, imitando as navegações das Single Page Applications (SPA). O projeto está em conformidade com o framework `.NET 10.0`.

## Como Executar a Aplicação ASP.NET Core MVC

1. No diretório raiz do projeto, você pode compilar a aplicação com o seguinte comando:
   ```bash
   dotnet build
   ```
2. Após compilar, inicie o servidor:
   ```bash
   dotnet run
   ```
3. O projeto estará disponível e escutando por padrão em `http://localhost:5239`.

## Estrutura do Diretório WEB3

O diretório `WEB3/` serve como um espaço isolado para a representação puramente estática das views, onde protótipos de interfaces de usuário (UI) sem backend integrado (apenas HTML, CSS e JS) podem ser criados, testados e apresentados. Para detalhes sobre a execução do protótipo contido neste diretório, consulte o arquivo de documentação dedicado em `WEB3/README.md`.
