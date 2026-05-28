# Biblioteca MVC e WEB3

Este projeto é uma aplicação web completa para catalogar e visualizar livros clássicos, estruturada em duas partes principais:

1. **Aplicação ASP.NET Core MVC (Raiz do repositório):** A aplicação funcional, utilizando C# (.NET 10.0) para controladores e modelos, e Razor Pages/HTML/CSS para a interface.
2. **Protótipos WEB3 (`WEB3/`):** Uma representação estática (HTML, CSS e JS puros) das páginas de detalhe do Livro e do Autor, sem a dependência do backend ASP.NET Core, útil para prototipagem rápida da UI.

## Funcionalidades Principais

*   **Catálogo de Livros:** Uma vitrine (Home) com rolagem horizontal (carrossel) e um botão para expandir a visão em grade com todos os títulos disponíveis.
*   **Barra de Pesquisa:** Localizada no topo do catálogo, permite filtrar em tempo real os livros por título ou autor.
*   **Navegação SPA-Like:** A transição entre o Catálogo, a página de Detalhes do Livro e o Perfil do Autor utiliza `localStorage` para transferir dados, evitando recarregamentos completos e consultas repetidas ao servidor (sem uso de banco de dados).
*   **Sistema de Favoritos:** O usuário pode favoritar livros na página de Detalhes. Esta preferência é salva diretamente no navegador usando `localStorage` sob a chave `bibliotecaFavoritos`, sendo persistente entre sessões.
*   **Design Responsivo e Moderno:** Interface pensada para se adaptar a diferentes tamanhos de tela, com cores agradáveis, botões elegantes e transições suaves. A capa dos livros é gerada usando cores hexadecimais ao invés de imagens, baseadas na propriedade `CorCapa` do modelo.

## Arquitetura e Decisões Técnicas

*   **Sem Banco de Dados:** A aplicação não utiliza Entity Framework ou qualquer banco de dados. Todos os dados (A lista de livros) estão mocados diretamente no `BibliotecaController.cs`. Eles são ordenados durante a inicialização (por data de publicação) para melhorar a performance.
*   **Armazenamento no Cliente:** O uso intensivo de `localStorage` para navegação e favoritos é uma decisão arquitetural para manter o backend simples (estritamente focado em servir as Views iniciais e a lista estática) e fornecer uma experiência de usuário (UX) muito ágil.

## Como Executar o Projeto

### Rodando a aplicação ASP.NET Core MVC (Completa)

1. Certifique-se de ter o SDK do .NET 10.0 instalado.
2. Navegue até o diretório raiz do projeto (onde está o arquivo `Biblioteca.csproj`).
3. Execute o comando de compilação:
   ```bash
   dotnet build
   ```
4. Inicie o servidor:
   ```bash
   dotnet run
   ```
5. Acesse no navegador a URL exibida no console (geralmente `http://localhost:5239`).

> **Aviso:** Se você receber um erro de "Address already in use", você pode matar o processo que está usando a porta com o comando `kill $(lsof -t -i :5239)`.

### Rodando os protótipos estáticos (WEB3)

1. Navegue até a pasta `WEB3/`:
   ```bash
   cd WEB3
   ```
2. Inicie um servidor HTTP simples usando Python:
   ```bash
   python3 -m http.server 8000
   ```
3. Acesse `http://localhost:8000` no seu navegador para ver os protótipos do Autor e do Livro.
