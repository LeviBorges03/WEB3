# Biblioteca Web

## Arquitetura do Projeto
Este projeto é uma aplicação **ASP.NET Core MVC** desenvolvida em **.NET 10.0**.

### Características Principais
* **Sem Banco de Dados:** O sistema **não utiliza** o Entity Framework ou qualquer banco de dados relacional (ex: SQL Server). Todos os dados e modelos de livros estão *hardcoded* em memória diretamente no controlador (`BibliotecaController.cs`) para otimização de performance.
* **Sistema de Favoritos via LocalStorage:** O projeto conta com um sistema de favoritos no front-end, onde os dados são salvos localmente no navegador do usuário utilizando a API do `localStorage` através da chave `bibliotecaFavoritos` (salvo em formato JSON array contendo os títulos das obras). Isso evita a necessidade de persistência no backend.
* **Barra de Pesquisa (Instant Search):** A aplicação suporta busca dinâmica baseada em *Single Page Application* (SPA). A busca por títulos ou autores ocorre via o evento JavaScript `oninput`, e não por `onkeyup`, garantindo detecção de *paste*. Os resultados são dispostos usando o Flexbox (aplicando `style.display = 'flex'` explícito para itens encontrados, em conformidade com as restrições arquiteturais).

## Como Executar Localmente
Para testar a aplicação em seu ambiente local, execute os seguintes passos no terminal (a partir da raiz do repositório):

1. **Compilar o Projeto:**
   ```bash
   dotnet build
   ```

2. **Rodar a Aplicação:**
   Inicie a aplicação utilizando:
   ```bash
   dotnet run
   ```
   *Nota: Por padrão, o ambiente de desenvolvimento iniciará o servidor na porta 5239 (`http://localhost:5239`).*

### Resolução de Problemas (Troubleshooting)
Se você tentar rodar o servidor e a porta já estiver em uso ("Address already in use"), force a parada do processo e reinicie utilizando:
```bash
kill $(lsof -t -i :5239)
```

## Protótipos Estáticos (WEB3)
O diretório `/WEB3/` na raiz do repositório é uma **representação totalmente estática e isolada** do front-end original.
Qualquer modificação de estilo, CSS, ou funcionalidades Javascript que envolvam componentes (como a página de detalhes de autor ou livro) devem idealmente ser reproduzidas em ambas as instâncias para manter coerência. Consulte [WEB3/README.md](WEB3/README.md) para mais detalhes.