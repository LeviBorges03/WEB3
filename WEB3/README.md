# Protótipos Estáticos (WEB3)

Este diretório abriga os protótipos puramente estáticos das interfaces gráficas (UI) utilizadas no projeto de Biblioteca. O objetivo dessa pasta é permitir que desenvolvedores desenhem as páginas (HTML/CSS/JS) de forma completamente isolada do backend ASP.NET Core, testando os layouts e animações mais rapidamente.

## Estrutura
- **Autor**: Contém o HTML e CSS focado na página de detalhes do autor.
- **Livro**: Contém o HTML, CSS e scripts mockados referentes à visualização de detalhes de um livro (incluindo lógica de botões de favoritos que replicam o que existe em Views/Biblioteca).

## Como rodar e visualizar
Não é necessário utilizar a CLI do .NET para rodar estes protótipos.
Você pode visualizar utilizando uma extensão como o *Live Server* do VSCode ou iniciando um servidor HTTP local Python:

```bash
cd WEB3
python3 -m http.server 8000
```
Em seguida, acesse no navegador:
`http://localhost:8000/Autor/index.html` ou `http://localhost:8000/Livro/index.html`
