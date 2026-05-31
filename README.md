# Biblioteca Web

Uma aplicação web ASP.NET Core MVC (C#) para catalogar obras literárias clássicas.

## Arquitetura e Decisões Técnicas

Este projeto adota algumas decisões arquiteturais para se manter simples e fluido:

- **Sem Banco de Dados:** A aplicação não utiliza Entity Framework ou bancos de dados reais. Todos os dados (como a lista de livros disponíveis) estão configurados de forma estática (`List<Livro>`) dentro do `BibliotecaController`.
- **Navegação SPA-Like via LocalStorage:** O projeto se comporta como uma Single Page Application (SPA) para dados de contexto, passando informações de uma view para outra usando a API `localStorage` do navegador em vez de roundtrips constantes de requisições GET para o servidor.
  - Chave `livroAtual`: Armazena um JSON com detalhes do livro selecionado na `Index.cshtml` para ser montado em `Livro.cshtml`.
  - Chave `autorAtual`: Armazena o nome do autor clicado, que é lido dinamicamente em `Autor.cshtml`.
  - Chave `bibliotecaFavoritos`: Array JSON que salva os títulos dos livros curtidos pelo usuário.
- **Barra de Pesquisa e Filtros:** Implementados inteiramente em JavaScript na página inicial para filtro em tempo real sem chamadas de rede.

## Como Executar o Servidor Backend (ASP.NET Core)

Certifique-se de que o SDK .NET 10.0 está instalado e execute:

```bash
dotnet build
dotnet run
```

A aplicação subirá em `http://localhost:5239`.

> **Nota:** Em caso de erro "Address already in use" na porta 5239, você pode matar o processo que a retém com o comando:
> `kill $(lsof -t -i :5239)`

## Visualizando o Protótipo Front-End (Pasta WEB3)

Este repositório também inclui uma pasta `WEB3/` contendo um protótipo estático puramente em HTML, CSS e JS que serviu de base para a construção das Views do ASP.NET Core.

Se quiser executar apenas este protótipo, vá até o diretório `WEB3` e utilize um servidor local, por exemplo:

```bash
cd WEB3
python3 -m http.server 8000
```

E então acesse `http://localhost:8000` em seu navegador.
