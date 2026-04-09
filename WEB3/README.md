# WEB3 (Pasta de Documentação e Recursos Estáticos de Referência)

Esta pasta contém o backup de recursos HTML, CSS e imagens (quando aplicável) que orientaram o desenvolvimento das `Views` ASP.NET Core MVC (Razor Pages).

Embora a aplicação principal seja o projeto raiz `.csproj`, os arquivos aqui podem servir para validar o design, verificar classes CSS propostas ou entender a estrutura HTML desejada antes da conversão para as views dinâmicas do Razor.

## Relação de Funcionalidades e Conceitos SPA-Like

Como exigido pelo modelo de design, este projeto abraça as capacidades de Web3 no sentido de client-side storage, utilizando o navegador do próprio usuário para melhorar a navegação.

*   **Busca Instantânea:** A barra de pesquisa adicionada no topo do `Index` (Catálogo) manipula diretamente os elementos do DOM da página sem a necessidade de uma Action específica de busca ou uso do banco de dados, tornando a resposta instantânea.
*   **Favoritos Descentralizados:** Ao clicar em "Adicionar aos Favoritos" dentro dos detalhes de uma obra (`Livro.cshtml`), o objeto inteiro do livro é salvo no `localStorage` do usuário. Isso dispensa uma tabela de relacionamento e endpoints para gerenciar perfis logados, descentralizando essa escolha para o próprio dispositivo.
*   **Gestão de Favoritos:** A interface em `Favoritos.cshtml` recupera esses dados via JavaScript e hidrata a tela com os *cards* correspondentes. A remoção também ocorre localmente pela chave no array JSON.