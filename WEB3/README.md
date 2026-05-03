# Catálogo da Biblioteca

## Sobre o Projeto
Este é um projeto desenvolvido em ASP.NET Core MVC (C#) voltado para exibir um catálogo digital de obras literárias clássicas. O projeto possui um forte foco em design de interface relaxante e moderno (com foco na experiência do usuário) e gerenciamento de estado no lado do cliente.

A aplicação se comporta de forma parecida com uma Single Page Application (SPA) para a navegação de dados de livros e autores, fazendo uso de \`localStorage\` para transferir dados entre as Views (ex: passando detalhes do livro selecionado na listagem principal para a página de detalhes da obra) sem necessitar de consultas frequentes ao servidor.

## Principais Funcionalidades
- **Catálogo de Clássicos:** Uma vitrine fluída exibindo diversas obras clássicas, permitindo navegação por carrossel e modo expandido.
- **Sistema de Pesquisa:** Filtragem em tempo real de livros por título e autor utilizando JavaScript.
- **Sistema de Favoritos:** Possibilidade de adicionar livros aos favoritos. Os dados são persistidos localmente no navegador do usuário via \`localStorage\` (chave: \`bibliotecaFavoritos\`).
- **Transferência de Estado no Cliente:** Os dados exibidos nas páginas de "Detalhes da Obra" e "Perfil do Autor" são dinamicamente preenchidos no lado do cliente, baseados no item selecionado previamente na página principal.

## Tecnologias Utilizadas
- **Backend:** C# / ASP.NET Core MVC (.NET 10.0)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Persistência:** Pomelo.EntityFrameworkCore.MySql (para operações de banco futuras) e \`localStorage\` para controle de estado do cliente.

## Estrutura do Projeto
- O código-fonte principal em C# e ASP.NET encontra-se na raiz do repositório (diretórios \`Controllers\`, \`Models\`, \`Views\`, etc).
- Há um diretório chamado \`WEB3/\` que serve como um protótipo estático puramente em HTML/CSS/JS do layout e fluxos, para facilitar validações de design em ambiente isolado.

## Como Executar Localmente
1. Certifique-se de que o SDK do .NET (versão 10.0) esteja instalado.
2. Clone o repositório.
3. Se estiver em um sistema onde a porta 5239 já esteja em uso, libere-a antes de rodar o servidor:
   \`kill $(lsof -t -i :5239)\`
4. Na raiz do projeto, execute:
   \`dotnet build\`
5. Inicie a aplicação com:
   \`dotnet run\`
6. Acesso o servidor local em: \`http://localhost:5239\`

## Boas Práticas e Observações
- A configuração da conexão com o banco de dados via Entity Framework deve ser feita utilizando as variáveis de ambiente pertinentes (como \`ConnectionStrings__DefaultConnection\`) e nunca committadas dentro do \`appsettings.json\`.
- Nunca commite as pastas \`bin/\` ou \`obj/\`.
