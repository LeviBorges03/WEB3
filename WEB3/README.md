# WEB3 - Biblioteca (Versões Estáticas)

A pasta `WEB3/` deste repositório contém a representação puramente estática e isolada (HTML, CSS e JavaScript sem o framework ASP.NET Core) de certas visões e fluxos da nossa aplicação de biblioteca. Estas visões estáticas permitem testar regras de interface e prototipar componentes de forma isolada.

## Funcionalidades Presentes

- **Navegação Isolada**: Telas como `Autor` e `Livro` possuem suas próprias implementações puramente baseadas no DOM e JavaScript.
- **Sistema de Favoritos**: Assim como na versão MVC (com Razor), a visualização dos detalhes do livro estática (`WEB3/Livro/index.html`) simula a capacidade de adicionar e remover livros da chave `bibliotecaFavoritos` utilizando o `localStorage`.

## Diretrizes de Manutenção

Qualquer mudança feita no repositório principal no que tange a layout e UX (como atualizações de JavaScript, novas estruturas de CSS e afins) deve ser, sempre que possível, refletida também nas versões estáticas correspondentes dentro da pasta `WEB3/`, garantindo assim que o ambiente de prototipagem e a versão final em MVC permaneçam perfeitamente consistentes.
