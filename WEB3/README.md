# WEB3 - UI Protótipos

Este diretório (`WEB3/`) contém arquivos puramente estáticos - HTML, CSS e JavaScript Vanilla.
Ele serve como a fundação de design e isolamento de protótipos visuais para a Biblioteca Digital, desconectado do backend ASP.NET Core MVC.

## Propósito

A finalidade deste repositório isolado é permitir testes rápidos de UI e modificações visuais (HTML/CSS) simulando comportamento de dados via JavaScript (`localStorage`) para itens como as listas de livros e o sistema de "Favoritos".

Ao alterar arquivos aqui, lembre-se de refletir quaisquer mudanças de design ou lógica aplicável para os arquivos `.cshtml` nas Views do MVC, pois a aplicação final compila à partir do diretório raiz.

## Como Executar

Para servir as páginas estáticas deste diretório para experimentação e testes via navegador, utilize o comando (estando no diretório `WEB3/`):

```bash
python3 -m http.server 8000
```

E acesse em seu navegador: `http://localhost:8000/`.