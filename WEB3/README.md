# WEB3 - Ambiente de Prototipagem de Interface

## O que é o diretório WEB3?

O diretório `WEB3` é um ambiente **isolado de prototipagem estática**. Ele contém arquivos unicamente voltados para o frontend (`.html`, `.css`, e scripts JS incorporados) e não tem dependência com o backend em ASP.NET Core (`.cshtml` ou `Controllers`).

## 🎯 Qual é o propósito?

Ele é utilizado pela equipe de design e engenharia frontend para:

1. **Desenvolver o Design System:** Criar variáveis CSS, grids e layouts fluidos e testá-los antes da integração com a lógica Razor no backend.
2. **Testar Funcionalidades SPA:** Modelar as interações de UI (ex: salvar/remover nos favoritos do `localStorage` ou testes visuais da tela de Livro e Autor) puramente com o DOM e o navegador.
3. **Agilidade:** Permitir que as interfaces sejam construídas, avaliadas e validadas sem precisar recompilar ou executar a aplicação .NET.

## ⚠️ Regra de Consistência

Qualquer mudança que envolva adicionar classes no CSS base, alterar a arquitetura dos layouts ou incluir novas lógicas de UI via JavaScript na raiz do projeto (nas `Views`), **deve ser refletida e atualizada dentro deste diretório `WEB3/`**, para que os protótipos de design nunca fiquem desatualizados em relação ao que está em produção.

## Funcionalidades Prototipadas Atualmente

- Tela de Detalhes do **Livro** com interatividade no botão de "Adicionar/Remover dos Favoritos" salvando via `localStorage` na chave `bibliotecaFavoritos`.
- Tela de Perfil do **Autor** com layout grid fluído para as obras publicadas.