# WEB3 - Protótipo Estático (UI)

Este diretório `WEB3` contém uma versão puramente estática da interface de usuário da aplicação **Biblioteca**.

Ele serve como um protótipo visual independente do backend ASP.NET Core MVC, permitindo focar exclusivamente no desenvolvimento e na experimentação de HTML, CSS e JavaScript sem a necessidade de compilar a aplicação ou rodar um banco de dados.

## Estrutura
- **`Livro/` e `Autor/`:** Pastas contendo as páginas HTML e estilos CSS correspondentes às views para visualização e isolamento do design.
- As mudanças feitas aqui, quando aprovadas em termos de UI/UX, costumam ser transportadas para as views Razor reais localizadas em `../Views/Biblioteca/`.

## Nota de Manutenção
Qualquer atualização no design principal ou na estrutura do catálogo deve ser considerada em ambos os lados (no projeto raiz MVC e aqui, se o protótipo precisar ser mantido em sincronia para testes de design rápidos).
