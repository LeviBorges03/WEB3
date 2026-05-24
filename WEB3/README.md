# Protótipo Front-End: WEB3

Esta pasta contém o protótipo puramente visual e comportamental (HTML/CSS/JS) para o projeto da Biblioteca. Funciona como um ambiente de testes de design isolado do ASP.NET Core.

## Para Que Serve?

*   Prototipar layouts, componentes e transições CSS de forma ágil.
*   Servir como referência fiel de UI e UX para a implementação no back-end (Views `.cshtml`).
*   Verificar comportamentos JavaScript (como Favoritos no `localStorage` e filtros) em um ambiente puramente client-side.

## Como Visualizar

Nenhuma instalação de back-end é requerida para esta pasta. Você pode abrir os arquivos `index.html` diretamente no seu navegador, ou, preferencialmente, iniciar um servidor local estático simples:

```bash
cd WEB3/
python3 -m http.server 8000
```

Em seguida, acesse `http://localhost:8000` ou `http://localhost:8000/Livro/` no seu navegador.

## Manutenção

Ao realizar atualizações de interface na raiz do projeto (no diretório `Views/` ou `wwwroot/`), certifique-se de aplicar as mesmas alterações de marcação e de CSS/JS aqui dentro da pasta `WEB3/` para que o protótipo se mantenha como fonte de verdade para a equipe de design.
