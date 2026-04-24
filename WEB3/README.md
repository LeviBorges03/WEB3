# WEB3 - Protótipo Estático de UI

## Propósito do Diretório
O diretório `WEB3/` abriga uma representação puramente estática e isolada (HTML, CSS e JS puros, sem ASP.NET Core) da interface da aplicação **Biblioteca Digital**.

Ele foi criado e deve ser mantido como um protótipo de design. Ele é extremamente útil para:
- Realizar testes rápidos de design UI/UX (ajustes em CSS Flexbox, Grid, Animações) sem precisar levantar o servidor ASP.NET Core e aguardar tempos de build do C#.
- Validar scripts JavaScript isolados (como o sistema de busca ou favoritos usando `localStorage`) de maneira rápida e segura.
- Garantir uma versão acessível para designers que não possuam ou não saibam utilizar o ambiente .NET.

## Manutenção e Sincronia
**Atenção:** Qualquer alteração de design, classes de CSS ou lógica de JavaScript de interface implementada nas views dinâmicas do ASP.NET Core (ex: `Views/Biblioteca/*.cshtml` e `wwwroot/css/*.css`) **devem** ser refletidas nos arquivos respectivos dentro de `WEB3/` e vice-versa.

Ao trabalhar em uma nova funcionalidade (ex: a busca no catálogo ou o botão de favoritar), lembre-se de manter os dois mundos (o projeto raiz e o diretório `WEB3/`) sempre sincronizados.