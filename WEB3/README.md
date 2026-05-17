# WEB3 Protótipos

Este diretório contém os protótipos puramente estáticos e visuais das páginas do projeto "Biblioteca".

Eles são usados para experimentações de design, validação de interface e como referência base antes da implementação no ambiente ASP.NET Core MVC principal (Razor Views).

## Conteúdo

*   **Livro (`/Livro`):** Protótipo da página de Detalhes da Obra. Inclui simulação visual da exibição do livro e a lógica funcional JavaScript para o Sistema de Favoritos via `localStorage`.
*   **Autor (`/Autor`):** Protótipo da página de Perfil do Autor, com demonstração do grid de obras relacionadas.

## Observações de Desenvolvimento

Quaisquer atualizações visuais ou lógicas de JavaScript (ex: pesquisa, favoritos) que sejam independentes de backend devem ser espelhadas nestes protótipos para manter o design system coerente.

Para testá-los, basta abrir os arquivos `index.html` diretamente em seu navegador (não é necessário servidor, exceto para algumas limitações estritas de CORS se houver chamadas a APIs locais no futuro).
