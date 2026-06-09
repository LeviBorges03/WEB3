# WEB3 - Ambiente Estático (Protótipo UI)

A pasta `WEB3` é um subprojeto isolado dentro do repositório principal do Projeto Biblioteca. Ela serve exclusivamente como o **campo de prototipagem** para o frontend da aplicação.

Aqui os desenvolvedores e designers podem trabalhar no visual, acessibilidade, estrutura HTML, regras de CSS e lógicas Vanilla de JavaScript, **sem a necessidade de rodar o framework backend (ASP.NET Core / C#)**.

## 🎯 Por Que Esta Pasta Existe?

1. **Desenvolvimento Focado no UI/UX:** Permite focar totalmente em marcação e estilo com ciclos de feedback instantâneos (Live Server).
2. **Separação de Preocupações:** O design e layout são validados e aprovados aqui primeiro, e somente depois a estrutura resultante é transportada e incorporada nos arquivos `.cshtml` da pasta `/Views` do servidor real.
3. **Apresentação Rápida:** Um protótipo navegável que não depende de nada mais do que um servidor estático básico, facilitando demonstrações.

## 📁 O Que Você Vai Encontrar Aqui

- `/Livro/index.html` - Protótipo completo e funcional da página de "Detalhes do Livro".
- `/Autor/index.html` - Protótipo da página biográfica dos autores.
- Os arquivos importam as folhas de estilo localmente dentro de suas respectivas subpastas ou da raiz web3, garantindo independência.

*(Note que as lógicas de pesquisa de barra ou favoritos implementadas nas Views do ASP.NET também têm versões parciais implementadas nestes estáticos para validação do comportamento e da atualização da árvore DOM).*

## 🚀 Como Executar o Protótipo Estático

Como a pasta contém apenas arquivos estáticos `.html`, `.css` e `.js`, você não precisa compilar nada. Use a sua extensão favorita do editor ou uma linha de comando local simples:

### Usando Python (Se Instalado)
Abra um terminal, acesse a pasta `WEB3/` e inicie um servidor HTTP básico:
```bash
python3 -m http.server 8000
```
Em seguida, acesse no navegador: `http://localhost:8000/Livro/index.html`.

### Usando NPM (http-server)
Caso tenha `node` na sua máquina e o pacote global `http-server`:
```bash
npx http-server -p 8000
```

## ⚠️ Regras e Manutenção
- Toda mudança visual estrutural solicitada pelo projeto **deve refletir a paridade entre `WEB3/` e os `.cshtml` do MVC**, visando consistência do repositório.
- Não injete código C# (`@Model`, `@Url.Action`) nestes arquivos.
