# WEB3 - Protótipos Estáticos UI

Este diretório contém a representação puramente estática e isolada (HTML, CSS e JavaScript puros) das páginas e interações da nossa Biblioteca Virtual, sem qualquer dependência do ASP.NET Core.

## Propósito
- **Prototipação Rápida**: Facilita a experimentação de novos estilos visuais (UI) e jornadas do usuário (UX), como as animações de expansão de botões e carrossel de livros.
- **Validação de Frontend**: Ideal para testar a lógica cliente-side (como o armazenamento de favoritos com `localStorage` e filtros) em um ambiente controlado antes da integração com as Views Razor (`.cshtml`).

## Como Visualizar
Não é necessário nenhum servidor ou build para visualizar os protótipos. Basta abrir os arquivos `.html` diretamente no seu navegador:
- `/WEB3/Livro/index.html` (Detalhes e lógica de Favoritos emulada)
- `/WEB3/Autor/index.html` (Perfil de Autor isolado)

**Atenção Desenvolvedor**: Quando fizer atualizações em designs ou regras de JS importantes aqui (como o sistema `bibliotecaFavoritos`), lembre-se de transpor e adaptar as mudanças equivalentes nos arquivos localizados em `Views/Biblioteca` na raiz do projeto (ASP.NET).