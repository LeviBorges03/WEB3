# WEB3 - UI Prototypes

A pasta `WEB3/` deste repositório serve como um **ambiente de prototipação estática (isolado)** para a interface do usuário da aplicação.

Seu objetivo é possibilitar o trabalho de designers e desenvolvedores na interface (HTML, CSS, JS puros) sem precisar lidar com a complexidade do framework ASP.NET Core MVC (como as renderizações em Razor, Controllers e configurações de servidor).

## Manutenção e Sincronia
Ao atualizar qualquer classe CSS, estrutura HTML ou lógica visual neste diretório, **você deve garantir que essas mudanças sejam replicadas para as views Razor** correspondentes no diretório `Views/` do projeto principal e vice-versa.

## Como rodar o protótipo
Os arquivos aqui são páginas estáticas `index.html`. Para visualizar e testar o funcionamento (como responsividade, cores e simulação de navegação), levante um servidor local leve diretamente nesta pasta:

```bash
cd WEB3
python3 -m http.server 8000
```

Feito isso, abra `http://localhost:8000` em seu navegador e explore os arquivos e pastas simulando a navegação.
