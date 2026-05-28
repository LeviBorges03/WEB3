# Biblioteca WEB3 (Protótipos Estáticos)

Esta pasta contém os protótipos puramente estáticos da interface da aplicação Biblioteca. Aqui, você encontrará apenas arquivos HTML, CSS e JavaScript sem nenhuma dependência do backend (ASP.NET Core ou C#).

## Objetivo

O objetivo deste diretório é permitir a prototipagem rápida e testes de design e layout da interface de usuário antes de sua integração nas Razor Pages (`.cshtml`) da aplicação principal. Qualquer alteração de design, como estilos (CSS) ou comportamentos de interface (JS, como o sistema de favoritos), deve ser feita e validada primeiramente aqui ou mantida em sincronia com o projeto raiz para referência.

## Como Executar Localmente

Você não precisa do .NET SDK para visualizar estas páginas. Basta servir os arquivos estáticos:

1. Certifique-se de estar dentro desta pasta (`WEB3/`).
2. Use o Python para iniciar um servidor local rápido:
   ```bash
   python3 -m http.server 8000
   ```
3. Abra seu navegador e acesse: `http://localhost:8000`. A partir daí, você pode navegar pelas pastas `Autor/` e `Livro/` e abrir seus respectivos `index.html`.

## Funcionalidades Demonstradas

*   **Página do Livro (`Livro/index.html`):** Demonstra o layout de detalhes de uma obra e a integração do script local para o **Sistema de Favoritos** (que utiliza o `localStorage` do navegador para manter o estado do botão "Adicionar aos Favoritos").
*   **Página do Autor (`Autor/index.html`):** Apresenta o perfil detalhado do autor e a lista estática (mockada) de suas obras.