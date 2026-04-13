# WEB3 - Documentação Extra do Módulo

Este diretório contém notas e documentos relativos a requisitos específicos e manutenções do Projeto WEB3: Catálogo Literário Dinâmico.

## 1. Contexto SPA e Passagem de Dados
A aplicação se comporta como uma Single Page Application em vários cenários usando a API `localStorage`.
Quando um usuário clica num livro no `Index.cshtml`, o JavaScript salva os dados daquela obra em formato JSON (`livroAtual`). A rota MVC muda para `/Biblioteca/Livro`, e então o script no cliente popula a view com os dados salvos sem precisar acessar o banco de dados. O mesmo padrão aplica-se para os dados do Autor.

## 2. Barra de Pesquisa Frontend
O recurso de pesquisa implementado na página principal não executa queries `LIKE` no banco de dados. Em vez disso, ele tira proveito de que todos os livros já estão carregados no DOM. Utilizando o evento nativo `oninput`, a tela filtra (esconde/mostra) os cards avaliando título, autor e gênero quase instantaneamente para uma melhor UX.

## 3. Gestão do Estado do "Favorito"
A persistência do botão de favoritos em `Views/Biblioteca/Livro.cshtml` é totalmente isolada no cliente. A lista de títulos é mantida num array JSON associado à chave `favoritos` no armazenamento do navegador. A função `atualizarBotaoFavorito` é chamada no carregamento da página para decidir a cor e a chamada à ação (ex: "Adicionar aos Favoritos" vs "Remover dos Favoritos").

**Nota para Desenvolvedores:** Sempre mantenha as alterações visuais em sincronia com os requisitos estabelecidos no `WEB3/README.md` e nos arquivos-raiz do projeto para consistência. Em atualizações futuras (ex. Login de usuário), este sistema local (`localStorage`) poderá ser subido para o banco de dados caso seja detectado um usuário logado.
