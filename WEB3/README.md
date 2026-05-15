# WEB3 - Protótipos de Interface (UI)

Este diretório contém os arquivos estáticos (HTML, CSS e JavaScript) usados para prototipar o visual e a interação da nossa aplicação de biblioteca.
Estes arquivos foram desenhados para rodar de forma 100% isolada e "offline", sem nenhuma dependência com o backend em C# ASP.NET Core MVC presente na raiz do projeto.

## Objetivo
* Testar mudanças de layout (CSS) rapidamente.
* Projetar novas estruturas HTML e comportamentos de scripts sem necessidade de compilação ou execução do projeto ASP.NET.
* Servir como uma base visual confiável para repassar as implementações para as *Views* (`.cshtml`).

## Estrutura
* **Livro/**: Contém a prototipação estática da página de Detalhes da Obra (inclui mock da funcionalidade de favoritos).
* **Autor/**: Contém a prototipação estática do perfil do Autor.

*Nota: Ao realizar alterações ou criar novas páginas de UI no projeto, mantenha sempre a correspondência entre a pasta WEB3 e as Views do projeto principal.*