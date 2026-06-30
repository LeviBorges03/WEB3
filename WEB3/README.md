# Prototipagem UI (WEB3)

A pasta `WEB3/` deste repositório abriga os protótipos estáticos do projeto da Biblioteca. Esses arquivos (`HTML`, `CSS`, e `JS`) servem para isolar as validações visuais e iterar sobre o design das páginas antes que elas sejam integradas nas Views dinâmicas do ASP.NET Core (Razor Pages).

## 🗂️ Estrutura

- **/Autor:** Contém a interface do perfil do autor e sua biografia estática.
- **/Livro:** Contém a interface de detalhes do livro e formatação da capa.

## 💡 Como Executar os Protótipos

Para testar ou desenvolver o layout puramente estático sem a necessidade do backend ASP.NET Core:

1. Abra um terminal apontando para a pasta `WEB3`.
2. Inicie um servidor HTTP local simples usando o Python:
   ```bash
   python3 -m http.server 8000
   ```
3. No navegador, acesse `http://localhost:8000/Livro` ou `http://localhost:8000/Autor` para ver os protótipos em ação.

## 🔗 Relação com o Projeto Principal

As alterações de design validadas aqui devem ser migradas e adaptadas nas _Views_ (localizadas em `Views/Biblioteca/`) e nos arquivos estáticos globais (localizados em `wwwroot/`) da raiz do projeto ASP.NET Core. Sempre mantenha consistência entre o layout provado nesta pasta e a renderização Razor final.