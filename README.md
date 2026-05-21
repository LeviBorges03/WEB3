# Biblioteca Clássica - ASP.NET Core MVC

Este projeto é um catálogo moderno e responsivo de obras clássicas da literatura.
Desenvolvido com ASP.NET Core MVC e C#, ele usa tecnologias front-end para fornecer uma experiência fluida de Single Page Application (SPA), apesar de ter uma arquitetura multi-page tradicional.

## Recursos e Funcionalidades
- **Barra de Pesquisa em Tempo Real**: Filtre livros diretamente na página principal por título, autor ou gênero sem recarregar a página (utilizando JavaScript).
- **Sistema de Favoritos**: Permite aos usuários favoritar livros em sua máquina local. O estado é gerido utilizando `localStorage` (chave: `bibliotecaFavoritos`).
- **Navegação SPA-Like**: Os dados de seleção entre as telas (Livro Atual, Autor Atual) são armazenados via `localStorage` e renderizados no lado do cliente nas Views secundárias.
- **Visual Moderno e Relaxante**: Desenvolvido com estilos em CSS nativo focado na usabilidade, animações suaves e botões tipo pílula ("pill-shaped").
- **Performance**: O servidor possui otimizações para ordenar listas carregadas na memória, dispensando uso de Entity Framework ou Banco de Dados (as obras estão _hardcoded_ no Controller).

## Como Rodar o Projeto

Você precisará do SDK do .NET 10.0 instalado.

1. **Compilar**:
   No diretório principal do projeto (onde está localizado o arquivo `.csproj`), execute:
   ```bash
   dotnet build
   ```

2. **Executar**:
   Logo em seguida, inicie o servidor:
   ```bash
   dotnet run
   ```
   *Caso você enfrente erros de Timeout na restauração do NuGet no seu ambiente local, você pode utilizar `dotnet build --no-restore` se os pacotes já estiverem cacheados.*

3. Acesse a aplicação na URL informada no console (geralmente http://localhost:5239).

### Dicas de Ambiente:
- Se houver problema de porta em uso ("Address already in use"), execute: `kill $(lsof -t -i :5239)`.
- A pasta `WEB3/` contém um protótipo visual puramente HTML/CSS/JS e não necessita do .NET para ser visualizada. Veja `WEB3/README.md` para mais detalhes.