# Catálogo da Biblioteca

Bem-vindo ao projeto da Biblioteca! Este é um projeto ASP.NET Core MVC projetado para fornecer um catálogo virtual moderno, responsivo e rico para visualização de livros e autores.

## Funcionalidades

O sistema conta com as seguintes funcionalidades principais:

1. **Navegação SPA-Like**: Em vez de fazer requisições completas ao backend para cada página, o aplicativo usa a funcionalidade `localStorage` do navegador para transferir rapidamente dados entre as views (Index, Livro e Autor), resultando em uma experiência mais suave e com cara de Single Page Application.
2. **Sistema de Favoritos**: Os usuários podem favoritar suas obras preferidas na página do livro. Esses dados são salvos localmente (usando o armazenamento do navegador na chave `bibliotecaFavoritos`) e as obras favoritadas recebem uma estrela (⭐) diretamente na vitrine do catálogo.
3. **Barra de Pesquisa**: Uma barra de pesquisa ágil está disponível na vitrine. Ao digitar o título de uma obra ou o nome do autor, os cards são filtrados instantaneamente.
4. **Protótipo Isolado (WEB3)**: A pasta `WEB3` possui a estrutura HTML/CSS/JS estática equivalente ao código dinâmico gerado pelo servidor, ideal para facilitar o protótipo de UI, testar estilos e garantir a integridade do design antes da implementação com Razor Pages.

## Execução Local

### ASP.NET Core (Aplicação Principal)

Para rodar a aplicação em seu ambiente de desenvolvimento, utilize a linha de comando no diretório raiz do projeto:

```bash
dotnet build
dotnet run
```

O servidor começará a escutar na porta padronizada (geralmente http://localhost:5239), permitindo o acesso via navegador.

### UI Isolada (WEB3)

Para verificar o protótipo isolado, navegue até o diretório `WEB3` e inicie um servidor estático. Você pode fazer isso rapidamente com Python:

```bash
cd WEB3
python3 -m http.server 8000
```

Abra http://localhost:8000 em seu navegador para visualizar as páginas.
