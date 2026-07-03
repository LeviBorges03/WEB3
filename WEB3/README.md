# WEB3 - Protótipos de Interface

Este diretório contém a prova de conceito original (protótipos estáticos em HTML/CSS) para as telas do projeto **Biblioteca Digital**. Estes arquivos foram criados independentemente do ASP.NET Core para testar o layout, responsividade e estilo.

## Estrutura
- **`/Autor`**: Protótipo da página de perfil do autor.
- **`/Livro`**: Protótipo da página de detalhes do livro.

## Como Visualizar os Protótipos
Como os arquivos referenciam estilos locais, é recomendado visualizá-los rodando um servidor estático simples para evitar problemas de CORS e caminhos locais no navegador.

Se você possui Python instalado, pode rodar o seguinte comando dentro da pasta `WEB3`:

```bash
python3 -m http.server 8000
```

Após rodar o comando, abra o navegador e acesse:
- Página do Livro: `http://localhost:8000/Livro/`
- Página do Autor: `http://localhost:8000/Autor/`
