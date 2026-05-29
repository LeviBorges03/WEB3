# Biblioteca Digital

Este é um projeto de Biblioteca Digital desenvolvido com **ASP.NET Core MVC (C#)**. Ele simula uma vitrine de livros com navegação baseada em Single Page Application (SPA), onde os dados trafegam pelo `localStorage` no lado do cliente.

## 📌 Arquitetura e Estrutura

- **Sem Banco de Dados:** O projeto não utiliza banco de dados (Entity Framework). Todos os modelos e dados dos livros (clássicos da literatura) estão mockados diretamente dentro do `BibliotecaController`.
- **Navegação SPA-Like:** Em vez de fazer chamadas de rede para buscar dados de um livro específico ou de um autor, a aplicação armazena os dados da seleção atual em `localStorage` (como `livroAtual` e `autorAtual`). As visualizações (`Livro.cshtml` e `Autor.cshtml`) consomem esses dados locais pelo JavaScript e populam a página dinamicamente.
- **Sistema de Favoritos:** Utiliza o `localStorage` (chave `bibliotecaFavoritos`) para armazenar um array JSON com os títulos dos livros favoritado, permitindo persistência de estado no cliente.
- **Protótipo Estático:** O diretório `/WEB3` contém uma versão do front-end puramente HTML, CSS e JS (protótipo). Manutenções de UI devem ser espelhadas tanto no MVC (`/Views` e `/wwwroot`) quanto em `/WEB3`.

## 🛠️ Tecnologias Utilizadas

- **Backend:** C# / .NET 10.0 / ASP.NET Core MVC
- **Frontend:** HTML5, CSS3, JavaScript Vanilla
- **Estilização:** CSS customizado focado em fluidez e temas modernos.

## 🚀 Como Executar

### Rodando o Servidor ASP.NET MVC
1. Certifique-se de ter o SDK do .NET 10.0 instalado.
2. No diretório raiz do projeto, restaure e compile:
   ```bash
   dotnet build --no-restore
   ```
3. Inicie o servidor:
   ```bash
   dotnet run
   ```
   *Se a porta 5239 estiver em uso, você pode matar o processo rodando:*
   `kill $(lsof -t -i :5239)`
4. Acesse http://localhost:5239 no seu navegador.

### Rodando o Protótipo Estático (WEB3)
Para fins de validação de layout:
1. Navegue até a pasta:
   ```bash
   cd WEB3
   ```
2. Inicie um servidor HTTP local:
   ```bash
   python3 -m http.server 8000
   ```
3. Acesse http://localhost:8000 no navegador.
