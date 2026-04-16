# Biblioteca Digital (Catálogo de Clássicos)

Este projeto é uma aplicação web ASP.NET Core MVC (escrita em C# e visando o framework .NET 10.0) que atua como um catálogo digital de obras literárias clássicas. O banco de dados suportado é o MySQL (via Pomelo.EntityFrameworkCore.MySql versão 9.0.0).

## Funcionalidades Principais

- **Vitrine Dinâmica**: A página principal apresenta um carrossel responsivo de obras literárias.
- **Navegação SPA-Like**: A aplicação aproveita o `localStorage` do navegador para oferecer uma navegação rápida e suave entre o catálogo, a página de detalhes de um livro e o perfil do autor, reduzindo a necessidade de consultas redundantes ou recarregamento total de página para obter informações secundárias.
- **Barra de Pesquisa em Tempo Real**: Os usuários podem filtrar os livros exibidos instantaneamente na página principal pelo título, autor ou gênero literário, melhorando a descoberta de novas obras.
- **Sistema de Favoritos**: Usuários podem marcar obras como "Favoritas". Esse estado é salvo e mantido localmente, e a interface se ajusta visualmente para refletir essa escolha em futuras visitas.

## Como Executar a Aplicação

1. **Pré-requisitos**:
   - SDK do .NET 10.0 ou superior instalado.
   - Um servidor MySQL (ex: `localhost`, versão 8.0.40 ou superior).

2. **Configuração de Banco de Dados**:
   - Forneça as credenciais sensíveis via variáveis de ambiente configurando `ConnectionStrings__DefaultConnection` (nunca adicione `UID` ou `PWD` diretamente no arquivo `appsettings.json`).

3. **Compilando e Rodando**:
   - Abra o terminal na raiz do repositório.
   - Execute o comando: `dotnet build`
   - Após a compilação bem-sucedida, inicie a aplicação com o comando: `dotnet run`
   - O servidor local iniciará, normalmente acessível na porta http://localhost:5239 (ou nas indicadas no log do terminal).

## Diretório WEB3
Para versões estáticas HTML/CSS de demonstração, consulte os arquivos dentro do diretório `/WEB3`. Este diretório possui seu próprio README acompanhando as modificações front-end estáticas correspondentes à lógica do MVC.
