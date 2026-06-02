# WEB3 - Prototipagem Frontend

Este diretório contém a representação puramente estática da interface da Biblioteca (HTML, CSS e JavaScript puros). Serve como área de prototipagem para validação de design e fluxos SPA *antes* da integração com o ASP.NET Core no projeto raiz.

## Estrutura SPA e Funcionalidades

O projeto usa abordagens SPA-like, simulando trânsito de dados através de `localStorage` para manter velocidade na navegação.

*   **index.html (Catálogo):** Apresenta o catálogo em carrossel. Funciona em conjunto com uma barra de busca (pesquisa pelo título/autor) que manipula a propriedade `display` dos cards em tempo real. Os favoritos também recebem tratamento aqui, mostrando um ícone caso o livro exista na lista de favoritos no `localStorage`.
*   **Livro/index.html (Detalhes da Obra):** Simula a view de detalhes. Lê os metadados do `localStorage` da chave `livroAtual` e manipula o botão "Adicionar aos Favoritos". Os livros marcados como favorito são salvos na chave de array JSON `bibliotecaFavoritos`.
*   **Autor/index.html (Detalhes do Autor):** Lê da chave `autorAtual` para atualizar as informações biográficas e listar obras fictícias do autor.

## Uso

Para rodar este protótipo na máquina local:

```bash
cd WEB3
python3 -m http.server 8000
```
O servidor será acessível em `http://localhost:8000`.
