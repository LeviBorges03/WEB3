# Protótipos Estáticos (WEB3)

Este diretório (`WEB3/`) contém uma representação puramente estática e isolada da interface de usuário da aplicação principal.

## Objetivo
O objetivo destes arquivos é servir como um ambiente de prototipação (HTML, CSS e JS puros) onde designers ou desenvolvedores front-end possam iterar o visual e interações das páginas de "Detalhes do Livro" e "Perfil do Autor" sem a necessidade de configurar, compilar ou rodar o backend ASP.NET Core MVC.

## Funcionalidades Integradas no Protótipo
- **Layout Fiel:** As páginas emulam perfeitamente o CSS principal da aplicação.
- **Sistema de Favoritos (Local):** A página de Detalhes do Livro (`Livro/index.html`) simula a adição/remoção de favoritos acessando o `localStorage` do navegador, mantendo a consistência funcional com a aplicação raiz.

## Como Utilizar
Como são arquivos estáticos simples, você pode simplesmente abrir os arquivos `index.html` em qualquer navegador moderno para visualizar e interagir com o layout:
- `WEB3/Livro/index.html`
- `WEB3/Autor/index.html`

*Nota:* Ao alterar o design ou funcionalidade base destes arquivos, lembre-se de refletir as mesmas mudanças nos arquivos `.cshtml` correspondentes no diretório `Views/` do projeto principal para manter a paridade.
