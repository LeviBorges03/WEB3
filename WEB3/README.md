# Biblioteca - WEB3 Prototypes

A pasta `WEB3/` deste repositório abriga os protótipos puramente estáticos da interface do usuário para o sistema **Biblioteca**.

## O que é a pasta WEB3?

É um ambiente isolado, contendo apenas HTML puro, CSS e JavaScript Vanilla, sem qualquer dependência ou amarração com o ecossistema ASP.NET Core (como Razor, Models, Controllers, etc.).

## Por que ela existe?

O objetivo principal deste diretório é facilitar o design da UI, prototipação ágil e homologação visual do projeto. Designers e desenvolvedores Frontend podem criar layouts flexíveis, testar animações CSS, ou aprimorar interações (ex: como o Sistema de Favoritos) de maneira inteiramente desacoplada do Backend de produção.

## Manutenção e Sincronização

Sempre que introduzir ou melhorar novas mecânicas de UI, animações, estilos CSS (ex: transições, botões "pill-shaped", ou classes como `.search-input`), garanta que o código nesta pasta permaneça atualizado e consistente com as views C# (.cshtml) na raiz do projeto.

Se um script em JavaScript for atualizado para manipular o `localStorage` do sistema principal (como por exemplo o array `bibliotecaFavoritos`), esse comportamento ou sua representação visual também devem ser refletidos ou documentados aqui para que a equipe de design entenda o fluxo.

## Estrutura Atual:
- **Livro/**: Contém o protótipo da página de Detalhes da Obra, incluindo o botão de gerenciar Favoritos do usuário.
- **Autor/**: Contém a estrutura e layout da página com os detalhes e a bibliografia de um autor selecionado.