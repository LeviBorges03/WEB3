# Protótipos de UI: WEB3

## O que é este diretório?
A pasta `WEB3/` serve como um **ambiente de prototipagem visual e de componentes estáticos** para a Biblioteca.

Ele contém **apenas HTML, CSS e JavaScript nativos**, sem qualquer vinculação direta ou dependência com as tecnologias back-end do ASP.NET Core MVC (como Razor pages, Controllers ou Models em C#) hospedados na raiz do repositório.

## Motivação e Como Funciona
Este isolamento possibilita que desenvolvedores e designers testem elementos de UI, transições fluidas e novas cores para as capas de livros de maneira super rápida, sem a necessidade de rodar o *build* de pacotes ou levantar o runtime do .NET Core inteiro.

### Simulação de Estado (State Simulation)
Para manter o comportamento da camada View coerente com a aplicação final em C#:
* O sistema implementa o **mesmo mecanismo de armazenamento no navegador**. Por exemplo, os favoritos das páginas na raiz ASP.NET (que usam o `localStorage` com a chave JSON array `bibliotecaFavoritos`) também são recriados e atualizados puramente via JavaScript nesta pasta, buscando títulos diretamente do DOM (ex: tags `<h1>`).
* Isto assegura que todas as lógicas SPA-like permaneçam congruentes com o deploy completo.

## Como Executar e Testar os Protótipos Localmente
Para visualizar e interagir com estas interfaces isoladas sem usar as portas e o servidor do ASP.NET, basta criar um servidor estático básico no terminal. Recomendamos o uso do Python 3:

1. Certifique-se de estar dentro deste diretório (`WEB3/`):
   ```bash
   cd WEB3
   ```
2. Inicialize o servidor local:
   ```bash
   python3 -m http.server 8000
   ```
3. Abra seu navegador em: `http://localhost:8000`