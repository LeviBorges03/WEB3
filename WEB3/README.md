# WEB3 - Protótipo Estático

Este diretório contém uma versão puramente estática da interface da aplicação **Biblioteca - Catálogo de Clássicos**. Ele serve como um laboratório visual para o design (HTML, CSS e JavaScript) antes de integrá-lo com o backend em ASP.NET Core.

## Funcionalidades do Protótipo

- Estrutura completa de navegação entre o Catálogo (Home), os Detalhes do Livro e o Perfil do Autor.
- Visualização de carrossel de livros e layouts em grade responsiva.
- Simulação das funcionalidades interativas, como o botão de **Favoritos** e a **Barra de Pesquisa** em tempo real, cujos comportamentos lógicos são detalhados na integração com o ASP.NET no projeto principal.

## Como Visualizar Localmente

Você pode servir estes arquivos utilizando qualquer servidor HTTP simples. Por exemplo, se tiver o Python instalado, você pode executar o seguinte comando a partir deste diretório (`WEB3/`):

```bash
python3 -m http.server 8000
```

E em seguida, acessar `http://localhost:8000` no seu navegador.
