# WEB3 - Prototipagem de UI Estática

Este diretório contém os protótipos puramente estáticos (HTML, CSS, JavaScript básico) das interfaces da aplicação Biblioteca.

A arquitetura aqui se baseia no isolamento de componentes visuais para testes rápidos de design, responsividade e fluxo de interações simuladas (mockups) sem a necessidade de instanciar ou configurar o servidor ASP.NET Core presente na raiz do projeto.

## Estrutura
- **Autor/**: Contém o protótipo da página de Perfil do Autor (`index.html`, `style.css`).
- **Livro/**: Contém o protótipo da página de Detalhes da Obra (`index.html`, `style.css`).
- A raiz deste projeto mock (se existente) representaria a Home page (Catálogo).

## Como Visualizar

Para rodar os mockups e navegar nas telas isoladas localmente sem problemas de CORS ou bloqueios de arquivos locais, inicie um servidor HTTP Python simples a partir de dentro do diretório `WEB3`:

```bash
cd WEB3
python3 -m http.server 8000
```

Após o servidor iniciar, abra o seu navegador e acesse:
- `http://localhost:8000/Livro/` para ver o protótipo da obra.
- `http://localhost:8000/Autor/` para ver o protótipo do autor.

## Atenção ao Manter o Código
Como estes são mockups estáticos em relação ao projeto real (C# MVC), certifique-se de que quaisquer alterações de regras visuais (CSS) importantes sejam refletidas também em `wwwroot/css/` na aplicação principal.